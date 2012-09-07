import json

FILENAME = './data.json'

def search(name):
    try:
        f = open(FILENAME, 'r')
    except IOError:
        return None

    user_dict = json.load(f)
    f.close()
    return user_dict.get(name)

def listContacts():
    try:
        f = open(FILENAME, 'r')
    except IOError:
        return None

def save(d, fileName):
    try:
        f = open(fileName, 'r')
        previousData = json.load(f)
    except (IOError, ValueError):
        previousData = None
        f = None

    if f:
        f.close()
    f = open(fileName, 'w')
    if previousData:
        d = dict(previousData.items() + d.items())

    newRecord = json.dumps(d)
    f.write(newRecord)
    f.close()
    return True


