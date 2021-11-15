#--------------------------------------------------------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# James Crockett, 2021-Nov-07, Added assignment 5 pseudo code objectives, lines 18-25.
# James Crockett, 2021-Nov-09, Replaced inner list with dictionary for Add CD, line 70.
# James Crockett, 2021-Nov-11, Fixed code to Display Inventory, lines 75-78.
#                              Updated [s] save inventory code block to save dictionary 
#                              collection to txt file, lines 119-126.
# James Crockett, 2021-Nov-12, Add delete functionality of a CD entry, lines 80-92.
# James Crockett, 2021-Nov-13, Refactor delete functionality for 'd' code block, 
#                              lines 80-115. Clean up redundancy of some print statements 
#                              in the body by using variables in lines 34-37.
#                                                                                         
#--------------------------------------------------------------------------------------------#

# ==========================
# Assignment 5 Objectives
# ==========================
# [Completed]- Modify the script as required to replace the inner data structure by dictionaries.
# [Completed]- Add the functionality of loading existing data.
# [Completed]- Add functionality of deleting an entry.
# [Completed]- Your finished script must use a list of dictionaries as 2D table
# [Completed]- Declare variables

# Variables to be used in body of code
strChoice = ''  # User input
lstTbl = []  # list of dictionaries to hold data
# TODO replace list of lists with list of dicts
dictRow = {}  # dictionaryt of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strCdHeader = ('ID, CD Title, Artist') #Header titles for CD Inventory
strCurInv = ('This is your current inventory from your application memory') #user notification
strUpdInv = ('This is your updated inventory. Please select "s" from main ' \
              'menu to save your changes.') #user notification
boolDel = None # user delete flag
    
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD and overwrite Inventory\n[s] Save Inventory to file\n[x] exit\n')
    # convert choice to lower case at time of input
    strChoice = input('l, a, i, d, s or x: ').lower()
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dictRow = {'ID': int(lstRow[0]), 'Title':lstRow[1], 'Artist':lstRow[2]}
            lstTbl.append(dictRow)
        objFile.close()


    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dictRow)

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print(strCdHeader)
        for row in lstTbl:
            print(row, sep=', ')
        print()

    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        # delete CD entry by ID, Title, or Artist
        print()
        print(strCurInv)
        print()
        print(strCdHeader)
        for row in lstTbl:
            print(row, sep=', ')
        print()
        print()
        intId = int(input('Enter the ID number you want to delete: '))
        
        for row in lstTbl:
            #for list, use index format: row[0], for dict, use key name ['ID']
            if row['ID'] == intId:
                lstTbl.remove(row)
                boolDel = True #bool flag used for line 102 code block
              
        
        #Auto display updated inventory 'if' user deletes a row
        #else inform user value does not exist and to try again
        if boolDel == True:
            print()
            print(strUpdInv)
            print()
            print(strCdHeader)
            for row in lstTbl:
                print(row, sep=', ')
            print()
            print()
        else:
            print()
            print('That ID does not exist in your collection, returning ' \
                 'to main menu. Please enter "d" from main menu and retry.')
            print()

    elif strChoice == 's':
       # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')#overwrite txt file since user is loading inventory into memory before saving
        for row in lstTbl:
            dictRow = ''
            for item in row.values():
                dictRow += str(item) + ','
            dictRow = dictRow[:-1] + '\n'
            objFile.write(dictRow)
        objFile.close()


    else:
        print('Please choose either l, a, i, d, s or x!')
