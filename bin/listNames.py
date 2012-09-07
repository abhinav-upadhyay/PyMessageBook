import sys

def main():
    sys.path.append('../PyMessageBook')
    import mutils
    name_list = mutils.getNames()
    if name_list:
        for name in name_list:
            print name
    else:
        print 'No contacts found'

if __name__ == '__main__':
    main()
