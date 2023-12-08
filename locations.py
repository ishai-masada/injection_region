import pandas

# Read in the CSV file with the spatial coordinates that make up the airfoil
coordinates = pandas.read_csv("export.csv")

# Separate the coordinates into x, y, and z values
x_coord = coordinates["x"]
y_coord = coordinates["y"]
z_coord = coordinates["z"]

# Define the number of holes in a row
num_holes = 20

# Evenly space out the holes in the x directino
x_locs = list(x_coord)[0::num_holes]

# Define the common y-coordinate
y_fraction = 0.9
y_loc = list(y_coord)[int(y_fraction * len(y_coord))]

sorted_y = coordinates[coordinates['y'] == y_loc]

print(len(sorted_y))
