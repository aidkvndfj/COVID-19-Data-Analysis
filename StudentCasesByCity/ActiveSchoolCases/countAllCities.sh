#!/bin/bash
# Use this script to get the number of cases throughout each valid city in Ontario

echo "Counting all cities"

python helperScripts/getAllCounts.py progData/cityNames.txt covidData/schoolsactivecovid.csv > progData/test1.txt