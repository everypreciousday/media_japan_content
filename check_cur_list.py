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

    def check_field(self):
        if self.uid == "" or self.dir == "" or self.vid == "" or self.ver == "" or self.t1 == "" or self.t2 == "":
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
        if os.path.isfile(check_path / check_file_name) == False:
            print (self.dir + "/" + check_file_name + " not exist!!!")

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
