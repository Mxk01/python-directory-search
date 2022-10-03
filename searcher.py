import glob,os 
import tkinter as tk
import re
from colorama import Fore
from colorama import Style


# Hi  guys Today I will be showing you a simple  text finder program in python
# let's get started :)  

# first we have the init__program function  then some funny looking ascii art 
def init__program():
 print("""\
.
──────────────────────────────────
───────────────▀█▄█▀──────────────
────────▄█████▄─███───────────────
──────▄████████████▄██████▄───────
──────██████████████████████──────
──────██████████████████████──────
──────██████████████████████──────
──────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█──────
──────██████████████████████──────
────▄█▀▀──────────────────▀▀█▄────
──▄█▀────────────────────────▀█▄──
─█▀────▄▀▀▀▀▄────────▄▀▀▀▀▄────▀█─
─█────█──▄▄──█─▄▀▀▄─█──▄▄──█────█─
─█────█─████─██░░░░██─████─█────█─
██──▄▄███████▀░░░░░░▀███████▄▄──██
█──▀█░░░░░░░░░░▄▄▄▄░░░░░░░░░░█▀──█
█───▀█▀▄▄▄▄▄▄▀▀░░░░▀▀▄▄▄▄▄▄▀█▀───█
█────▀▄░░░░░░░░▄▄▄▄░░░░░░░░▄▀────█
██─────▀▀▀▀▀▀▀▀────▀▀▀▀▀▀▀▀─────██
─█──────────────────────────────█─
─█▄────────────────────────────▄█─
──█▄──────────────────────────▄█──
───█▄────────────────────────▄█───
──────────────────────────────────
      """)
 # first it look for the folder path 
 searchDirectory  = input('Enter folder path :')
 # then our list of directories where we have our own 
 dir_list = os.listdir(searchDirectory)
 a=0

 print("The following files were found in  '", searchDirectory, "' :")

 # prints all files  # we loop in the list of directories 
 for line in dir_list:
    
    a+=1
    print(f"{Fore.YELLOW}{str(a-1)} ){line}{Style.RESET_ALL}")


 
 # you can choose a specific file 
 choosenFile = dir_list[int(input('Choose a file : '))] 
 print(choosenFile)

 word = input('Enter the word you want to find : ')
 # so basically we change the directory so we can loop in our folder that we chose
 os.chdir(searchDirectory)
 wordExists = False
 i=0
 lines = [] 
 # loop through text files in that specific directory
 with open(choosenFile,"r") as file:
     # reading each line    
    for line in file:
   
        # reading each word        
        for foundWord in line.split():
            #print(foundWord==word)
            i+=1
            # print(line)
            # displaying the words           
            if foundWord==word:
               wordExists=True
               lines.append(i)
            else :
               wordExists=False
 if(len(lines)>0):
   # Let's change our text file a bit 
      print(f"{Fore.GREEN}{str(len(lines))} entries found at the following lines {str(lines)}{Style.RESET_ALL}")
 else:
      print("Word doesn't exist")
init__program()