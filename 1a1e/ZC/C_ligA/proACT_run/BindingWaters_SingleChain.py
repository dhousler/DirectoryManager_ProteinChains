#!/usr/bin/env python

# Creation Date: 16-02-2014
# Last update: 19-02-2014
# Author: Dale Housler
# Find Binding Waters

'''
This program sorts the water column in order
Matches aby chain/ ligand with the same water number, (binding waters)
Counts the number of binding waters.
'''

'''
NOTE: Currently this program only works if one chain at a time is compared

If sorted is ignored assumes that the proACT HOH list will always be ordered,
this is dangerous

Needs revision in these areas!!
'''

# REFERENCE #
# www.youtube.com/watch?v=Vvkn3y7qAKs
#

import csv
import operator
import os
from os import listdir
from os.path import isfile,isdir



FileInput = input("Enter the csv file to use: ")
OpenFile = open(FileInput, 'r')
#OpenFile = open('/root/Scorpio2_PDB_Files/CSVruns/1a1e/1a1e_ALL_PTNChains_run1_residue_contacts.csv', 'r')

os.chdir("..")
contacts_file = input("Enter the file name for the contacts to be saved under\n")

if ((contacts_file != ("")) or (contacts_file != (" ")) or (contacts_file != ("\n"))):
        path = os.getcwd()
        print (path)
        save_g = (contacts_file)
        g = open(save_g, 'a+')
        g.write("\n")
else:
        print("File not saved")
        conti = 'n'

csvFile = csv.reader(OpenFile, delimiter=',' , quotechar=' ') # remove quotechar if want to remove double quotes around string values
sort = sorted(csvFile, key=operator.itemgetter(int(x=3))) #int(x=3) sets the col value to an integer

store_HOH = []
store_HOH1 = []
storeHOH1 = []
store_HOH2 = []
storeHOH2 = []

#print ('Check water order\n')
for line in sort: # can change to csvFile if waters pre-sorted
    #print(line)
    if (('"HOH"' in line) or ('HOH' in line)):
        #print(line)
        ##print(line[1:5])
        store_HOH += [line[1:5]] # if you want this to be individual strings use () instead of []

chain_store = []
bindingWater_positions = []
count_bridgingWaters = 0
bridgingWater_positions = []
count_bridgingWaters_withZ = 0
count_bindingWaters = 0

for i,line in enumerate(store_HOH): #skips the header line
    store_HOH1 = store_HOH[i]
    ##print (store_HOH[i])
    store_HOH2 = store_HOH[i-1] #set to i-1 NOT i+1 because want 1 less as skipped the first to make the comparison
    ##print (store_HOH[i])
    
    if ((store_HOH1[1] != store_HOH2[1]) and (store_HOH1[2] == store_HOH2[2])):
        ##print (store_HOH1)
        ##print (store_HOH2)
        store_chain1 = store_HOH1[1]
        store_chain2 = store_HOH2[1]
        
        if ((store_chain1 in ('Z','"Z"')) and (store_chain2 != store_chain1)):
            ## this if checks scenario AB Z
            print (store_HOH1)
            g.write(str(store_HOH1)+ "\n")
            print (store_HOH2)
            g.write(str(store_HOH2)+ "\n")
            count_bindingWaters +=1
            #if store_HOH1[2] not in bindingWater_positions:
                #bindingWater_positions += [store_HOH1[2]] #get position to determine if a binding or bridging water
         
            
         

##print(bindingWater_positions)
#length_binding = len(bindingWater_positions)

print ("\nBinding water count = ", count_bindingWaters) #'{Considers multi-chain bridge and counts as 1}')
g.write ("\nBinding water count = " + str(count_bindingWaters) + "\n")
g.close()
#if (count_bridgingWaters_withZ > 0):
    #print ("Binding water TOTAL count = ", (count_bindingWaters + count_bridgingWaters_withZ)-1)
    ##subtract 1 for the ligand chain interaction already counted
#else:
   # print ("Binding water TOTAL count = ", (count_bindingWaters + count_bridgingWaters_withZ))

