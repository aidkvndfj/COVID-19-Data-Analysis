#!/usr/bin/env python
'''
getAllCounts.py
  Author(s): Jason Kyle Tan (1134487)

  Project: Team Group Project
  Date of Last Update: March 29, 2021

  Functional Summary
    This program gets all the number of cases for each
    city, provided that the required files are located
    in their specified directories. It is recommended that the
    program output be stored in a file for future usage.

     Commandline Parameters: 2
        argv[1] = cityNames.txt (city names)
        argv[2] = schoolsactivecovid.csv (data file)

  Command to run: python getAllCounts.py <cityFile> <dataFile>
    <cityFile> = cityNames.txt
    <dataFile> = schoolsactivecovid.csv
    
    Also refer to the bash script: countAllCities.sh
        After making it an executable running in terminal: chmod +x countAllCities.sh
        Run it using ./countAllCities.sh

    (Optional to save data to file):
                  python getAllCounts.py > (filename).txt
    Accepted formats also include: .csv
'''

from schoolsIndexMap import INDEX_MAP
import re
import sys
import csv

#
# This function takes a city (string) and list of COVID-19 cases
# as parameters respectively, counting the number of cases within that city
#
def countCity(city, caseList):
    count = 0
    for case in caseList:
        if city in case["city"]:
            count += int(case["count"])
    return count


def main(argv):
    # Check for proper usage
    if len(argv) != 3:
        print("Usage: python getAllCounts.py <cityFile> <dataFile> ")
        sys.exit(1)
    # Assuming that these files exist and are valid, open the city names file along with
    # the cases file
    cityData = open(argv[1], encoding="utf-8-sig")
    caseData = open(argv[2], encoding="utf-8-sig")

    # Prepare to read data from the case data
    data = csv.reader(caseData)

    # Read the city names file into a list
    cities = []
    with cityData as reader:
        reader.readline()
        for line in reader.readlines():
            line = re.sub(r"[^a-zA-Z0-9]", "", line)
            cities.append(line)

    # Read each case into a dictionary, appending it to a list of dictionaries
    cases = []
    for row in data:
        case = {}
        case["city"] = row[INDEX_MAP["MUNICIPALITY"]]
        case["count"] = row[INDEX_MAP["CONFIRMED_STUDENT_CASES"]]
        cases.append(case)


    counts = []
    # Count the number of cases in each city using a list filled with dictionaries of city information
    for city in cities:
        case = {}
        case["city"] = city
        case["count"] = countCity(city, cases)
        counts.append(case)

    counts.sort(key=lambda x: x['city']) # Sorts the cases by city name
    # Uncomment the line under to sort by alphabet instead of student cases, commenting the line above this
    # counts.sort(key=lambda x: x['count'], reverse=True)

    print("City,ConfirmedNumberOfCases")
    for count in counts:
        print(f"{count['city']},{count['count']}")


    
main(sys.argv)
