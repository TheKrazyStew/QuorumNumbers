 ############################
# The Zip Code Member Search #
# Author: Kevin Stewart      #
 ############################

# OBJECTIVE:
    # Import the list of members as a .txt to read (Done)
    # Import the list of zip codes as a .txt to read (Done)
    # Find the number of zip codes in members.txt that are also in zipcodes.txt
    # Print the result to the console
# PRECONDITIONS:
    # Both lists are .txt files
    # Both files contain the necessary data ONLY; No headers, footers, or extra data
    # In the zip code file, the zip codes are all in one line, separated by commas
    # In the member list file, each member has one line, with each piece of data separated by tabs ('   ')
    
# Input
print("Before we continue, please ensure that the list of members and the list of zip codes are in the same folder as this file.\n")
nameFileMem = str(input("Please enter the name of the file that contains the list of members (remember the .txt at the end!): "))
nameFileZip = str(input("Please enter the name of the file that contains the list of zip codes (remember the .txt at the end!): "))

# Import, Variables
fileMem = open(nameFileMem, mode = 'r') # The list of members
fileZip = open(nameFileZip, mode = 'r') # The list of zip codes
fileOut = open('output.txt', mode = 'w') # The list of matches

totalCodes = 0
tabs = 0
currentLine = fileMem.readline() # Initialize the first line of the member list for later

# Process
zips = fileZip.readline() # Collecting the zip codes
zipList = zips.split(',') # Making a list of zip codes, separated by commas
# print(zipList) # Debugging; making sure the list is made


while currentLine != '': # As long as there are still lines left in the member list:
    currentList = currentLine.split('\t') # Making a list, separating data by tabs
    # print(currentList) # Debugging; making sure the list is made correctly
    
    if currentList[3][:5] in zipList: # If the zip code (item 3 in the list) is in the list of zip codes:
        totalCodes += 1 # Add 1 to the total
        fileOut.write(currentLine) # Write the line to the output file
    currentLine = fileMem.readline() # Go to the next line of the file

# Output
codes = str(totalCodes) # Now read-able by print()
print("\nThere are " + codes + " members that match the given zip codes.")
fileOut.write("TOTAL: " + codes)

# Close Files
fileMem.close()
fileZip.close()
fileOut.close()

# Stop The Program
input("Press ENTER to exit.")
