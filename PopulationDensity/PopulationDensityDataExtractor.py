'''
    PopulationDensityDataExtrator.py
    Author(s): Eric Morse (1141504)
    Previous Author(s): Andrew Hamilton-Wright, Ikeoluwa Agbaje (1125093), Jason Kyle Tan (1134487), Ryan Grace (1103232)

    Project: Team Group Porject
    Date of Last Update: March 18, 2021.

    Functional Summary
        PopulationDensityDataExtrator.py is a script that will take the data
        from https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario
        and condense it into a readable text file for seaborn to crate a graph with

        The program will take 3 parameters:
        argv[1] = data file
        argv[2] = PHU ID 1
        argv[2] = PHU ID 2

    Command to run: python PopulationDensityDataExtractor.py ../data/conposcovidloc.csv 2253 3895
'''

# Required program imports
import sys
import csv

INDEX_MAP = {
    "Row_ID" :  0,
    "Accurate_Episode_Date" :  1,
    "Case_Reported_Date" :  2,
    "Test_Reported_Date" :  3,
    "Specimen_Date" :  4,
    "Age_Group" :  5,
    "Client_Gender" :  6,
    "Case_AcquisitionInfo" :  7,
    "Outcome1" :  8,
    "Outbreak_Related" :  9,
    "Reporting_PHU_ID" : 10,
    "Reporting_PHU" : 11,
    "Reporting_PHU_Address" : 12,
    "Reporting_PHU_City" : 13,
    "Reporting_PHU_Postal_Code" : 14,
    "Reporting_PHU_Website" : 15,
    "Reporting_PHU_Latitude" : 16,
    "Reporting_PHU_Longitude" : 17 }

def main(argv):
    # check to make sure the correct number of parameters have been given
    if (len(argv) != 4):
        print("ERROR: Usage PopulationDensityDataExtractor.py <DataFile> <PHU1> <PHU2>")
        # if not exit with code 1
        sys.exit(1) 

    fileName = argv[1]
    PHU1 = argv[2]
    PHU2 = argv[3]


    # Make sure file opens without issues
    try:
        fh = open(fileName, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                fileName, err), file=sys.stderr)
        sys.exit(1)


    dataReader = csv.reader(fh)

    # setup lists and other variables.
    covidCases = []

    PHU1FemaleCases = 0
    PHU1MaleCases = 0
    PHU1TotalCases = 0
    PHU2FemaleCases = 0
    PHU2MaleCases = 0
    PHU2TotalCases = 0

    PHU1City = ""
    PHU2City = ""

    outFile = open("PopulationDensityCompressed.csv".format(fileName), "w", encoding="utf-8")

    # extract the relevent cases, aka the ones that have the same PHU as the ones inputted.
    for row in dataReader:
        data = []
        if (row[INDEX_MAP["Reporting_PHU_ID"]] == PHU1 or row[INDEX_MAP["Reporting_PHU_ID"]] == PHU2):
            # record the date, gender, id, and cityname
            data.append(row[INDEX_MAP["Case_Reported_Date"]])
            data.append(row[INDEX_MAP["Client_Gender"]])
            data.append(row[INDEX_MAP["Reporting_PHU_ID"]])
            data.append(row[INDEX_MAP["Reporting_PHU_City"]])
            if (row[INDEX_MAP["Reporting_PHU_ID"]] == PHU1 and PHU1City == ""):
                PHU1City = row[INDEX_MAP["Reporting_PHU_City"]]
            elif (row[INDEX_MAP["Reporting_PHU_ID"]] == PHU2 and PHU2City == ""):
                PHU2City = row[INDEX_MAP["Reporting_PHU_City"]]
            
            covidCases.append(data)
    
    # sort the cases by date
    covidCases.sort()

    lastDate = covidCases[0][0]
    # write header
    outFile.write("Date,Category,Cases\n")
    # loop through relevent cases and count them
    for currCase in covidCases:
        # if the date changes, record the currect cases and other information
        # to the file, then reset the variables
        if(currCase[0] != lastDate):
            outFile.write("{0},FEMALE-{2},{1}\n".format(lastDate, PHU1FemaleCases, PHU1City))
            outFile.write("{0},MALE-{2},{1}\n".format(lastDate, PHU1MaleCases, PHU1City))
            outFile.write("{0},TOTAL-{2},{1}\n".format(lastDate, PHU1TotalCases, PHU1City))
            outFile.write("{0},FEMALE-{2},{1}\n".format(lastDate, PHU2FemaleCases, PHU2City))
            outFile.write("{0},MALE-{2},{1}\n".format(lastDate, PHU2MaleCases, PHU2City))
            outFile.write("{0},TOTAL-{2},{1}\n".format(lastDate, PHU2TotalCases, PHU2City))
            PHU1FemaleCases = 0
            PHU1MaleCases = 0
            PHU1TotalCases = 0
            PHU2FemaleCases = 0
            PHU2MaleCases = 0
            PHU2TotalCases = 0

        # if the PHU matches, then add 1 to total, and the correct gender counter
        if (currCase[2] == PHU1):
            PHU1City = currCase[3]
            if (currCase[1] == "MALE"):
                PHU1TotalCases += 1
                PHU1MaleCases += 1
            
            if (currCase[1] == "FEMALE"):
                PHU1TotalCases += 1
                PHU1FemaleCases += 1
            
            if (currCase[1] == "UNSPECIFIED"):
                PHU1TotalCases += 1
            
            if (currCase[1] == "GENDER DIVERSE"):
                PHU1TotalCases += 1

        # if the PHU matches, then add 1 to total, and the correct gender counter
        elif (currCase[2] == PHU2):
            PHU2City = currCase[3]
            if (currCase[1] == "MALE"):
                PHU2TotalCases += 1
                PHU2MaleCases += 1
            
            if (currCase[1] == "FEMALE"):
                PHU2TotalCases += 1
                PHU2FemaleCases += 1
            
            if (currCase[1] == "UNSPECIFIED"):
                PHU2TotalCases += 1
            
            if (currCase[1] == "GENDER DIVERSE"):
                PHU2TotalCases += 1

        lastDate = currCase[0]

    # close the files
    fh.close()
    outFile.close()
# END OF: main

#
# Call Main passing in system argv as parameter
#
main(sys.argv)

#
# End of script
#