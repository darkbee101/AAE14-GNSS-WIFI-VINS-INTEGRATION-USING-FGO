import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the experiment and ground truth data from CSV files
vins_exp_data = pd.read_csv('ENU_individual_1Hz_Serial.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east1', 'north1'])
wifi_exp_data = pd.read_csv('Wi-Fi_data_sync_serial.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east1', 'north1'])
gnss_exp_data = pd.read_csv('gnss_data_sync_serial.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east1', 'north1'])
inte_exp_data = pd.read_csv('optimized_data_synced.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east1', 'north1'])
gt_data = pd.read_csv('GT_output_sync_serial.csv', header=None, usecols=[0,1,2], names=['timestamp', 'east2', 'north2'])


#VINS
# Merge the two data frames based on their timestamps
vins_merged_data = pd.merge(vins_exp_data, gt_data, on='timestamp')

# Calculate the 2D error between the experiment and ground truth data
vins_merged_data['error'] = np.sqrt((vins_merged_data['east1'] - vins_merged_data['east2'])**2 + (vins_merged_data['north1'] - vins_merged_data['north2'])**2)

# Plot the 2D error as a function of time
plt.plot(vins_merged_data['timestamp'], vins_merged_data['error'], color='green', label='VINS')
plt.scatter(vins_merged_data['timestamp'], vins_merged_data['error'], facecolors='none', edgecolors='green')


#gnss
# Merge the two data frames based on their timestamps
gnss_merged_data = pd.merge(gnss_exp_data, gt_data, on='timestamp')

# Calculate the 2D error between the experiment and ground truth data
gnss_merged_data['error'] = np.sqrt((gnss_merged_data['east1'] - gnss_merged_data['east2'])**2 + (gnss_merged_data['north1'] - gnss_merged_data['north2'])**2)

# Plot the 2D error as a function of time
plt.plot(gnss_merged_data['timestamp'], gnss_merged_data['error'], color='blue', label="GNSS")
plt.scatter(gnss_merged_data['timestamp'], gnss_merged_data['error'], facecolors='none', edgecolors='blue')


#wifi
# Merge the two data frames based on their timestamps
wifi_merged_data = pd.merge(wifi_exp_data, gt_data, on='timestamp')

# Calculate the 2D error between the experiment and ground truth data
wifi_merged_data['error'] = np.sqrt((wifi_merged_data['east1'] - wifi_merged_data['east2'])**2 + (wifi_merged_data['north1'] - wifi_merged_data['north2'])**2)

# Plot the 2D error as a function of time
plt.plot(wifi_merged_data['timestamp'], wifi_merged_data['error'], color='orange', label="Wi-Fi RTT")
plt.scatter(wifi_merged_data['timestamp'], wifi_merged_data['error'], facecolors='none', edgecolors='orange')


#integrate
# Merge the two data frames based on their timestamps
inte_merged_data = pd.merge(inte_exp_data, gt_data, on='timestamp')

# Calculate the 2D error between the experiment and ground truth data
inte_merged_data['error'] = np.sqrt((inte_merged_data['east1'] - inte_merged_data['east2'])**2 + (inte_merged_data['north1'] - inte_merged_data['north2'])**2)

# Plot the 2D error as a function of time
plt.plot(inte_merged_data['timestamp'], inte_merged_data['error'], color='black', label='FGO')
plt.scatter(inte_merged_data['timestamp'], inte_merged_data['error'], facecolors='none', edgecolors='black')



#calculate maximum 2d error
vins_max_error = np.max(vins_merged_data['error'])
gnss_max_error = np.max(gnss_merged_data['error'])
wifi_max_error = np.max(wifi_merged_data['error'])
inte_max_error = np.max(inte_merged_data['error'])
print('vins_max_error:', vins_max_error)
print('gnss_max_error:', gnss_max_error)
print('wifi_max_error:', wifi_max_error)
print('inte_max_error:', inte_max_error)

#add graph label
plt.xlabel('Time (seconds)')
plt.ylabel('Error (meters)')
plt.title('2D error of experiment data')
plt.legend()
plt.show()
