import sys
def main():
    sys.path.append('../PyMessageBook')
    import mutils
    contacts = mutils.getContacts()
    if contacts:
        for k, v in contacts.iteritems():
            print str(k) + ': ' + str(v)
    else:
        print 'No contacts found.'

if __name__ == '__main__':
    main()
