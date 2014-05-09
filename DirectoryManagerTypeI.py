#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 08-05-2014
# PROGRAM: DirectoryManagerTypeI
#####

##### PROGRAM DESCRIPTION #####
# This program takes the number of protein chains entered by a user
# creates x number of directories
# inside x directories it makes further directories for the ligand chains
# assumes same number of attached ligands as chains
#####

##### EXAMPLE #####
#
# User input = 4
# 
# 4 Chains: A B C D
#
# Assumes main protein chains A B C D:          dir: A
#                                               dir: B
#                                               dir: C
#                                               dir: D
#
# Assumes cross reference of ligands chains:    dir: A -drill down-> dir: A_ligA + A_ligB + A_ligC + A_ligD
#                                               dir: B -drill down-> dir: B_ligC + B_ligD + B_ligC + C_ligD
#                                               dir: C -drill down-> dir: C_ligC + C_ligD + C_ligC + C_ligD
#                                               dir: D -drill down-> dir: D_ligC + D_ligD + D_ligC + D_ligD
#####
import os

start_directory = os.getcwd()

#create_dir = input("Enter the directory name: ")
chain_number = int(input("How many chains are there? "))
chains = ['0','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z']

length = len(chains)

### Make directories - Beginning of while ###
i = 1

while (i <= chain_number) and (i <= length):
    #print(chains[i])
    if (not os.path.isfile(chains[i])) and (not os.path.isdir(chains[i])):
        os.mkdir(chains[i])
        os.chdir(chains[i])
        
        ### Ligand Loop - creates same chain with diff ligands dir###
        j = 1
        while (j <= chain_number) and (j <= length):
            if (not os.path.isfile(chains[j])) and (not os.path.isdir(chains[j])):
                os.mkdir(chains[i] + '_lig' + chains[j])
            j += 1
        ### End Ligand Loop ###
            
        os.chdir(start_directory)
        
    i+= 1

### End of While loop ###
print('All files can be found in: ' + start_directory)
input("Press any key to exit!")
