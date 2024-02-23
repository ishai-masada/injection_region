import csv

# Read in the coordinates from the text file
with open('s1 blade.txt', 'r') as f:
    coordinates = f.read().strip().splitlines()

# Coordinates
x_coords = []
y_coords = []
z_coords = []

# Sort Coordinates
for line in coordinates:
    # Separate the coordinates into x, y, and z coordinates
    coord_set = line.split(',')

    # Add each coordinate to its corresponding list and apply the scientific notation
    x_coords.append(float(coord_set[0][:-4]) / 10**(int(coord_set[0][-1:])))
    y_coords.append(float(coord_set[1][:-4]) / 10**(int(coord_set[1][-1:])))
    z_coords.append(float(coord_set[2][:-4]) / 10**(int(coord_set[2][-1:])))


# Sort the z values in ascending order
z_coords.sort()

# Find the middle z index of the blade 
middle_idx = int(len(z_coords) / 2)

# Define the number of holes in a row and the interval between each hole
num_holes = 20
interval = 20

# Find the minimum and maximum indices
lower_idx = middle_idx - ((num_holes * interval) + interval)
upper_idx = middle_idx + (num_holes * interval) + interval

'''
List Slice: [START: END: INTERVAL]
'''
# Find the z coordinates given by the indices
z_points = z_coords[lower_idx: upper_idx: interval]

# Lists for coordinate storage
x_points = []
y_points = []

# Add each value to its corresponding coordinate axis
for z in z_points:
    x_points.append(x_coords[z_coords.index(z)])
    y_points.append(y_coords[z_coords.index(z)])

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
