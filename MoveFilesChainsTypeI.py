#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 08-05-2014
# PROGRAM: 
#####

##### PROGRAM DESCRIPTION #####
# This program itertates through a user defined number of chains
# It then finds a .pdb file related to that chain and copies it into the chain dir
# It also copies all .mol2 to that chain file for all chains 
#####

##### EXAMPLE #####
#
#
#####

import os           #allows operating system commands
import shutil       #allows file movement in different operating systems
import re

start_directory = os.getcwd()
#text_files = [f for f in os.listdir(path) if f.endswith('b.txt')]


#create_dir = input("Enter the directory name: ")
chain_number = int(input("How many chains are there? "))

#copyfile = input("Enter the file to copy: ")
chains = ['0','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z']

print("\nFiles copied:")

### Make directories - Beginning of while ###
i = 1
for i in range(1,chain_number+1):
    fileToFind = chains[i] + '.pdb'
    #print(fileToFind)
    chain_files = [f for f in os.listdir(start_directory) if f.endswith(fileToFind)] # collects all files ending with fileToFind details
    ## Find the file name as a string
    chain_files_str = str(chain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str) #uses re (regular expressions) to remove the ' and []
    print ('\nDirectory ' + chains[i] + ':')
    print(chain_files_str)
    ## end
    
    saveToDir = chains[i]
     
    shutil.copy2(chain_files_str, saveToDir) #moves files that end in a specific terminus

    #os.system("cp copyfile saveToDir") # cp file1 dir1
    #shutil.copy2(copyfile, saveToDir) # moves the file entered

    ### Ligand Loop - creates same chain with diff ligands dir###
    j = 1
    for j in range(1,chain_number+1):
        lig_fileToFind = chains[j] + '.mol2'
        #print(fileToFind)
        lig_chain_files = [f for f in os.listdir(start_directory) if f.endswith(lig_fileToFind)]
        #print(lig_chain_files)

        ## Find the file name as a string
        lig_chain_files_str = str(lig_chain_files)
        lig_chain_files_str = re.sub('[\'\[\]]','',lig_chain_files_str)
        print(lig_chain_files_str)
        ## end
        
        lig_saveToDir = chains[i]   #set to i NOT j so copies each file in i's directory
                                    #(otherwise will move files each time and overwrite)
        
        shutil.copy2(lig_chain_files_str, lig_saveToDir) #moves files that end in a specific terminus   
    j += 1
        ### End Ligand Loop ###
            
i+= 1

### End of While loop ###


input("\nSuccessful!\nPress any key to exit.")
