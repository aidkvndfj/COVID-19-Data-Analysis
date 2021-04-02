'''
    ResponseFrameworkDataExtractor.py
    Author(s): Ryan Grace (1103232)
    Previous Author(s): Andrew Hamilton-Wright, Eric Morse (1141504), Ikeoluwa Agbaje (1125093), Jason Kyle Tan (1134487)

    Project: Team Group Porject
    Date of Last Update: April 1, 2021.

    Functional Summary

    Create a script for extracting data:

        ResponseFrameWorkDataExtractor is a script that will take the data
        from https://data.ontario.ca/dataset/ontario-covid-19-zones
        and condense it into 3 readable csv file for CompareData to compare it to the total cases
        It also creates a PHUNames csv file so the names of the regions will be on the graph

    Data to Extract:

        Reporting_PHU
        Reporting_PHU_id
        Satus_PHU
        start_date
        end_date
    
        from the [response framework](https://data.ontario.ca/dataset/ontario-covid-19-zones) so it becomes possible to compare case numbers of four different safety measures. 
        
    To Run:
    python RegionResponse/ResponseFrameworkDataExtractor.py
'''
#import proper libraries
import sys
import csv
import io
import array as arr
#create a index map
INDEX_MAP = {
    "Reporting_PHU" :  0,
    "Reporting_PHU_id" :  1,
    "Satus_PHU" :  2,
    "start_date" :  3,
    "end_date" :  4,
    "PHU_url" :  5}
#Set PHU IDs
phuIds = arr.array('i', [2262, 2268, 2261])
#set filename
fileName = "data/response_framework.csv"
# Make sure file opens without issues
try:
    fh = open(fileName, encoding="utf-8-sig")
#if file does not open
except IOError as err:
    print("Unable to open file '{}' : {}".format(
            fileName, err), file=sys.stderr)
    sys.exit(1)
#create data reader to read the file
dataReader = csv.reader(fh)
counter = 0
phuData = []
#Create 3 checks used gather PHU Names
phu1NameCheck = 0
phu2NameCheck = 0
phu3NameCheck = 0
#Create file name for region 1 & csv file
PHU1RegionDataFileName = "RegionResponse/" + "PHU1RegionData" + ".csv"
PHU1RegionDataFile = io.open(PHU1RegionDataFileName, "w+", encoding="utf-8")
PHU1RegionDataFile.write("Reporting_PHU_id,Status_PHU,start_date,end_date\n")
#Create file name for region 2 & csv file
PHU2RegionDataFileName = "RegionResponse/" + "PHU2RegionData" + ".csv"
PHU2RegionDataFile = io.open(PHU2RegionDataFileName, "w+", encoding="utf-8")
PHU2RegionDataFile.write("Reporting_PHU_id,Status_PHU,start_date,end_date\n")
#Create file name for region 3 & csv file
PHU3RegionDataFileName = "RegionResponse/" + "PHU3RegionData" + ".csv"
PHU3RegionDataFile = io.open(PHU3RegionDataFileName, "w+", encoding="utf-8")
PHU3RegionDataFile.write("Reporting_PHU_id,Status_PHU,start_date,end_date\n")
#Create file name for PHUNames & csv file
PHUNamesFileName = "RegionResponse/" + "PHUNames" + ".csv"
PHUNamesFile = io.open(PHUNamesFileName, "w+", encoding="utf-8")
PHUNamesFile.write("PHU_id,Name\n")
#Extracting the data from the file
for row in dataReader:
    #Skip first row of csv file (because its a header)
    if (counter == 0):
      counter = counter + 1
      continue
    data = []
    #Check if PHU ID from the file is the first PHU ID. If so, write first PHU id to file
    if (int(row[INDEX_MAP["Reporting_PHU_id"]]) == phuIds[0]):
      PHU1RegionDataFile.write(row[INDEX_MAP["Reporting_PHU_id"]] + "," + row[INDEX_MAP["Satus_PHU"]] + "," + row[INDEX_MAP["start_date"]][0:10] + "," + row[INDEX_MAP["end_date"]][0:10] + "\n")
    #Check if PHU ID from the file is the second PHU ID. If so, write second PHU id to file
    if (int(row[INDEX_MAP["Reporting_PHU_id"]]) == phuIds[1]):
      PHU2RegionDataFile.write(row[INDEX_MAP["Reporting_PHU_id"]] + "," + row[INDEX_MAP["Satus_PHU"]] + "," + row[INDEX_MAP["start_date"]][0:10] + "," + row[INDEX_MAP["end_date"]][0:10] + "\n")
    #Check if PHU ID from the file is the third PHU ID. If so, write third PHU id to file
    if (int(row[INDEX_MAP["Reporting_PHU_id"]]) == phuIds[2]):
      PHU3RegionDataFile.write(row[INDEX_MAP["Reporting_PHU_id"]] + "," + row[INDEX_MAP["Satus_PHU"]] + "," + row[INDEX_MAP["start_date"]][0:10] + "," + row[INDEX_MAP["end_date"]][0:10] + "\n")
    counter = counter + 1
#Close file
fh.close()
#Open file 
try:
    fh = open(fileName, encoding="utf-8-sig")
#If there is an error
except IOError as err:
    print("Unable to open file '{}' : {}".format(
            fileName, err), file=sys.stderr)
    sys.exit(1)
#set data reader
dataReader = csv.reader(fh)
counter = 0;
for row in dataReader:
    #skip first row
    if (counter == 0):
      counter = counter + 1
      continue
    #check if PHU ids are the same
    if ((int(row[INDEX_MAP["Reporting_PHU_id"]]) == phuIds[0]) and (phu1NameCheck == 0)):
      #Set check to true 
      phu1NameCheck = 1
      PHUNamesFile.write(row[INDEX_MAP["Reporting_PHU_id"]] + "," + row[INDEX_MAP["Reporting_PHU"]] + "\n")
    if ((int(row[INDEX_MAP["Reporting_PHU_id"]]) == phuIds[1]) and (phu2NameCheck == 0)):
      PHUNamesFile.write(row[INDEX_MAP["Reporting_PHU_id"]] + "," + row[INDEX_MAP["Reporting_PHU"]] + "\n")
      phu2NameCheck = 1
    if ((int(row[INDEX_MAP["Reporting_PHU_id"]]) == phuIds[2]) and (phu3NameCheck == 0)):
      PHUNamesFile.write(row[INDEX_MAP["Reporting_PHU_id"]] + "," + row[INDEX_MAP["Reporting_PHU"]] + "\n")
      phu3NameCheck = 1  
fh.close()

#
# End of script
#