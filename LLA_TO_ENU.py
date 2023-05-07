import csv
import math

# Define the WGS84 ellipsoid parameters
a = 6378137.0  # semi-major axis (m)
f = 1/298.257223563  # inverse flattening

# Define the ENU coordinate system origin (reference point)
origin_lat = math.radians(22.306629283333336)  # San Francisco latitude
origin_lon = math.radians(114.17923408333333)  # San Francisco longitude
origin_alt = 0  # altitude (m)

# Define the input and output file paths
input_file = 'output5.csv'
output_file = 'output6.csv'

# Open the input and output files
with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    # Create CSV reader and writer objects
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    
    # Loop over each row in the input CSV file
    for row in reader:
        # Get the latitude and longitude coordinates
        lat = float(row[0])
        lon = float(row[1])
        
        # Convert the latitude and longitude coordinates to ECEF coordinates
        sin_lat = math.sin(math.radians(lat))
        cos_lat = math.cos(math.radians(lat))
        sin_lon = math.sin(math.radians(lon))
        cos_lon = math.cos(math.radians(lon))
        ecef_x = (a / math.sqrt(1 - (2*f - f*f) * sin_lat*sin_lat)) * cos_lat * cos_lon
        ecef_y = (a / math.sqrt(1 - (2*f - f*f) * sin_lat*sin_lat)) * cos_lat * sin_lon
        ecef_z = (a*(1-f)*(1-f) / math.sqrt(1 - (2*f - f*f) * sin_lat*sin_lat)) * sin_lat
        
        # Convert the ECEF coordinates to ENU coordinates
        sin_origin_lat = math.sin(origin_lat)
        cos_origin_lat = math.cos(origin_lat)
        sin_origin_lon = math.sin(origin_lon)
        cos_origin_lon = math.cos(origin_lon)
        dx = ecef_x - (a / math.sqrt(1 - (2*f - f*f) * sin_origin_lat*sin_origin_lat)) * cos_origin_lat * cos_origin_lon
        dy = ecef_y - (a / math.sqrt(1 - (2*f - f*f) * sin_origin_lat*sin_origin_lat)) * cos_origin_lat * sin_origin_lon
        dz = ecef_z - (a*(1-f)*(1-f) / math.sqrt(1 - (2*f - f*f) * sin_origin_lat*sin_origin_lat)) * sin_origin_lat
        enu_east = -sin_origin_lon*dx + cos_origin_lon*dy
        enu_north = -sin_origin_lat*cos_origin_lon*dx - sin_origin_lat*sin_origin_lon*dy + cos_origin_lat*dz
        enu_up = cos_origin_lat*cos_origin_lon*dx + cos_origin_lat*sin_origin_lon*dy + sin_origin_lat*dz
        
        # Write the ENU coordinates to the output CSV file
        writer.writerow([enu_east, enu_north, enu_up])
