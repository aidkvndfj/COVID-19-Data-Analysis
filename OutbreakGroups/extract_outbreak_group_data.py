#!/usr/bin/env python

'''
extract_school_data.py
  Author(s): Ikeoluwa Agbaje (1125093)
  Previous Author(s): Andrew Hamilton-Wright

  Project: COVID-19 in Ontario
  Date of Last Update: April 01, 2021

  Functional Summary
    extract_school_data.py will extract the relevant information needed to creat graphs
    and put it in a CSV file

  Commandline Parameters: 2
    argv[1] = ongoingoutbreaksphu file
    argv[2] = PHU ID

  Running:
    OutbreakGroups/extract_outbreak_group_data.py data/ongoing_outbreaks_phu.csv <phuId> > OutbreakGroups/extracted_outbreak_groups_data.csv
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
#
# Index map for the ongoing outbreaks phu file 
OUTBREAKS_BY_PHU_INDEX_MAP = {
        "Date" :  0,
        "PHU_Name" :  1,
        "PHU_ID" :  2,
        "Outbreak_Group" :  3,
        "Num_Of_Ongoing_Outbreaks" :  4 }

# Main function
def main(argv):
    
    '''
    Load a data file and print out the columns matching the selected
    indices
    '''

    #
    #   Check that we have been given the right number of parameters (3),
    #   and store the command line arguments in appropriate variables
    #
    if len(argv) != 3:
        print("Usage: OutbreakGroups/extract_outbreak_group_data.py <ongoingoutbreaksphu file> <PHU_id>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    # Saves the file name given from the command-line in an appropriate variable
    ongoingOutbreaksPhuFile = argv[1]

    #
    # Attempts to open the file using a utf-8-sig encoding 
    # and exits with a non-zero value if there is an error opening the file after printing an error message
    #
    try:
        ongoingOutbreaksPhuFh = open(ongoingOutbreaksPhuFile, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                ongoingOutbreaksPhuFile, err), file=sys.stderr)
        sys.exit(1)


    # Reads the opened csv file and stores it in a corresponding variable
    ongoingOutbreaksPhuReader = csv.reader(ongoingOutbreaksPhuFh)


    #
    # Variable Declarations
    #
    # Variable to hold the PHU ID given as an input from the command line
    # The extracted csv file and the graph visualization created will be based on this PHU ID
    phuId = argv[2]

    # Integers to hold the total number of ongoing outbreaks in each outbreak group overtime for the given PHU
    totalCongregateCare = 0
    totalCongregateLiving = 0
    totalEducation = 0
    totalWorkplace = 0
    totalRecreational = 0
    totalOtherOrUnknown = 0

    # Integers to hold the number of days there is an ongoing outbreak in each outbreak group overtime for the given PHU
    # The total number of ongoing outbreaks will be divided by this number to get the average number of ongoing outbreaks per day
    numberCongregateCare = 0
    numberCongregateLiving = 0
    numberEducation = 0
    numberWorkplace = 0
    numberRecreational = 0
    numberOtherOrUnknown = 0

    # Integers to hold the average number of ongoing outbreaks in each outbreak group overtime for the given PHU
    averageCongregateCare = 0
    averageCongregateLiving = 0
    averageEducation = 0
    averageWorkplace = 0
    averageRecreational = 0
    averageOtherOrUnknown = 0
    
    # Loop that goes through the ongoing outbreaks phu file to extract the necessary information
    # When a row corresponding to the given PHU ID is found, the if-else statements are executed based on what the outbreak group of that row is
    # The number of ongoing outbreaks for that day is added to the total number of ongoing outbreaks for that outbreak group
    #
    # If statement used to ignore the first line from the file since it does not contain any actual data
    for row in ongoingOutbreaksPhuReader:
        if ((row[0][0].isnumeric()) == True):
            if (row[OUTBREAKS_BY_PHU_INDEX_MAP["PHU_ID"]] == phuId):

                if (row[OUTBREAKS_BY_PHU_INDEX_MAP["Outbreak_Group"]] == "1 Congregate Care"):
                    totalCongregateCare += int (row[OUTBREAKS_BY_PHU_INDEX_MAP["Num_Of_Ongoing_Outbreaks"]])
                    numberCongregateCare += 1

                elif (row[OUTBREAKS_BY_PHU_INDEX_MAP["Outbreak_Group"]] == "2 Congregate Living"):
                    totalCongregateLiving += int (row[OUTBREAKS_BY_PHU_INDEX_MAP["Num_Of_Ongoing_Outbreaks"]])
                    numberCongregateLiving += 1

                elif (row[OUTBREAKS_BY_PHU_INDEX_MAP["Outbreak_Group"]] == "3 Education"):
                    totalEducation += int (row[OUTBREAKS_BY_PHU_INDEX_MAP["Num_Of_Ongoing_Outbreaks"]])
                    numberEducation += 1

                elif (row[OUTBREAKS_BY_PHU_INDEX_MAP["Outbreak_Group"]] == "4 Workplace"):
                    totalWorkplace += int (row[OUTBREAKS_BY_PHU_INDEX_MAP["Num_Of_Ongoing_Outbreaks"]])
                    numberWorkplace += 1

                elif (row[OUTBREAKS_BY_PHU_INDEX_MAP["Outbreak_Group"]] == "5 Recreational"):
                    totalRecreational += int (row[OUTBREAKS_BY_PHU_INDEX_MAP["Num_Of_Ongoing_Outbreaks"]])
                    numberRecreational += 1

                elif (row[OUTBREAKS_BY_PHU_INDEX_MAP["Outbreak_Group"]] == "6 Other/Unknown"):
                    totalOtherOrUnknown += int (row[OUTBREAKS_BY_PHU_INDEX_MAP["Num_Of_Ongoing_Outbreaks"]])
                    numberOtherOrUnknown += 1

    # For the given PHU, if the total number of ongoing outbreaks for EVERY outbreak group is 0,
    # that means there is no record of an outbreak in that PHU. This could either mean that the PHU has no recorded outbreaks,
    # or that the PHU simply does not exist. It is not obvious from the file which of these options is the case, so an error
    # message is printed to the user with both options so they are aware of the possible causes of this problem.
    if ((totalCongregateCare == 0) and (totalCongregateLiving == 0) and (totalEducation == 0) and (totalWorkplace == 0) and (totalRecreational == 0) and (totalOtherOrUnknown == 0)):
        print ("You either entered an invalid PHU ID or this PHU has no recorded outbreaks. Data could not be generated")
        sys.exit(1)

    # For the given PHU, if the number of ongoing outbreaks for ANY outbreak group is 0, that means that there
    # is no recorded outbreak for that specific outbreak group, but there have been outbreaks in this PHU from a diffrent outbreak group
    # The average number of ongoing outbreaks for that group is given a value of 0, 
    # so that the program does not attempt to divide by 0 when trying to find the average
    if (numberCongregateCare == 0):
        averageCongregateCare = 0
    else:
        averageCongregateCare = totalCongregateCare / numberCongregateCare

    if (numberCongregateLiving == 0):
        averageCongregateLiving = 0
    else:
        averageCongregateLiving = totalCongregateLiving / numberCongregateLiving

    if (numberEducation == 0):
        averageEducation = 0
    else:
        averageEducation = totalEducation / numberEducation

    if (numberWorkplace == 0):
        averageWorkplace = 0
    else:
        averageWorkplace = totalWorkplace / numberWorkplace

    if (numberRecreational == 0):
        averageRecreational = 0
    else:
        averageRecreational = totalRecreational / numberRecreational

    if (numberOtherOrUnknown == 0):
        averageOtherOrUnknown = 0
    else:
        averageOtherOrUnknown = totalOtherOrUnknown / numberOtherOrUnknown

    # Prints out the extracted information to the output specified in the command line       
    print ("Outbreak Group,Average Number Of Ongoing Outbreaks")    
    
    print ("Congregate Care,{:.2f}".format(averageCongregateCare))
    print ("Congregate Living,{:.2f}".format(averageCongregateLiving))
    print ("Education,{:.2f}".format(averageEducation))
    print ("Workplace,{:.2f}".format(averageWorkplace))
    print ("Recreational,{:.2f}".format(averageRecreational))
    print ("Other/Unknown,{:.2f}".format(averageOtherOrUnknown))


##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#