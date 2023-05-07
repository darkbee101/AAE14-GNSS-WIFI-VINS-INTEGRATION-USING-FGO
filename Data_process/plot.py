import csv
import matplotlib.pyplot as plt

# Load data from first CSV file
x1 = []
y1 = []
with open('GT_output_sync_serial.csv', 'r') as file1:
    reader = csv.reader(file1)
    #next(reader)  # Skip header row
    for row in reader:
        x1.append(float(row[0]))
        #y1.append(float(row[2]))
        y1.append(float(row[1]))

# Load data from second CSV file
x2 = []
y2 = []
with open('optimized_data_synced.csv', 'r') as file2:
    reader = csv.reader(file2)
    #next(reader)  # Skip header row
    for row in reader:
        x2.append(float(row[0]))
        #y2.append(float(row[2]))
        y2.append(float(row[1]))

# Plot the data
plt.plot(x1, y1, 'bo', label='Ground Truth')
#plt.plot(x2, y2, 'rx', label='VINS (individual)')
#plt.plot(x2, y2, 'rx', label='GNSS data')
#plt.plot(x2, y2, 'rx', label='Wi-Fi RTT')
plt.plot(x2, y2, 'rx', label='FGO integrated data')
plt.xlabel('time/s')
#plt.ylabel('North Coordinate')
#plt.title('Comparison of North Coordinates')
plt.ylabel('East Coordinate')
plt.title('Comparison of East Coordinates')
plt.legend()
plt.show()
