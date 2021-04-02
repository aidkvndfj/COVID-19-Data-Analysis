'''

This program creates a double line graph using the provided dataset and
combines them into one graph using matplotlibs twinx() function,
combining two graphs with the same x-axes

'''



'''
Importing the two implemented functions that plot the two graphs
is essential for us to later combine them into one
'''
from plotting_functions import plot_avg_precip, plot_avg_temp

# Here we're importing the data required to plot the two graphs
from data.random_data import data
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# Create a figure for drawing the graph and an axes for manipulating that graph
fig, ax1 = plt.subplots(figsize=(10, 6))

# Configure the data into a dataframe that matplotlib can manipulate
df = pd.DataFrame(data)

# Configuring the first set of axes before we plot the first graph
color = "tab:green"
ax1.set_title("Average Percipitation Percentage by Month", fontsize=16)
ax1.set_xlabel('Month', fontsize=16)
ax1.set_ylabel('Avg Temp', fontsize=16, color=color)

# Plot the first graph onto the second set of axes which is currently empty
ax2 = sns.lineplot(x='Month', y='Avg_Temp', data=df, color=color)
ax1.tick_params(axis='y') # Optional

#
# This line says to create a new axes, such that the y-label is placed on the right-hand
# side of the graph where the x-label is invisible but inherited from the original axes.
# We then say the second axis is equal to this axes so that we inherit a right y-label
# that contains the proper y-label for the first graph
#
ax2 = ax1.twinx()
plot_avg_temp()
plt.show()

# Configuring the second set of axes and then graph it
color = 'tab:red'
ax2.set_ylabel('Avg Percipitation %', fontsize=16, color=color)
ax2 = sns.lineplot(x='Month', y='Avg_Percipitation_Perc', data = df, sort=False, color=color)
ax2.tick_params(axis='y', color=color) # Optional

# Save it to a file
fig.savefig("graphs/ax1_2tickparams")

