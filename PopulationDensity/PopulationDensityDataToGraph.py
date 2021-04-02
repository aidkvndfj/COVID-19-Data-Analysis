'''
    PopulationDensityDataToGraph.py
    Author(s): Eric Morse (1141504)
    Previous Author(s): Jason Kyle Tan (1134487), Andrew Hamilton-Wright, Kassy Raymond

    Project: Team Group Porject
    Date of Last Update: March 18, 2021.

    Functional Summary
        PopulationDensityDataToGraph.py is a script that will take the simplified
        data from PopulationDensityDataExtracotr.py and will plot it on a double y
        axis graph.

        The program will take 2 parameters:
        argv[1] = data file
        argv[2] = graphics file

    Command to run: python PopulationDensityDataToGraph.py PopulationDensityCompressed.csv PopulationDensityGraph.pdf
'''
import sys

# Import the data required to plot the two graphs
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns

def main(argv):
    if (len(argv) != 3):
        print("ERROR: USAGE PopulationDensityDataToGraph.py <Data File> <graphics file>")
        sys.exit(-1)

    dataFilename = argv[1]
    outputFilename = argv[2]

    try:
        dataFrame = pd.read_csv(dataFilename)
    except IOError as err:
        print("Unable to open source file {1}.csv : {0}".format(err, dataFilename), file=sys.stderr)
        sys.exit(-1)

    ## Program Start
    fig = plt.figure()

    ax = sns.lineplot(data=dataFrame, x = "Date", y = "Cases", hue = "Category")
    ax.xaxis.set_major_locator(ticker.MaxNLocator(8))
    plt.xticks(rotation = 45, ha="right")

    fig.savefig(outputFilename, bbox_inches="tight")

# END: main

main(sys.argv)