'''
    ResponseFrameworkDataExtractor.py
    Author(s): Ryan Grace (1103232)
    Previous Author(s): Andrew Hamilton-Wright, Eric Morse (1141504), Ikeoluwa Agbaje (1125093), Jason Kyle Tan (1134487)

    Project: Team Group Porject
    Date of Last Update: April 1, 2021.

    Functional Summary

    Create a script to compare data from both sets:
      Reporting_PHU_id
      Status_PHU
      start_date
      end_date
      
      Reported_Date
      Case_Total
      PHU_ID

      PHU_id
      Name

      It will export it to a csv file used for graphing
        
    To Run:
    python RegionResponse/CompareData.py 
'''
#import proper libraries
import sys
import csv
import io
import datetime
import array as arr

#create a index map
INDEX_MAP = {
    "Reporting_PHU_id" :  0,
    "Status_PHU" :  1,
    "start_date" :  2,
    "end_date" :  3}

INDEX_MAP2 = {
    "Reported_Date" : 0,
    "Case_Total" : 1,
    "PHU_ID" : 2,
}

INDEX_MAP3 = {
    "PHU_id" : 0,
    "Name" : 1,
}

phuIds = arr.array('i', [2262, 2268, 2261])

#create file names
PHU1RegionData = "RegionResponse/PHU1RegionData.csv"
PHU1CaseRegionData = "RegionResponse/PHU1CaseRegionData.csv"
PHU2RegionData = "RegionResponse/PHU2RegionData.csv"
PHU2CaseRegionData = "RegionResponse/PHU2CaseRegionData.csv"
PHU3RegionData = "RegionResponse/PHU3RegionData.csv"
PHU3CaseRegionData = "RegionResponse/PHU3CaseRegionData.csv"
PHUNames = "RegionResponse/PHUNames.csv"

# Make sure file opens without issues

OutputForGraphFileName = "RegionResponse/" + "OutputForGraphData" + ".csv"
OutputForGraphFile = io.open(OutputForGraphFileName, "w+", encoding="utf-8")
OutputForGraphFile.write("Status,PHU,Cases,Name\n")  

#Open Files for reading
try:
    PHU2CaseRegionDataFile = open(PHU2CaseRegionData, encoding="utf-8-sig")

except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU2CaseRegionData, err), file=sys.stderr)
    sys.exit(1)

try:
    PHU3CaseRegionDataFile = open(PHU3CaseRegionData, encoding="utf-8-sig")

except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU3CaseRegionData, err), file=sys.stderr)
    sys.exit(1)

try:
    PHU1RegionDataFile = open(PHU1RegionData, encoding="utf-8-sig")

except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU1RegionData, err), file=sys.stderr)
    sys.exit(1)

try:
    PHU2RegionDataFile = open(PHU2RegionData, encoding="utf-8-sig")

except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU2RegionData, err), file=sys.stderr)
    sys.exit(1)
    
try:
    PHU3RegionDataFile = open(PHU3RegionData, encoding="utf-8-sig")

except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU3RegionData, err), file=sys.stderr)
    sys.exit(1)

#set counters for headers of csv files
counter = 0
counter2 = 0
#create file readers for loop through csv files
PHU1RegionDataReader = csv.reader(PHU1RegionDataFile)
PHU2RegionDataReader = csv.reader(PHU2RegionDataFile)
PHU3RegionDataReader = csv.reader(PHU3RegionDataFile)
PHU2CaseDataReader = csv.reader(PHU2CaseRegionDataFile)
PHU3CaseDataReader = csv.reader(PHU3CaseRegionDataFile)
totalCasesPHU1 = arr.array('i', [0, 0, 0, 0, 0, 0])
totalCasesPHU2 = arr.array('i', [0, 0, 0, 0, 0, 0])
totalCasesPHU3 = arr.array('i', [0, 0, 0, 0, 0, 0])
#array for loop
currentStatus = ["Protect", "Prevent", "Shutdown", "Control", "Restrict", "Lockdown"]
#comparing data for PHU1 by looking at the reported date and seeing if its between the start and end date for status
for regionRow in PHU1RegionDataReader:
  if (counter == 0):
      counter = counter + 1
      continue
  #Set start and end date as variables used to compare
  start = datetime.datetime.strptime(regionRow[INDEX_MAP["start_date"]], "%Y-%m-%d")
  end = datetime.datetime.strptime(regionRow[INDEX_MAP["end_date"]], "%Y-%m-%d")
  #open case file for phu1
  try:
    PHU1CaseRegionDataFile = open(PHU1CaseRegionData, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU1CaseRegionData, err), file=sys.stderr)
    sys.exit(1)
  #create file reader
  PHU1CaseDataReader = csv.reader(PHU1CaseRegionDataFile)
  counter2 = 0
  #Looping through cases file
  for caseRow in PHU1CaseDataReader:
    if (counter2 == 0):
      counter2 = counter2 + 1
      continue
    #set date for specific case
    currentDate = datetime.datetime.strptime(caseRow[INDEX_MAP2["Reported_Date"]], "%Y-%m-%d")
    #Check if date is between start and end date
    if (start <= currentDate <= end):
      for x in range(0,6):
        convertedStatus = str(regionRow[INDEX_MAP["Status_PHU"]])
        if (regionRow[INDEX_MAP["Status_PHU"]] == currentStatus[x]):
          #fill total case array
          totalCasesPHU1[x] = totalCasesPHU1[x] + int(caseRow[INDEX_MAP2["Case_Total"]])
  PHU1CaseRegionDataFile.close()

#comparing data for PHU2 by looking at the reported date and seeing if its between the start and end date for status
counter = 0
for regionRow in PHU2RegionDataReader:
  if (counter == 0):
      counter = counter + 1
      continue
  #Set start and end date as variables used to compare
  start = datetime.datetime.strptime(regionRow[INDEX_MAP["start_date"]], "%Y-%m-%d")
  end = datetime.datetime.strptime(regionRow[INDEX_MAP["end_date"]], "%Y-%m-%d")
  #open case file for phu2
  try:
    PHU2CaseRegionDataFile = open(PHU2CaseRegionData, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU2CaseRegionData, err), file=sys.stderr)
    sys.exit(1)
  #create file reader
  PHU2CaseDataReader = csv.reader(PHU2CaseRegionDataFile)
  counter2 = 0
  #Looping through cases file
  for caseRow in PHU2CaseDataReader:
    if (counter2 == 0):
      counter2 = counter2 + 1
      continue
    #set date for specific case
    currentDate = datetime.datetime.strptime(caseRow[INDEX_MAP2["Reported_Date"]], "%Y-%m-%d")
    #Check if date is between start and end date
    if (start <= currentDate <= end):
      for x in range(0,6):
        convertedStatus = str(regionRow[INDEX_MAP["Status_PHU"]])
        if (regionRow[INDEX_MAP["Status_PHU"]] == currentStatus[x]):
          totalCasesPHU2[x] = totalCasesPHU2[x] + int(caseRow[INDEX_MAP2["Case_Total"]])
  PHU2CaseRegionDataFile.close()

counter = 0
#comparing data for PHU3 by looking at the reported date and seeing if its between the start and end date for status
for regionRow in PHU3RegionDataReader:
  if (counter == 0):
      counter = counter + 1
      continue
  #Set start and end date as variables used to compare
  start = datetime.datetime.strptime(regionRow[INDEX_MAP["start_date"]], "%Y-%m-%d")
  end = datetime.datetime.strptime(regionRow[INDEX_MAP["end_date"]], "%Y-%m-%d")
  #open case file for phu2
  try:
    PHU3CaseRegionDataFile = open(PHU3CaseRegionData, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHU2CaseRegionData, err), file=sys.stderr)
    sys.exit(1)
  #create file reader for PHU 3
  PHU3CaseDataReader = csv.reader(PHU3CaseRegionDataFile)
  counter2 = 0
  #Looping through cases file
  for caseRow in PHU3CaseDataReader:
    if (counter2 == 0):
      counter2 = counter2 + 1
      continue
    #set date for specific case
    currentDate = datetime.datetime.strptime(caseRow[INDEX_MAP2["Reported_Date"]], "%Y-%m-%d")
    #Check if date is between start and end date
    if (start <= currentDate <= end):
      for x in range(0,6):
        convertedStatus = str(regionRow[INDEX_MAP["Status_PHU"]])
        if (regionRow[INDEX_MAP["Status_PHU"]] == currentStatus[x]):
          totalCasesPHU3[x] = totalCasesPHU3[x] + int(caseRow[INDEX_MAP2["Case_Total"]])
  PHU3CaseRegionDataFile.close()

#Writing all compared data to csv file used to graph
#WRTIE FOR PHU1
for y in range(0, 6):
  try:
    PHUNamesFile = open(PHUNames, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHUNames, err), file=sys.stderr)
    sys.exit(1)
  counter = 0
  PHUNamesDataReader = csv.reader(PHUNamesFile)
  for nameRow in PHUNamesDataReader:
    if (counter == 0):
      counter = counter + 1
      continue
    #check if correct phu id
    if (phuIds[0] == int(nameRow[INDEX_MAP3["PHU_id"]])):
      currentName = str(nameRow[INDEX_MAP3["Name"]])
  PHUNamesFile.close()
  OutputForGraphFile.write(str(currentStatus[y]) + "," + str(phuIds[0]) + "," + str(totalCasesPHU1[y]) + "," + currentName + "\n")
#WRTIE FOR PHU2
for h in range(0, 6):
  try:
    PHUNamesFile = open(PHUNames, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHUNames, err), file=sys.stderr)
    sys.exit(1)
  counter = 0
  PHUNamesDataReader = csv.reader(PHUNamesFile)
  for nameRow in PHUNamesDataReader:
    if (counter == 0):
      counter = counter + 1
      continue
    #check if correct phu id
    if (phuIds[1] == int(nameRow[INDEX_MAP3["PHU_id"]])):
      currentName = str(nameRow[INDEX_MAP3["Name"]])
  PHUNamesFile.close()
  OutputForGraphFile.write(str(currentStatus[h]) + "," + str(phuIds[1]) + "," + str(totalCasesPHU2[h]) + "," + currentName + "\n")
#WRTIE FOR PHU3
for t in range(0, 6):
  try:
    PHUNamesFile = open(PHUNames, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open file '{}' : {}".format(
            PHUNames, err), file=sys.stderr)
    sys.exit(1)
  counter = 0
  PHUNamesDataReader = csv.reader(PHUNamesFile)
  for nameRow in PHUNamesDataReader:
    if (counter == 0):
      counter = counter + 1
      continue
    #check if correct phu id
    if (phuIds[2] == int(nameRow[INDEX_MAP3["PHU_id"]])):
      currentName = str(nameRow[INDEX_MAP3["Name"]])
  PHUNamesFile.close()
  OutputForGraphFile.write(str(currentStatus[t]) + "," + str(phuIds[2]) + "," + str(totalCasesPHU3[t]) + "," + currentName + "\n")

#
# End of script
#