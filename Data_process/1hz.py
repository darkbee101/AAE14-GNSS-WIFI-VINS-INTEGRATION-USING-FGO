import csv

# Open the input and output files
with open('ENU_sue_for_integrate.csv', 'r') as input_file, open('ENU_sue_for_integrate_1Hz.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')

    # Keep track of the timestamps we've seen
    seen_timestamps = set()

    # Loop over each row in the input file
    for row in reader:
        timestamp = row[0]

        # If we haven't seen this timestamp before, write the row to the output file and add it to the set of seen timestamps
        if timestamp not in seen_timestamps:
            writer.writerow(row)
            seen_timestamps.add(timestamp)