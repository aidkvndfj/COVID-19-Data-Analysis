'''
    CasesDataExtractor.py
    Author(s): Ryan Grace (1141504)
    Previous Author(s): Andrew Hamilton-Wright, Ikeoluwa Agbaje (1125093), Jason Kyle Tan (1134487)

    Project: Team Group Porject
    Date of Last Update: April 1, 2021.

    Functional Summary
        CasesDataExtractor.py is a script that will take the data
        from https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario
        and condense it into 3 readable csv files used to be compared with 3 other csv files

        Data to extract:
          Case_Reported_Date
          Reporting_PHU_ID

        And if the PHU Links with the PHUs given then it counts as a case, which is incremented through a counter

    Command to run: python RegionResponse/CasesDataExtractor.py data/conposcovidloc.csv
'''

# Required program imports
import sys
import csv
import io
#create map for index
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
    if (len(argv) != 2):
        print("ERROR: Usage CasesDataExtractor.py <DataFile>")
        # if not exit with code 1
        sys.exit(1) 

    fileName = argv[1]

    PHU1 = str(2262)
    PHU2 = str(2268)
    PHU3 = str(2261)

    # Make sure file opens without issues
    try:
        fh = open(fileName, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                fileName, err), file=sys.stderr)
        sys.exit(1)

    #set data reader
    dataReader = csv.reader(fh)

    covidCases = []

    PHU1TotalCases = 0
    PHU2TotalCases = 0
    PHU3TotalCases = 0

    #create files to export data into (PHU1)
    PHU1CaseRegionDataFileName = "RegionResponse/" + "PHU1CaseRegionData" + ".csv"
    PHU1CaseRegionDataFile = io.open(PHU1CaseRegionDataFileName, "w+", encoding="utf-8")
    PHU1CaseRegionDataFile.write("Reported_Date,Case_Total,PHU_ID\n")    
    #create files to export data into (PHU2)    
    PHU2CaseRegionDataFileName = "RegionResponse/" + "PHU2CaseRegionData" + ".csv"
    PHU2CaseRegionDataFile = io.open(PHU2CaseRegionDataFileName, "w+", encoding="utf-8")
    PHU2CaseRegionDataFile.write("Reported_Date,Case_Total,PHU_ID\n")
    #create files to export data into (PHU3)
    PHU3CaseRegionDataFileName = "RegionResponse/" + "PHU3CaseRegionData" + ".csv"
    PHU3CaseRegionDataFile = io.open(PHU3CaseRegionDataFileName, "w+", encoding="utf-8")
    PHU3CaseRegionDataFile.write("Reported_Date,Case_Total,PHU_ID\n")

    for row in dataReader:
        data = []
        if (row[INDEX_MAP["Reporting_PHU_ID"]] == PHU1 or row[INDEX_MAP["Reporting_PHU_ID"]] == PHU2 or row[INDEX_MAP["Reporting_PHU_ID"]] == PHU3):

            data.append(row[INDEX_MAP["Case_Reported_Date"]])
            data.append(row[INDEX_MAP["Client_Gender"]])
            data.append(row[INDEX_MAP["Reporting_PHU_ID"]])
            
            covidCases.append(data)
    
    covidCases.sort()

    lastDate = covidCases[0][0]
    for currCase in covidCases:
        if(currCase[0] != lastDate):
            PHU1CaseRegionDataFile.write(str(lastDate) + "," + str(PHU1TotalCases) + "," + str(PHU1) + "\n")
            PHU2CaseRegionDataFile.write(str(lastDate) + "," + str(PHU2TotalCases) + "," + str(PHU2) + "\n")
            PHU3CaseRegionDataFile.write(str(lastDate) + "," + str(PHU3TotalCases) + "," + str(PHU3) + "\n")
            PHU1TotalCases = 0
            PHU2TotalCases = 0

        if (currCase[2] == PHU1):
            PHU1TotalCases += 1

        elif (currCase[2] == PHU2):
            PHU2TotalCases += 1

        elif (currCase[2] == PHU3):
            PHU3TotalCases += 1

        lastDate = currCase[0]
# END OF: main

main(sys.argv)

#
# End of script
#