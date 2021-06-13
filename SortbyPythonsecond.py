# First we will initialise the list of coordinates
coordinates = [("f", 9), ("z", 2), ("t", 4), ("x", 8), ("b", 1), ("m", 7)]
# Secondly we will set "second" to index 1 of coordinate
second = lambda coordinate: coordinate[1]
# Now we set the sort key to "second", set the sort in ascending order and sort the list
coordinates.sort(key=second, reverse=False)
# In the last step we will output the sorted list of coordinates
print(coordinates)


