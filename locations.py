import os
import csv

# Read in the coordinates from the text file
with open('s1 blade.txt', 'r') as f:
    coordinates = f.read().strip().splitlines()

# Coordinates
x_coords = {}
y_coords = {}
z_coords = {}

# Sort Coordinates
for idx, line in enumerate(coordinates):
    # Separate the coordinates into x, y, and z coordinates
    coord_set = line.split(',')

    # Add each coordinate and its corresponding index to a dictionary
    x_coords[idx] = float(coord_set[0][:-4])
    y_coords[idx] = float(coord_set[1][:-4])
    z_coords[idx] = float(coord_set[2][:-4])

# Define the number of holes in a row and the interval of coordinates between each hole
num_holes = 20
interval = 20

# Sort the z values in ascending order
x_values = list(x_coords.values())
y_values = list(y_coords.values())
z_values = list(z_coords.values())
z_values.sort()

# Find the middle z index of the blade 
middle_idx = int(len(z_values) / 2)

# Find the minimum and maximum indices
lower_idx = middle_idx - ((num_holes * interval) + interval)
upper_idx = middle_idx + (num_holes * interval) + interval

'''
List Slice: [START: END: INTERVAL]
'''
# Find the z coordinates given by the indices
z_points = z_values[lower_idx: upper_idx: interval]

# Lists for coordinate storage
x_points = []
y_points = []

# Add each value to its corresponding coordinate axis
for z_point in z_points:
    # Adjust to meters
    x_points.append(x_values[z_values.index(z_point)] / 10)
    y_points.append(y_values[z_values.index(z_point)] / 10)

'''
Write the injection locations to a file

NOTE: Code works. Don't change it.
'''
# Match the x, y, and z coordinates with each other
push_coordinates = tuple(zip(x_points, y_points, z_points))

filename = 'injection regions.csv'

# Erase the contents of the file
open(filename, 'w').close()

# Open the file to use csv module
with open(filename, 'w', newline='\n') as csvfile:
    coord_writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')

    # File Format Requirements
    csvfile.write('[Name]\nS1 Blade\n\n')
    csvfile.write('[Spatial Fields]\n')
    coord_writer.writerow(['X', 'Y', 'Z'])
    csvfile.write('\n[Data]\n')
    coord_writer.writerow(['X[m]', 'Y[m]', 'Z[m]'])
    csvfile.write('\n')

    # Write each set of coordinates as a row in the file
    for point in push_coordinates:
        coord_writer.writerow([point[0], point[1], point[2]])
