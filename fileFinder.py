""" This program parses your Downloads folder in Windows and returns a list with all the 
files that have even size in bytes, or have every vowel in their file name. 

It uses recursion to traverse every folder. You need Python to be installed on your computer. """

import os

def hasEvenlyBytesSize(fullFilePath):
    """Returns True if fullFilePath has an even size in bytes,
    otherwise returns False."""
    fileSize = os.path.getsize(fullFilePath)
    return fileSize % 2 == 0

def hasEveryVowel(fullFilePath):
    """Returns True if the fullFilePath has a, e, i, o , and u,
    otherwise returns False."""
    name = os.path.basename(fullFilePath).lower()
    return ('a' in name) and ('e' in name) and ('i' in name) and ('o' in name) and ('u' in name)


def walk(folder, matchFunc):
    """Calls the match funciton with every file in the folder and its subfolders.
    Returns a list of files that the match function returned True for."""
    matchedFiles = []
    folder = os.path.abspath(folder)

    # Loop over every file and subfolder in the selected folder
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        if os.path.isfile(filepath):
            # Call the match function for each file:
            if matchFunc(filepath):
                matchedFiles.append(filepath)
        
        elif os.path.isdir(filepath):
            # Recursevile call walk for each subolder, 
            # extending the matchedFiles with their matches:
            matchedFiles.extend(walk(filepath, matchFunc))

    return matchedFiles

# Get the user's Downolads folder
downloadFolder = os.path.expanduser('~') + "/Downloads/"


print('All files with even byte sizes:')
print(walk(downloadFolder, hasEvenlyBytesSize))

print()
print()

print('All files with every vowel in their name:')
print(walk(downloadFolder, hasEveryVowel))


