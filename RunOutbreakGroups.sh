#!/bin/bash

echo

echo "Please enter a PHU ID"
read phuId

echo "Reading data from ongoing_outbreaks_phu file..."

python OutbreakGroups/extract_outbreak_group_data.py data/ongoing_outbreaks_phu.csv $phuId > OutbreakGroups/extracted_outbreak_groups_data.csv
echo

echo "CSV file generated that contains the data needed to create the graph"

echo
echo "Creating graph visualization for PHU #"$phuId"..."

echo
python OutbreakGroups/graph_outbreak_groups.py OutbreakGroups/extracted_outbreak_groups_data.csv OutbreakGroups/outbreak_group_visualization.pdf
echo

echo "Done!"
echo