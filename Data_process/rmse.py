import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

# Load the experiment and ground truth data from CSV files
exp_data = pd.read_csv('ENU_individual_1Hz_Serial.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east1', 'north1'])
gt_data = pd.read_csv('GT_output_sync_serial.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east2', 'north2'])

# Merge the two data frames based on their timestamps
merged_data = pd.merge(exp_data, gt_data, on='timestamp')

# Calculate the 2D error between the experiment and ground truth data
merged_data['error'] = np.sqrt((merged_data['east1'] - merged_data['east2'])**2 + (merged_data['north1'] - merged_data['north2'])**2)

# Calculate the root mean square error
rmse = np.sqrt(mean_squared_error(merged_data['east1'], merged_data['east2']) + mean_squared_error(merged_data['north1'], merged_data['north2']))

print('Root Mean Square Error:', rmse)
