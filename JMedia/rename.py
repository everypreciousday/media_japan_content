import os

arr = os.listdir('.')
for item in arr:
    if item.endswith('html'):
        print(item)
        os.rename(item, item.replace("html", "md"))
    #os.rename
