import csv

with open('ENU_individual_1Hz.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)



# Change timestamps to serial
for i in range(len(rows)):
    rows[i][0] = i + 1

with open('ENU_individual_1Hz_serial.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)