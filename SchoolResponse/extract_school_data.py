#!/usr/bin/env python

'''
extract_school_data.py
  Author(s): Ikeoluwa Agbaje (1125093)
  Previous Author(s): Andrew Hamilton-Wright

  Project: COVID-19 in Ontario
  Date of Last Update: April 01, 2021

  Functional Summary
    extract_school_data.py will extract data from two files - one containing dates and the number of scools closed for each date, and another containing dates and the number of schools with confirmed COVID-19 cases for each date (there will be more data in each file but these are the relevant data for this program). After the relevant data has been extracted and processed, it will be printed to a csv file using the output redirection command in the command line. The csv file will have the format:
    Date,State Of School,Number Of Schools 
    where State Of School is either number of schools closed or number of schools with confirmed cases for each day.

  Commandline Parameters: 2
    argv[1] = schoolcovidsummary file
    argv[2] = schoolsactivecovid file

  Running:
    python SchoolResponse/extract_school_data.py data/schoolcovidsummary.csv data/schoolsactivecovid.csv > SchoolResponse/extracted_school_data.csv
'''


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv


# This is a dictionary -- a data structure that associates
# values (in this case integers) with names.

# Index map for the school covid summary file based on the first 4 columns 
# (there are 17 more columns but they are irrelvant to this program)
COVID_SUMMARY_INDEX_MAP = {
        "Collected_Date" :  0,
        "Reported_Date" :  1,
        "Current_Schools_With_Cases" :  2,
        "Current_Schools_Closed" :  3 }

# Index mapping for the schools active covid file based on the 10 columns in the file
ACTIVE_COVID_INDEX_MAP = {
        "Collected_Date" :  0,
        "Reported_Date" :  1,
        "School_Board" :  2,
        "School_ID" :  3,
        "School" :  4,
        "Municipality" :  5,
        "Confirmed_Student_Cases" :  6,
        "Confirmed_Staff_Cases" :  7,
        "Confirmed_Unspecified_Cases" :  8,
        "Total_Confirmed_Cases" :  9 }

# Main function
def main (argv):

    '''
    Load two data files and print out the columns matching the selected
    indices
    '''

    #
    #   Check that we have been given the right number of parameters (3),
    #   and store the command line arguments in appropriate variables
    #
    if len(argv) != 3:
        print("Usage: SchoolResponse/extract_school_data.py <schoolcovidsummary file> <activeschoolcovid file>")

        # We exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    # Saves the file names given from the command-line in appropriate string variables
    schoolCovidSummaryFile = argv[1]
    activeSchoolCovidFile = argv[2]

    #
    # Attempts to open both files using a utf-8-sig encoding 
    # and exits with a non-zero value if there is an error opening any of the files after printing an error message
    #
    try:
        schoolCovidSummaryFh = open(schoolCovidSummaryFile, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                schoolCovidSummaryFile, err), file=sys.stderr)
        sys.exit(1)

    try:
        activeSchoolCovidFh = open(activeSchoolCovidFile, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                activeSchoolCovidFile, err), file=sys.stderr)
        sys.exit(1)

    # Reads the opened csv files and stores them in corresponding variables
    schoolCovidSummaryReader = csv.reader(schoolCovidSummaryFh)
    activeSchoolCovidReader = csv.reader(activeSchoolCovidFh)


    #
    # Variable Declarations
    #
    # Array to store the extracted active school cases data after the file has been read through and filtered to get only the necessary columns
    # Useful because this data will have to be read through in its entirety multiple times (for nearly every sigle line in the school covid summary file). Creating an array with only the relevant data instead of using the original file makes this reading more effecient because not only is it easier to go back to the beginning of the array each time, there is also less data to be read through each time making the program run faster
    activeSchoolCovidExtractedData = []

    # Array to store the final extracted data needed to create the graph visualization. 
    # It will hold the date, number of schools with confirmed cases, and number of schools closed
    finalExtractedData = []

    # Integers to store the current row number when going through active school cases array
    # and the total number of lines in the array
    stringRow = 0
    numOfLines = 0
    
    # Loop that goes through the active school cases file to extract the necessary information and put it in an array for simplicity of going through the data
    # Stores the reported date (column 2) and total number of confirmed cases (column 9) from the file to the array
    # If statement is used to ignore the first line from the file since it does not contain any actual data
    # activeSchoolCovidString array holds information from the current row
    for row in activeSchoolCovidReader:
        if ((row[0][0].isnumeric()) == True):
            activeSchoolCovidString = []

            activeSchoolCovidString.append(row[ACTIVE_COVID_INDEX_MAP["Reported_Date"]])
            activeSchoolCovidString.append(row[ACTIVE_COVID_INDEX_MAP["Total_Confirmed_Cases"]])

            activeSchoolCovidExtractedData.append(activeSchoolCovidString)

            numOfLines += 1

    # Loop that goes through the school covid summary file to extract the reported date and the number of schools closed for that day
    # The while loop compares the reported date from the covid summary file to the reported date in the activeSchoolCovidExtractedData array
    # If a match is found between the dates (meaning there was a covid case in a school that day), 
    # the number of schools with confirmed cases for that day is incremented
    #
    # After the number of schools closed and the number of schools with confirmed cases for a day have been found,
    # the information for that day is appended to the finalExtractedData array to be printed later on
    for row in schoolCovidSummaryReader:
        if ((row[0][0].isnumeric()) == True):
            data = []
            totalConfirmedCases = 0        

            data.append(row[COVID_SUMMARY_INDEX_MAP["Reported_Date"]])
            data.append(row[COVID_SUMMARY_INDEX_MAP["Current_Schools_Closed"]])

            while (stringRow < numOfLines and activeSchoolCovidExtractedData[stringRow][0] == row[COVID_SUMMARY_INDEX_MAP["Reported_Date"]]):
                totalConfirmedCases += int (activeSchoolCovidExtractedData[stringRow][1])
                stringRow += 1
                
            data.append(totalConfirmedCases)

            finalExtractedData.append(data)

    # Prints out the extracted information needed for the graph visualization to the output specified in the command line
    # This information is read from the finalExtractedData array     
    print ("Date,State Of School,Number Of Schools")
    
    for row in finalExtractedData:
        print ("{0},Schools With Confirmed Cases,{1}".format(row[0], row[2]))
        print ("{0},Schools Closed,{1}".format(row[0], row[1]))


##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#