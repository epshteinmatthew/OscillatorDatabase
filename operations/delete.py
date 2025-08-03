#these would happen as github actions
import json
import os
import sys


def delete(path):
    try:
        with open("metadata.json", "r") as f:
            data = json.load(f)
        if os.path.isfile(path):
            paths = [path]
        else:
            paths = [pt for pt in os.listdir(path)]
        for item in data:
            print("yes")
            if item['path'] in paths:
                data.remove(item)
                break
        with open("metadata.json", "w") as f:
            json.dump(data, f)
        with open("checksum", "w") as ch:
            ch.write(( int(ch.read())+1).__str__())
        print("added model")
        return
    except:
        print("failed to add placeholder")

delete(sys.argv[1])
