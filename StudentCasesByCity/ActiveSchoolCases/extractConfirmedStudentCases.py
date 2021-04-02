'''
extractConfirmedStudentCases.py
  Author(s): Jason Kyle Tan (1134487)

  Project: Team Group Project
  Date of Last Update: March 21, 2021

  Functional Summary
    This program takes any number of cities, assuming they're valid and directly from
    the program that generates them (extractCityNames.py), and counts the number of
    confirmed student cases within each of them. As a result, the program outputs the total number of student cases in each city.

     Commandline Parameters: 2+
        argv[1] = schoolsactivecovid.csv (data file)
        argv[2] = City (1) (please refer to the schoolNames.csv file)
        argv[3] = City (2)
        .
        . .
        . . .
        . . . .
        . . . . .
        argv[x] = City (x) (for an arbitrary number and names of cities)

  Command to run: python extractConfirmedStudentCases.py schoolsactivecovid.csv <cityName>
    (Optional to save data to file):
                  python extractConfirmedStudentCases.py schoolsactivecovid.csv <cityName> > (filename).txt
    Note: <cityName> refers to the names of cities separated by spaces
          If the user has no (filename) to save to, they are recommended to save it to
          a file named studentCasesPerCity.txt to follow the consistency and flow of the
          program.
    Accepted formats also include: .csv
'''

from helperScripts.schoolsIndexMap import INDEX_MAP
import sys
import csv

def main(argv):
    # Check for proper usage since we must always compare more than
    # two cities at a given time
    if not len(argv) > 3:
        print("Usage: python extractConfirmedStudentCases.py (datafile) <cityNames> > (filename).txt")
        sys.exit(1)

    # Assign the required variables to access the file of interest,
    # alongside the school ID to find data for
    filename = argv[1]

    #
    # Here we're creating a list to hold each of the valid cities from
    # schoolNames.csv that the user has inputted
    #
    citiesToFind = []

    # Iterate through each item in the command-line arguments, excluding
    # the first two, those being the file and this python file
    for i in range(len(argv)):
        #
        # Since we know that the users inputted cities occur after the file and python file,
        # we're filling it into a list of cities and assuming that the user entered values are valid
        #
        if i > 1:
            citiesToFind.append(argv[i])
            
    # Attempt to open the file
    try:
        fh = open(filename, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(filename, err),
              file=sys.stderr)
        sys.exit(1)


    # Create a list that holds the rows of data that are of interest to us
    # so that we can parse and access the data later on
    studentCasesOfInterest = []

    # Create a data reader to read into the file
    data_reader = csv.reader(fh)

    # Iterate over each row in the file
    for row in data_reader:
        # Check to see if the rows city is any one of the cities
        # required to find
        if row[INDEX_MAP["MUNICIPALITY"]]in citiesToFind:
            #
            # Here we only want to append the city
            # and the confirmed number of student cases. To do that, we'll
            # create a small dictionary with that information unique to each case
            #
            currentCase = {}
            currentCase["city"] = row[INDEX_MAP["MUNICIPALITY"]]
            currentCase["studentsInfected"] = row[INDEX_MAP["CONFIRMED_STUDENT_CASES"]]

            # Afterwards we want to append that smaller list to the bigger 
            # studentCasesOfInterest one
            studentCasesOfInterest.append(currentCase)

    # Sort the list by cities to prepare for output
    studentCasesOfInterest = sorted(studentCasesOfInterest, key=lambda case: case["city"])

    # Create a list that holds dictionaries of the city alongside it's number of counts
    casesCountPerCity = []

    # Here we're iterating over each city in the city list to go over each of their counts
    for city in citiesToFind:
        #
        # Create two containers, one is an integer variable that holds the number of cases in a city,
        # while the second one is a dictionary that will hold onto the number of cases alongside it's city name
        #
        numOfCases = 0
        cityInfo = {}
            
        # Iterate over every case of interest
        for case in studentCasesOfInterest:
            # Check if the case has the same name as the currently indexed city
            if case["city"] == city:
                # Add to the total number of cases if the above condition is true
                numOfCases += int(case["studentsInfected"])
        
        # Append the number of cases along with its city inside a dictionary
        cityInfo["city"] = city
        cityInfo["cases"] = numOfCases

        # Append the dictionary from earlier into the list that contains the information for each city
        # and it's relevant counts
        casesCountPerCity.append(cityInfo)
    
    # Print out the information retrieved and counted from earlier
    print("City,ConfirmedNumberOfCases")
    for caseInfo in casesCountPerCity:
        print(f"{caseInfo['city']},{caseInfo['cases']}")



main(sys.argv)