#!/usr/bin/env python

'''
graph_school_data.py
  Author(s): Ikeoluwa Agbaje (1125093)
  Previous Author(s): Andrew Hamilton-Wright, Kassy Raymond

  Project: COVID-19 in Ontario
  Date of Last Update: April 01, 2021

  Functional Summary
    Creates a graph that shows the average number of outbreaks for each outbreak group in a given PHU

  Commandline Parameters: 2
    sys.argv[0] = name of file to read
    sys.argv[1] = name of graphics file to create

  Running:
    python OutbreakGroups/graph_outbreak_groups.py OutbreakGroups/extracted_outbreak_groups_data.csv OutbreakGroups/outbreak_group_visualization.pdf
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
                "OutbreakGroups/graph_outbreak_groups.py <data file> <graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]


    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
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
    fig = plt.figure(figsize=(12,6))


    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    # Gives the graph a title
    sns.barplot(x = 'Outbreak Group', y = 'Average Number Of Ongoing Outbreaks', data = csv_df, palette = 'magma')
    plt.title('Average Number of Outbreaks per Group', fontsize = 13)
    


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
