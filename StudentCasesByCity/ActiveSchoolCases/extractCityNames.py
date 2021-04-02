'''
extractCityNames.py
  Author(s): Jason Kyle Tan (1134487)

  Project: Team Group Project
  Date of Last Update: March 29, 2021

  Functional Summary
    This program extracts city names from the Schools with Active COVID-19 Cases
    dataset. It is recommended that the output be directed into a file for future
    usage.

     Commandline Parameters: 1
        argv[1] = schoolsactivecovid.csv (data file)

  Command to run: python extractConfirmedStudentCases.py schoolsactivecovid.csv <cityName>
    (Optional to save data to file):
                  python extractCityNames.py schoolsactivecovid.csv > (filename).txt
    Accepted formats also include: .csv
'''

from helperScripts.schoolsIndexMap import INDEX_MAP
import sys
import csv

def main(argv):
    # Get the file name from the command-line
    filename = argv[1]

    # Attempt to open the file
    try:
        fh = open(filename, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(filename, err),
              file=sys.stderr)
        sys.exit(1)

    # Create a list to hold all the names of cities
    cities = []

    # Iterate over every row in the file, skipping the first row
    next(fh)
    data_reader = csv.reader(fh)
    for row in data_reader:
        #
        # Only accept cities that contain alphanumeric characters, this effectively
        # means we are losing out on some cities, but it's done to better narrow down the
        # choices that the user has. Also, it prevents inconsistences found in the data with
        # random characters in municipalities and such.
        #
        currentCity = row[INDEX_MAP["MUNICIPALITY"]]
        if not currentCity.isalnum():
            continue
        
        # Check if the cities list is empty (this is only true once)
        if not cities:
            # Append the first city
            cities.append(currentCity)
            continue
        
        # Check if the currently indexed city exists and is in the cities list
        if currentCity not in cities and currentCity:
            # Append the currently indexed city
            cities.append(currentCity)
            continue

    # Iterate over every city in the cities list and sort it by alphabetical order
    cities.sort()
    print("City")
    for city in cities:
        print(city)

main(sys.argv)