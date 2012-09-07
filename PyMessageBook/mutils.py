import json

CONTACTS_FILENAME = '../data.json'

def search(name):
    try:
        f = open(CONTACTS_FILENAME, 'r')
    except IOError:
        return None

    user_dict = json.load(f)
    f.close()
    return user_dict.get(name)

def getContacts():
    try:
        f = open(CONTACTS_FILENAME, 'r')
    except IOError:
        return None
    contacts_dict = json.load(f)
    f.close()
    return contacts_dict

def getNames():
    try:
        f = open(CONTACTS_FILENAME, 'r')
    except IOError:
        return None
    contacts_dict = json.load(f)
    f.close()
    return contacts_dict.keys()

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


