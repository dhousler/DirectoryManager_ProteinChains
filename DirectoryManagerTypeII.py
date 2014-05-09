#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 08-05-2014
# PROGRAM: DirectoryManagerTypeII
#####

##### PROGRAM DESCRIPTION #####
# This program takes the number of protein chains entered by a user
# creates x number of directories
# inside x directories it makes further directories for the protein chain ligands
# makes the following assumption ABCD --> AB main chain : CD ligand chains
#####

##### EXAMPLE #####
#
# User inputs = 4
# 
# 4 Chains: A B C D
#
# Assumes A and B are main protein chains:      dir: A
#                                               dir: B
#
# Assumes C and D are protein ligands chains:   dir: A -drill down-> dir: A_ligC + A_ligD
#                                               dir: B -drill down-> dir: B_ligC + B_ligD
#####

import os

start_directory = os.getcwd()

#create_dir = input("Enter the directory name: ")
chain_number = int(input("How many main protein chains are there? "))
chain_number = int(chain_number / 2)

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
        print(j)
        while (j <= chain_number) and (j <= length):
            if (not os.path.isfile(chains[j])) and (not os.path.isdir(chains[j])):
                os.mkdir(chains[i] + '_lig' + chains[j+chain_number])
            j += 1
        ### End Ligand Loop ###
            
        os.chdir(start_directory)
        
    i+= 1

### End of While loop ###
print('All files can be found in: '+ start_directory)
