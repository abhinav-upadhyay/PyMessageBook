#-
# Copyright (c) 2012 Abhinav Upadhyay <er.abhinav.upadhyay@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
# COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

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

