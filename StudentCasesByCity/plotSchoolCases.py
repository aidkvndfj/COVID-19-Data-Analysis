'''
plotSchoolCases.py
  Author(s): Jason Kyle Tan (1134487)

  Project: Team Group Project
  Date of Last Update: March 21, 2021
  Previous Author(s): Conner Leavitt

  Functional Summary
    This program takes the previously generated data from extractConfirmedStudentCases.py
    and plots it onto a bar graph, allowing the user to visually see the
    difference in the number of cases across students for different cities.

     Commandline Parameters: 2
        argv[1] = studentCasesPerCity.txt (data file)
        argv[2] = <graph.pdf> (graph file the user wants to save to)
            Accepted graph formats: .png, .jpg, .pdf

  Command to run: python plotSchoolCases.py <dataToPlot.txt>
    Note: <dataToPlot.txt> is the file generated from extractConfirmedStudentCases.py,
           but in the event that the user has followed from extractConfirmedStudentCases.py, 
           then <dataToPlot.txt> is studentCasesPerCity.txt
    Accepted data file formats: .txt, .csv

'''

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import textwrap

def main(argv):
    # Check for correct usage
    if len(argv) != 3:
        print('Usage: python plotSchoolCases.py <data file> <graph file>')
        sys.exit(1)
    
    # Assign the user input to the file which contains the data we want to plot
    # and the file we want to save our graph to
    filename = argv[1]
    graphFilename = argv[2]

    # Attempt to open the file
    try:
        # Here we're reading it as a dataframe object required for seaborn to properly
        # plot the graph required for this program
        df = pd.read_csv(filename)

    except IOError as err:
        print("Unable to open file '{}' : {}".format(filename, err),
              file=sys.stderr)
        sys.exit(1)

    # Create a drawing figure
    fig = plt.figure()

    # Set the theme
    sns.set_theme(style="darkgrid")

    # Create bar plot for total number of cases per city in terms of students
    plt.title("Total number of Confirmed Student Cases per City")

    # 
    # Set the line underneath equal to the variable name 'ax' if highlighting Toronto and Ottawa,
    # like this,
    # ax = sns.barplot(x="City", y="ConfirmedNumberOfCases", data=df)
    #
    sns.barplot(x="City", y="ConfirmedNumberOfCases", data=df)

    plt.xlabel("Cities")
    plt.ylabel("Confirmed Number of Student Cases")

    #
    # Uncomment to highlight Toronto and Ottawa on the plot
    #
    # texts = [textwrap.fill(t.get_text(), 10)  for t in ax.get_xticklabels()]
    # for text in texts:
    #     if text not in ["Toronto", "Ottawa"]:
    #         texts[texts.index(text)] = ""
    # plt.xticks(rotation=90)
    # ax.set_xticklabels(texts)

    # Save the graph into a file
    fig.savefig(graphFilename, bbox_inches="tight")



main(sys.argv)