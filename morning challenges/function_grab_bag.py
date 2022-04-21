#!/usr/bin/env python3

samplestring = 'What is the DEAL with airline food?'

def upperlower(string):
    uppercounter = 0
    lowercounter = 0
    splitstring = string.split(' ')
    for i in splitstring:
        if i.islower():
            lowercounter + 1
        elif i.isupper():
            uppercounter + 1
    print('number of lowercase characters is:' + lowercounter)
    print('number of uppercase characters is:' + uppercounter)

upperlower(samplestring)