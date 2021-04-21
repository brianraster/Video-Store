import json

def loadData(filename):
    with open(filename, 'r') as f:
        temp = json.load(f)
        return temp

def writeData(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)