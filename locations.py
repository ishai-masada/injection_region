import csv

# Read in the airfoil coordinates from the text file
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

# Define the middle index to obtain the point at the middle of the blade
mid_idx = int(len(coordinates) / 2)

# Find the indices above and below the middle point
upper_portion = range(mid_idx, mid_idx + (num_holes * interval) + interval, interval)
lower_portion = range(mid_idx, mid_idx - ((num_holes * interval) + interval), -interval)


# Sort the x, y, and z values in ascending order
x_values = list(x_coords.values())
y_values = list(y_coords.values())
z_values = list(z_coords.values())
x_values.sort()
y_values.sort()
z_values.sort()

# List for coordinate storage
x_points = []
y_points = []
z_points = []

# Add each value to its corresponding coordinate axis
for idx in lower_portion:
    x_points.append(x_values[idx])
    y_points.append(y_values[idx])
    z_points.append(z_values[idx])
for idx in upper_portion:
    x_points.append(x_values[idx])
    y_points.append(y_values[idx])
    z_points.append(z_values[idx])

push_coordinates = tuple(zip(x_points, y_points, z_points))

# Write the injection locations to a file
with open('injection regions.csv', 'w', newline='') as csvfile:
    coord_writer = csv.writer(csvfile, delimiter=',')
    for point in push_coordinates:
        coord_writer.writerow([point[0]])
        coord_writer.writerow([point[1]])
        coord_writer.writerow([point[2]])

