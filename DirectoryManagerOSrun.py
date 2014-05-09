#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 09-05-2014
# PROGRAM: 
#####

##### PROGRAM DESCRIPTION #####
# This program manages and runs a series of 6 file creation programs
# 3 Programs for Type I - PTN chains + chemical ligand directories created
# 3 Programs for Type II - PTN chains + protein ligand directories created
#####

##### EXAMPLE #####
#
#
#####

import os           #allows operating system commands
from os import listdir
from os.path import isfile,isdir

run_program = "T"

print ("I - Type I: Directories are created for protein chains & chemical ligands")
print ("II - Type II: Directories are created for protein chains & protein ligands")
print ("Q - to quit\n")


while run_program == "T":
    type_selected = input("Enter I for Type I and II for Type II\n").upper()
    
    if (type_selected == "I"):
        print(type_selected)

        ###Run program DirectoryManagerTypeI###
        os.system('python3.3 /root/Scorpio2_PDB_Files/DirectoryManager/DirectoryManagerTypeI.py')
        ###Run program DirectoryManagerTypeI###
        os.system('python3.3 /root/Scorpio2_PDB_Files/DirectoryManager/MoveFilesChainsTypeI.py')
        ###Run program DirectoryManagerTypeI###
        os.system('python3.3 /root/Scorpio2_PDB_Files/DirectoryManager/MoveFilesLigandsTypeI.py')
        
    elif (type_selected == "II"):
        print(type_selected)
    elif (type_selected == "Q"):
        exit;
    else:
        print("Invalid selection, must be I or II\n")
        run_program = "T"

    continue_program = input("Type y if you would like to run this program again, or any key to exit?\n").upper()

    if continue_program == "Y":
        run_program = "T"
    else:
        run_program = "F"
