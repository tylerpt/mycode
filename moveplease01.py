#!/usr/bin/env python3

import shutil
import os

def main():
    os.chdir('/home/student/mycode') #change cwd
    shutil.move('raynor.obj', 'ceph_storage/') #move raynor.obj to ceph_storage dir - will overwrite if already exists

    xname = input('what is the new name for kerrigan.obj? ') #prompt user for xname input

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #move to same dir with xname as new filename

main()