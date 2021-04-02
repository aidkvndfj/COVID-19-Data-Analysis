# Import the required libraries and data for plotting
from data.random_data import data
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# This function produces a line graph using average precipitation and saves it to a file
def plot_avg_precip():
    # Convert the dictionary data into a dataframe
    df = pd.DataFrame(data)

    # Create a drawing figure
    fig = plt.figure()

    # Set the theme
    sns.set_theme(style="darkgrid")

    # create line plot for average precip levels
    plt.title('Average Precipitation Percent By Month')
    sns.lineplot(x='Month', y='Avg_Percipitation_Perc', data=df, sort=False)

    # Save the average precip into a file
    fig.savefig("graphs/avg_precip")

def plot_avg_temp():
    # Convert the dictionary data into a dataframe
    df = pd.DataFrame(data)

    # Create a drawing figure
    fig = plt.figure()

    # Set the theme
    sns.set_theme(style="darkgrid")

    # Create line plot for average temperature in fahrenheit
    plt.title("Average Temperature By Month")
    sns.lineplot(x="Month", y="Avg_Temp", data=df, palette="summer")

    # Save the average temp into a file
    fig.savefig("graphs/avg_temp", bbox_inches="tight")