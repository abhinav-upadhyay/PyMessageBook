import sys

def main(argv):
    sys.path.append('../PyMessageBook')
    from messaging import User
    userName = argv[1]
    userEmail = argv[2]
    user = User(userName, userEmail)
    user.save()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: addContact <user-name> <email>'
    else:
        main(sys.argv)
