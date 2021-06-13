# We start by importing the math module
import math
# We assign the variable "elements" to 500000
elements = float(500000)
# We calculate the time complexity of the merge sort algorithm
mergesort = float(500000)*math.log2(500000)
# We calculate the time complexity of the quick sort algorithm
quicksort = float(500000**2)
# We calculate how many times faster the worst case for merge sort is than the worst case for quicksort
difference = int(round(quicksort/mergesort))
# We return how many times faster merge sort is in comparison to quick sort
print("The worst case for merge sort is", difference, "times faster than quick sort for a list of 500000 elements")