#!/usr/bin/env python

'''
graph_school_data.py
  Author(s): Ikeoluwa Agbaje (1125093)
  Previous Author(s): Andrew Hamilton-Wright, Kassy Raymond

  Project: COVID-19 in Ontario
  Date of Last Update: April 01, 2021

  Functional Summary
    Creates a graph that shows Ontario schools responses to confirmed 
    COVID cases in their schools

  Commandline Parameters: 2
    sys.argv[0] = name of file to read
    sys.argv[1] = name of graphics file to create

  Running:
    python SchoolResponse/graph_school_data.py SchoolResponse/extracted_school_data.csv SchoolResponse/school_data_visualization.pdf
'''

#
#   Packages and modules
#
import sys

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


# Main Function
def main(argv):

    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters (3),
    #   and store the command line arguments in appropriate variables
    #
    if len(argv) != 3:
        print("Usage:",
                "SchoolResponse/graph_school_data.py <data file> <graphics file>")
        sys.exit(-1)

    # Saves the file names given from the command-line in appropriate string variables
    csv_filename = argv[1]
    graphics_filename = argv[2]


    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    # Exits with a non-zero value if there is an error opening any of the files after printing an error message
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)

    # A this point in the file, we begin to do the plotting

    # We must get the figure before we plot to it, or nothing will show up.
    # The matplotlib "figure" is the data environment that we are drawing
    # our plot into.  The seaborn library will draw onto this figure.
    # We don't see seaborn directly refer to "fig" because it is internally
    # drawing on "the current figure" which is the same one we are
    # referencing on this line.
    fig = plt.figure(figsize=(8,6))


    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    # Chooses 15 major points on the x - axis to show the date so that all the dates are not clumped together and illegible
    # Rotates the x-axis ticks by 45 degrees and gives the graph a title
    axis = sns.lineplot(x = "Date", y = "Number Of Schools", hue = "State Of School", data = csv_df, palette = 'magma')
    axis.xaxis.set_major_locator(ticker.MaxNLocator(15))
    plt.xticks(rotation = 45, ha="right")
    plt.title('School Responses to COVID-19 Outbreaks', fontsize = 13)


    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")

    #
    #  End of Function
    



##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
