#!/usr/bin/env python

import os
import re

start_directory = os.getcwd()

def GetLigandChain_ref():

    ligChain_files = [f for f in os.listdir(start_directory) if f.endswith('.mol2')]
    chain_files_str = str(ligChain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str)
    #print(ligChain_files)

    chain_files_str = re.sub('.mol2','',chain_files_str) # removes the file type
    underscore_split = re.split('\_',chain_files_str)

    print (underscore_split[3])

def GetPDB_ref():
    ligChain_files = [f for f in os.listdir(start_directory) if f.endswith('.mol2')]
    chain_files_str = str(ligChain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str)
    #print(ligChain_files)

    chain_files_str = re.sub('.mol2','',chain_files_str) # removes the file type
    underscore_split = re.split('\_',chain_files_str)

    print (underscore_split[0])

def GetPTNChain_ref():
    Chain_files = [f for f in os.listdir(start_directory) if f.endswith('.pdb')]
    chain_files_str = str(Chain_files)
    chain_files_str = re.sub('[\'\[\]]','',chain_files_str)
    #print(Chain_files)

    chain_files_str = re.sub('.pdb','',chain_files_str) # removes the file type
    chain_files_str = re.sub('Chain','',chain_files_str)# removes word 'Chain' from file name
    print(chain_files_str)
    underscore_split = re.split('\_',chain_files_str)

    print (underscore_split[1])

#####

GetLigandChain_ref()
GetPDB_ref()
GetPTNChain_ref()
