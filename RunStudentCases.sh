#!/bin/bash

cd StudentCasesByCity

echo Generating City Names...

python ActiveSchoolCases/extractCityNames.py ActiveSchoolCases/covidData/schoolsactivecovid.csv > ActiveSchoolCases/progData/cityNames.txt

echo "Generating the number of cases for the provided cities"

python ActiveSchoolCases/extractConfirmedStudentCases.py ActiveSchoolCases/covidData/schoolsactivecovid.csv Ajax Brampton Ottawa Mississauga > ActiveSchoolCases/progData/studentCasesPerCity.txt

echo "Plotting the graph" 

python plotSchoolCases.py ActiveSchoolCases/progData/studentCasesPerCity.txt cityGraphs/graphOne.pdf