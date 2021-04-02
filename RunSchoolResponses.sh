#!/bin/bash

echo
echo Reading data from schoolcovidsummary.csv file and schoolsactivecovid.csv file...

python SchoolResponse/extract_school_data.py data/schoolcovidsummary.csv data/schoolsactivecovid.csv > SchoolResponse/extracted_school_data.csv
echo

echo CSV file generated that contains the data needed to create the graph

echo
echo Creating graph visualization...

echo
python SchoolResponse/graph_school_data.py SchoolResponse/extracted_school_data.csv SchoolResponse/school_data_visualization.pdf
echo

echo Done!
echo