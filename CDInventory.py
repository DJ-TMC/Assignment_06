#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TMcFarland, 2021-Feb-19, started mods: adding functions, looking at TODOs
#------------------------------------------#

#Importing os.path for additional FileProcessor.read_file functionality, to check to see if text file exists
import os.path

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of dicts to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def delete_dict(delDict):
        """Deletes lstTbl dicitonary entry based on user input of ID number
        Args:
            delDict (integer): ID number representing table entry

        Returns:
            NONE
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == delDict:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed\n')
        else:
            print('Could not find this CD!\n')


    @staticmethod
    def append_table(strID, strTitle, strArtist):
        # 3.3.2 Add item to the table
        """Takes arguments from Main loop append section and appends to lstTbl list of dictionaries in memory
        Args:
            strID (string): ID number
            strTitle (string): CD title
            StrArtist (string); Artist Name

        Returns:
            None
        """
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts). One line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        #check to see if database file already exists. If not, create blank one.
        if os.path.exists('CDInventory.txt'):
            #print('yay! already exists')
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        else:
            #create blank database in same folder as script
            objFile = open(strFileName, 'w')
            objFile.close()

    def write_file():
        """Writes List of Dicitonaries lstTbl from memory into a text file.
        Ensures proper comma seperated formatting for best storage and retrieval
        Args:
            None

        Returns:
            None
        """
        # TODO move processing code into function
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        print('Saved to file\n')


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """

        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def user_cd_input():
        """ Receives user input for CD ID number, Album Title, and Artist Name
        Args:
            None
        Returns:
            All strings: CD ID number, CD Title, CD Artist Name
        """

        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist


# -- MAIN PROGRAM -- #
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 EXIT process exit first
    if strChoice == 'x':
        break
    # 3.2 LOAD process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...\n')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 ADD CD process add a CD
    elif strChoice == 'a':
        #assign received data from user variables from return of IO.user_cd_input
        recStrId, recStrTitle, recStrArtist = IO.user_cd_input()
        #Feed received data from user into DataProcessor.append_table
        DataProcessor.append_table(recStrId, recStrTitle, recStrArtist)
        continue  # start loop back at top.
    # 3.4 DISPLAY INVENTORY process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 DELETE process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_dict(intIDDel)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 SAVE process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y' or 'yes':
            FileProcessor.write_file()
        #consider an elif for 'n' using code below and re-ask question for user if they enter anything else
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')