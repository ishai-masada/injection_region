import pandas
import matplotlib.pyplot as plt

# Read in the CSV file with the spatial coordinates that make up the airfoil
coordinates = pandas.read_csv("export.csv")

# Separate the coordinates into x, y, and z values
x_coord = list(coordinates["x"])
y_coord = list(coordinates["y"])
z_coord = list(coordinates["z"])

# Define the number of holes in a row
num_holes = 20

# Evenly space out the holes in the x directino
x_locs = list(x_coord)[0::num_holes]

# Define the common y-coordinate
z_fraction = 0.9
z_loc = list(z_coord)[int(z_fraction * len(z_coord))]

sorted_z = coordinates[coordinates['z'] == z_loc]

#print(z_loc)
