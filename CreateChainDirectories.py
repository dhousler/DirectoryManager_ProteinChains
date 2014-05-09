#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 08-05-2014
# PROGRAM: CreateChainDirectories
#####

##### PROGRAM DESCRIPTION #####
# This program takes the number of protein chains entered by a user
# creates x number of directories
#####

##### EXAMPLE #####
#
# User input = 4
# 
# 4 Chains: A B C D
#
# Assumes main protein chains A B C D:  dir: A
#                                       dir: B
#                                       dir: C
#                                       dir: D
#####

import os

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
        
    i+= 1

### End of While loop ###

print(str(chain_number) + " directories created.")
input("Press any key to exit.")
