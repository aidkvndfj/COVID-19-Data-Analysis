'''
    RegionResponseDataToGraph.py
    Author(s): Ryan Grace (1141504), Eric Morse (1141504)
    Previous Author(s): Jason Kyle Tan (1134487), Andrew Hamilton-Wright, Kassy Raymond

    Project: Team Group Porject
    Date of Last Update: April 1, 2021.

    Functional Summary
        Plot graph from the data exported by compareData.py

    Command to run: python RegionResponse/RegionResponseDataToGraph.py 
'''

import sys

# Import the data required to plot the graph
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns

#plot graph
def main(argv):
    fig = plt.figure()
    OutputForGraph = pd.read_csv('RegionResponse/OutputForGraphData.csv')

    ax = sns.barplot(x = "Status", y = "Cases", hue = "Name", data = OutputForGraph)
    #output graph
    fig.savefig("RegionResponse/Output.pdf", bbox_inches="tight")


main(sys.argv)

#
# End of script
#