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


