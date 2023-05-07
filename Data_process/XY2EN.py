import numpy as np
import csv

def convert_to_ENU(x, y, rotation_angle):
    # Convert rotation angle to radians
    theta = np.radians(rotation_angle)

    # Define rotation matrix
    R = np.array([[np.cos(theta), np.sin(theta), 0],
                  [-np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])

    # Define vector in local coordinate system
    v_local = np.array([x, y, 0])

    # Apply rotation matrix to get ENU coordinates
    v_ENU = R @ v_local

    return v_ENU[0], v_ENU[1]



# Open text file
filename = 'sue_data_deleted.txt'
with open(filename, 'r') as file, open('output_file.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Loop through each line in file
    for line in file:
        # Split line into x and y values
        timestamp, x, y, x_c, y_c = map(float, line.split())

        # Convert to ENU coordinates with rotation angle of 252 clockwise
        E, N = convert_to_ENU(x, y, 18)

        # Convert covariance to ENU coordinates with rotation angle of 252 clockwise
        E_c, N_c = convert_to_ENU(x_c, y_c, 18)

        # Write the data to the CSV file
        writer.writerow([int(timestamp), E, N, E_c, N_c])
