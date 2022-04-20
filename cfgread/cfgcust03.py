#!/usr/bin/env python3

with open("vlanconfig.cfg", "r") as vlanfile:
    readfile = vlanfile.read()
    configlist = readfile.splitlines()

print(len(configlist))