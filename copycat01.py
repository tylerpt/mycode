#!/usr/bin/env python3

import shutil
import os

def main():
    os.chdir("/home/student/mycode/") # move cwd

    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy") #shutil.copy(source, destination) - copy single file

    shutil.copytree("5g_research/", "5g_research_backup/") #copy entirety of src directory to dest directory

main()