import json
import sys
import mutils

class User():
    ''' The User class which represents a User record in the address book.
        Instance attributes: user name, email, phone
    '''

    fileName = '../data.json'
        
    
    def __init__(self, name=None, email=None):
        ''' Initialize a new User instance with the data '''
        if name:
            self.__name = name

        if email:
            self.__email = email

    def __repr__(self):
        return str(self.getName()) + ' ' + str(self.getEmail())

    def getName(self):
        ''' Return the name of the user'''
        if self.__name:
            return self.__name
        else:
            return None

    def getEmail(self):
        ''' Return email '''
        if self.__email:
            return self.__email
        else:
            return None

    def setName(self, name):
        ''' Set Name attribute '''
        self.__name = name

    def setEmail(self, email):
        ''' Set Email attribute '''
        self.__email = email

    def save(self):
        ''' Save the data to the disk '''
        userDict = {self.getName(): self.getEmail()}
        return mutils.save(userDict, User.fileName)

class Message():

    ''' Message class: represnts a message. '''
    fileName = '../messages.json'

    def __init__(self, sender, content):
        if mutils.search(sender):
            self.__sender = sender
        else:
            raise Exception('Invalid user')
            
        self.__content = content


    def save(self):
        mdict = {self.getSender(): self.getContent()}
        return mutils.save(mdict, Message.fileName)
    
    def getSender(self):
        return self.__sender

    def getContent(self):
        return self.__content

