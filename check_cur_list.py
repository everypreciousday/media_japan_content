# -*- conding: utf-8 -*-
import requests
import urllib.request
import json
import time
import xmltodict
import pprint
import re
import os.path

pp = pprint.PrettyPrinter(indent=4)

TARGET_FILE_PATH = "cur-list.yml"

class Item:
    def __init__(self):
        self.id = ""
        self.dir = ""
    def check_file(self):
        if self.id == "" or self.dir == "":
            return True
        check_path = self.dir + "\\" + self.id + ".html"
        if os.path.isfile(self.dir + "\\" + self.id + ".html") == False:
            print (check_path + " not exist!!!")

fp = open(TARGET_FILE_PATH, "r",encoding='UTF8')

lines = fp.readlines()
item = Item()
for line in lines:
    line = line.strip()

    if line == "-":
        item.check_file()
        item = Item()
    elif line.startswith("id"):
        item.id = line.split(":")[1].strip()
    elif line.startswith("dir"):
        item.dir = line.split(":")[1].strip()
