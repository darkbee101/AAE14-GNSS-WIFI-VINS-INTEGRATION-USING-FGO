import csv
import re

# Open the input and output files
with open("D:\FYP\Final\Data\Experimental Data\gnss_log_2023_04_03_18_39_45.nmea", "r") as in_file, open("output1.csv", "w", newline="") as out_file:
    # Create a CSV writer object
    writer = csv.writer(out_file)
    
    # Write the header row
    writer.writerow(["GSA_15", "GSA_16", "GSA_17", "GGA_3", "GGA_5"])
    
    # Initialize a counter to keep track of the number of sets processed
    counter = 0
    
    # Loop through each line in the input file
    for line in in_file:
        # Check if the line starts with "$GNGSA"
        if line.startswith("$GNGSA"):
            # Split the line by commas and extract the 15th, 16th, and 17th values
            values = line.split(",")
            gsa_15 = float(values[15])
            gsa_16 = float(values[16])
            gsa_17 = str(values[17])

            
            
            writer.writerow([gsa_15, gsa_16, gsa_17])
            
            
        # Check if the line starts with "$GNGGA"
        elif line.startswith("$GPGGA"):
            # Split the line by commas and extract the 3rd and 5th values
            values = line.split(",")
            if values[2] == '' or values[4] == '':
                values[2] = '0'
                values[4] = '0'
            else:
                gga_3 = float(values[2])/100
                gga_5 = float(values[4])/100
                writer.writerow([gga_3, gga_5])
        else:
            continue
           
            
            
