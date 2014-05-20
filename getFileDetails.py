#!/usr/bin/env python

import os
import re
import csv

start_directory = os.getcwd()

########## Subroutines ##########

##### Finds the ligand chain from the files in the directory #####
def GetLigandChain_ref():
    ligChain_files = [f for f in os.listdir(start_directory) if f.endswith('.mol2')]

    chain_files_str = str(ligChain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str)
    chain_files_str = re.sub('.mol2','',chain_files_str) # removes the file type

    underscore_split = re.split('\_',chain_files_str)

    return (underscore_split[3])
#####End

##### Finds the PDB reference from the files in the directory #####
def GetPDB_ref():
    ligChain_files = [f for f in os.listdir(start_directory) if f.endswith('.mol2')]

    chain_files_str = str(ligChain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str)
    chain_files_str = re.sub('.mol2','',chain_files_str) # removes the file type

    underscore_split = re.split('\_',chain_files_str)

    return (underscore_split[0])
#####End

##### Finds the protein chain from the files in the directory #####
def GetPTNChain_ref():
    Chain_files = [f for f in os.listdir(start_directory) if f.endswith('.pdb')]

    chain_files_str = str(Chain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str)
    chain_files_str = re.sub('.pdb','',chain_files_str) # removes the file type
    chain_files_str = re.sub('Chain','',chain_files_str)# removes word 'Chain' from file name
    
    underscore_split = re.split('\_',chain_files_str)

    return (underscore_split[1])
#####End

########## End Subroutines ##########

### Return Values fron subroutines ###
pdb_ref = GetPDB_ref()
chain_ref = GetPTNChain_ref()
ligand_ref = GetLigandChain_ref()

### Change directory to top level
os.chdir ('../..') # moves the log file to the pdb top directory

### Create the Log file 
save_f = (pdb_ref + '_log.csv')
g = open(save_f, 'a+')
g.close()#Closes PDB File

### Check if log file is empty, if empty writes heading else no header only body data is written

header = 'pdb_ref,Protein Chain,Ligand,Polar Count, Apolar Count, Binding Water Count, Total Count,'

if os.stat(save_f).st_size==0: #Checks if file is empty
    
    ### Print heading to File ###
    g = open(save_f, 'a+') #Writes to file by adding (w overwrites but then the last line only appears
    g.write(header)
    g.write('\n') #Skips header if found
    ### Print body to File ###
    g.write(pdb_ref + ',' + chain_ref + ',' + chain_ref  + '_' + ligand_ref + ',' )
    g.write('\n')
    g.close()#Closes PDB File
else:
    ### Prints Body to file ###
    g = open(save_f, 'a+')
    g.write(pdb_ref + ',' + chain_ref + ',' + chain_ref  + '_' + ligand_ref + ',' )
    g.write('\n')
    g.close()#Closes PDB File

### Print to Screen ###

logfile_directory = os.getcwd()
print("Details written to file: " + logfile_directory + "/" + save_f)

