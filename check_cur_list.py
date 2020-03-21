# -*- conding: utf-8 -*-
import time
import pprint
import re
import os.path

pp = pprint.PrettyPrinter(indent=4)

TARGET_FILE_PATH = "cur-list.yml"

class Item:
    def __init__(self):
        self.id = ""
        self.dir = ""
        self.vid = ""
        self.ver = ""
        self.t1 = ""
        self.t2 = ""
    def print(self):
        print ("  -")
        print ("    dir: " + self.dir)
        print ("    id: " + self.id)
        print ("    ver: " + self.ver)
        print ("    t1: " + self.t1)
        print ("    t2: " + self.t2)

    def check_field(self):
        if self.id == "" or self.dir == "" or self.vid == "" or self.ver == "" or self.t1 == "" or self.t2 == "":
            print ("!!something is missing:")
            self.print()
    def check_file(self):
        if self.id == "" or self.dir == "":
            return True
        check_path = self.dir + "\\" + self.id + ".html"
        if os.path.isfile(self.dir + "\\" + self.id + ".html") == False:
            print (check_path + " not exist!!!")

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
    elif line.startswith("id"):
        item.id = line.split(":")[1].strip()
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
