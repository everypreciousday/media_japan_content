# -*- conding: utf-8 -*-
import time
import pprint
import re
import os.path
from pathlib import Path

pp = pprint.PrettyPrinter(indent=4)

TARGET_FILE_PATH = "cur-list.yml"

class Item:
    def __init__(self):
        self.uid = ""
        self.enabled = ""
        self.dir = ""
        self.vid = ""
        self.ver = ""
        self.t1 = ""
        self.t2 = ""

    def print(self):
        print ("  -")
        print ("    dir: " + self.dir)
        print ("    uid: " + self.uid)
        print ("    ver: " + self.ver)
        print ("    t1: " + self.t1)
        print ("    t2: " + self.t2)
        print ("    enabled: " + self.enabled)

    def check_field(self):
        if self.uid == "" or self.dir == "" or self.vid == "" or self.ver == "" or self.t1 == "" or self.t2 == "" or self.enabled == "":
            print ("!!something is missing:")
            self.print()

    def check_file(self):
        if self.uid == "" or self.dir == "":
            return True

        # id should be lower cased.
        lowered = self.uid.lower()
        if self.uid != lowered:
            print("uid has upper case")
            self.print()

        check_path = Path(self.dir)
        check_file_name = self.uid + ".md"
        the_path = check_path / check_file_name
        if os.path.isfile(the_path) == False:
            print (the_path + " not exist!!!")

        itemfile = open(the_path, "r", encoding='UTF8')
        items = itemfile.readlines()
        for item in items:
            ruby_cnt = item.count("<Ruby>")
            ruby_end_cnt = item.count("</Ruby>")
            rt_cnt = item.count("<rt>")
            rt_end_cnt = item.count("</rt>")
            rb_cnt = item.count("<rb>")
            rb_end_cnt = item.count("</rb>")

            if ruby_cnt != ruby_end_cnt:
                print(the_path)
                print("ruby cnt not same")
                print(item)

            if rt_cnt != rt_end_cnt:
                print(the_path)
                print("rt cnt not same")
                print(item)

            if rb_cnt != rb_end_cnt:
                print(the_path)
                print("rb cnt not same")
                print(item)

        # check whether each sentence finish with <br> 
        f = open(the_path, "r", encoding='UTF8')
        lines = f.readlines()
        for line in lines:
            result = re.match(r".*<br><br>$", line)
            if result:
                print(str(the_path) + "\n" + line)
                continue
            result = re.match(r".*<br>$", line)
            if result:
                continue
            
            print(str(the_path) + "\n" + line)

fp = open(TARGET_FILE_PATH, "r",encoding='UTF8')
lines = fp.readlines()
item = Item()
cnt = 0
for line in lines:
    line = line.strip()

    if line == "-":
        # ignore 1st "-"
        if cnt == 0:
            cnt = 1
            continue
        item.check_field()
        item.check_file()
        item = Item()
    elif line.startswith("uid"):
        item.uid = line.split(":")[1].strip()
    elif line.startswith("dir"):
        item.dir = line.split(":")[1].strip()
    elif line.startswith("vid"):
        item.vid = line.split(":")[1].strip()
    elif line.startswith("ver"):
        item.ver = line.split(":")[1].strip()
    elif line.startswith("t1"):
        item.t1 = line.split(":")[1].strip()
    elif line.startswith("t2"):
        item.t2 = line.split(":")[1].strip()
    elif line.startswith("enabled"):
        item.enabled= line.split(":")[1].strip()
