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
# Checks are also made for user input
# There is the ability to quit
# The process has a continious cycle
#####

##### EXAMPLE #####
#
#
#####

import os           #allows operating system commands
import shutil       #allows file movement in different operating systems
import re

########## Subroutines ##########

######## Type I - PTN Chains with chemical Ligands ########

##### Create the main directories #####
def CreateMainDirectories_TypeI(chain_number):
    start_directory = os.getcwd()

    #chain_number = int(input("How many chains are there? "))

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
    print("\n" + str(chain_number) + " directories created successfully!")
    #print("All files can be found in: " + start_directory + "\n")
##### end #####

##### MoveChainFiles_TypeI #####
def MoveChainFiles_TypeI(chain_number):
    start_directory = os.getcwd()

    #chain_number = int(input("How many chains are there? "))

    chains = ['0','A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T',
              'U','V','W','X','Y','Z']

    print("\nFiles copied successfuly!")

    ### Make directories - Beginning of while ###
    i = 1
    for i in range(1,chain_number+1):
        fileToFind = 'Chain' + chains[i] + '.pdb'
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

        ### Ligand Loop - creates same chain with diff ligands dir###
        j = 1
        for j in range(1,chain_number+1):
            lig_fileToFind = '_' + chains[j] + '.mol2'
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
    
    #print("\nFiles copied successfuly!\n")

##### end #####

##### MoveLigandFiles_TypeI#####

def MoveLigandFiles_TypeI(chain_number):
    start_directory = os.getcwd()

    #chain_number = int(input("How many chains are there? "))

    chains = ['0','A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T',
              'U','V','W','X','Y','Z']

    print("\nAll files can be found in the following directories: \n")
    for k in range(1,chain_number+1):
        path = start_directory + '/' + chains[k]
        print(path)
        os.chdir(path)
        chain = chains[k]

        ### Make directories - Beginning of while ###
        i = 1
        for i in range(1,chain_number+1):
            fileToFind = 'Chain' + chain + '.pdb'
            #print(fileToFind)
            chain_files = [f for f in os.listdir(start_directory) if f.endswith(fileToFind)] # collects all files ending with fileToFind details
            ## Find the file name as a string
            chain_files_str = str(chain_files)
            chain_files_str = re.sub('[\'\[\]]','',chain_files_str) #uses re (regular expressions) to remove the ' and []
            #print ('\nDirectory ' + chains[i] + ':')
            #print(chain_files_str)
            ## end
    
            saveToDir = chain + '_lig' + chains[i]
     
            shutil.copy2(chain_files_str, saveToDir) #moves files that end in a specific terminus

            ### Ligand Loop - creates same chain with diff ligands dir###
            j = 1
            for j in range(1,chain_number+1):
                lig_fileToFind = '_' + chains[j] + '.mol2'
                #print(fileToFind)
                lig_chain_files = [f for f in os.listdir(start_directory) if f.endswith(lig_fileToFind)]
                #print(lig_chain_files)

                ## Find the file name as a string
                lig_chain_files_str = str(lig_chain_files)
                lig_chain_files_str = re.sub('[\'\[\]]','',lig_chain_files_str)
                #print(lig_chain_files_str)
                ## end
        
                lig_saveToDir = chain + '_lig' + chains[j]   #set to j NOT i so copies specific file in i's directory
                                    
                shutil.copy2(lig_chain_files_str, lig_saveToDir) #moves files that end in a specific terminus   
            j += 1
            ### End Ligand Loop ###
            
        i+= 1

        ### End of While loop ###
    k += 1
    os.chdir(start_directory) #otherwise will start to create next set of files in this directory
    #print("\nFiles moved successful!\n")
##### end #####

######## end Type I #######################################################################################################################

######## Type II - PTN Chains with PTN Ligands ########
def CreateMainDirectories_TypeII(chain_number):
    start_directory = os.getcwd()

    #chain_number = int(input("How many main protein chains are there? "))
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
            #print(j)
            while (j <= chain_number) and (j <= length):
                if (not os.path.isfile(chains[j])) and (not os.path.isdir(chains[j])):
                    os.mkdir(chains[i] + '_lig' + chains[j+chain_number])
                j += 1
            ### End Ligand Loop ###
            
            os.chdir(start_directory)
        
        i+= 1

    ### End of While loop ###
    print("\n" + str(chain_number) + " directories created successfully!")
    #print('All files can be found in: '+ start_directory)
##### END #####

##### MoveChainFiles_TypeI #####
def MoveChainFiles_TypeII(chain_number):
    start_directory = os.getcwd()

    #chain_number = int(input("How many chains are there? "))
    chain_number = int(chain_number / 2) #half the number as the other half are ligand chains
    
    chains = ['0','A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T',
              'U','V','W','X','Y','Z']

    print("\nFiles copied successfuly!")

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

        ### Ligand Loop - creates same chain with diff ligands dir###
        j = 1
        for j in range(1,chain_number+1):
            lig_fileToFind = 'Chain' + chains[j+2] + '.mol2'
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
        
##### END #####
    
##### MoveLigandFiles_TypeII#####
def MoveLigandFiles_TypeII(chain_number):
    start_directory = os.getcwd()

    #chain_number = int(input("How many chains are there? "))
    chain_number = int(chain_number / 2) #half the number as the other half are ligand chains
    
    chains = ['0','A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T',
              'U','V','W','X','Y','Z']

    print("\nAll files can be found in the following directories: \n")
    
    for k in range(1,chain_number+1):
        path = start_directory + '\\' + chains[k] #windows
        #path = start_directory + '/' + chains[k]  #Unix
        print(path)
        os.chdir(path)
        chain = chains[k]

        ### Make directories - Beginning of while ###
        i = 1
        for i in range(1,chain_number+1):
            fileToFind = chain + '.pdb'
            #print(fileToFind)
            chain_files = [f for f in os.listdir(start_directory) if f.endswith(fileToFind)] # collects all files ending with fileToFind details
            ## Find the file name as a string
            chain_files_str = str(chain_files)
            chain_files_str = re.sub('[\'\[\]]','',chain_files_str) #uses re (regular expressions) to remove the ' and []
            #print ('\nDirectory ' + chains[i] + ':')
            #print(chain_files_str)
            ## end
    
            saveToDir = chain + '_lig' + chains[i+2]
     
            shutil.copy2(chain_files_str, saveToDir) #moves files that end in a specific terminus

            ### Ligand Loop - creates same chain with diff ligands dir###
            j = 1
            for j in range(1,chain_number+1):
                lig_fileToFind = 'Chain' + chains[j+2] + '.mol2'
                #print(fileToFind)
                lig_chain_files = [f for f in os.listdir(start_directory) if f.endswith(lig_fileToFind)]
                #print(lig_chain_files)

                ## Find the file name as a string
                lig_chain_files_str = str(lig_chain_files)
                lig_chain_files_str = re.sub('[\'\[\]]','',lig_chain_files_str)
                #print(lig_chain_files_str)
                ## end
        
                lig_saveToDir = chain + '_lig' + chains[j+2]   #set to j NOT i so copies specific file in i's directory
                                    
        
                shutil.copy2(lig_chain_files_str, lig_saveToDir) #moves files that end in a specific terminus   
            j += 1
                ### End Ligand Loop ###
            
        i+= 1

        ### End of While loop ###
    k += 1
    #os.chdir(start_directory)
    #input("\nSuccessful!\nPress any key to exit.")
##### END #####
    
########## end subroutines ############################################################################################

########## MAIN PROGRAM ##########

run_program = "T"

print ("I - Type I: Directories are created for protein chains & chemical ligands")
print ("II - Type II: Directories are created for protein chains & protein ligands")
print ("Q - to quit\n")


while run_program == "T":
    type_selected = input("Enter I for Type I and II for Type II\n").upper()
    
    if (type_selected == "I"):
        #print(type_selected)
        chain_number = int(input("How many chains are there? "))

        ###Run Subroutine: CreateMainDirectories_TypeI###
        CreateMainDirectories_TypeI(chain_number)

        ###MoveFilesChainsTypeI###
        MoveChainFiles_TypeI(chain_number)

        ###MoveFilesLigandsTypeI###
        MoveLigandFiles_TypeI(chain_number)
        
    elif (type_selected == "II"):
        #print(type_selected)
        chain_number = int(input("How many chains are there? "))

        ###Run Subroutine: CreateMainDirectories_TypeI###
        CreateMainDirectories_TypeII(chain_number)

        ###MoveFilesChainsTypeI###
        MoveChainFiles_TypeII(chain_number)

        ###MoveFilesLigandsTypeI###
        MoveLigandFiles_TypeII(chain_number)
        
    elif (type_selected == "Q"):
        exit;
    else:
        print("Invalid selection, must be I or II\n")
        run_program = "T"

    continue_program = input("\nType y if you would like to run this program again, or any key to exit.\n").upper()

    if continue_program == "Y":
        run_program = "T"
    else:
        run_program = "F"

