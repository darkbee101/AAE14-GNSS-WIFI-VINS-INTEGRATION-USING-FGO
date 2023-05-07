import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Load the first CSV file
df1 = pd.read_csv('GT_data.csv', header=None, names=['Timestamp', 'East', 'North'])

# Load the second CSV file
df2 = pd.read_csv('wifi_data.csv', header=None, names=['Timestamp', 'East', 'North'])

# Create a figure and axis for the plot and animation
fig, ax = plt.subplots()
line, = ax.plot([], [], color='r')  # set the line color to red
ax.scatter(df1['Timestamp'], df1['North'], label='GT Data', facecolors='none', edgecolors='b')
ax.scatter(df2['Timestamp'], df2['North'], label='Wifi Data', facecolors='none', edgecolors='r')
ax.legend()

# Add axis labels
ax.set_xlabel('Timestamp')
ax.set_ylabel('North')

# Define a function to update the line in each frame of the animation
def update(frame):
    x = df2['Timestamp'][:frame+1]
    y = df2['North'][:frame+1]
    line.set_data(x, y)
    return line,

# Create the animation with 10 frames per second
ani = FuncAnimation(fig, update, frames=len(df2), interval=100, blit=True)

# Set up the writer for the animation
writer = FFMpegWriter(fps=10, metadata=dict(artist='Me'), bitrate=1800)

# Save the animation as an MP4 video
ani.save('wifi_animation2.mp4', writer=writer)

# Show the plot (optional)
plt.show()