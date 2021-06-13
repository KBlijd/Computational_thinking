# To write more efficient code we first define getBoxString with the variable "measurement"
def getBoxString(measurement):
    return f"Please give the {measurement} of the box in centimetres"
# First we will ask the user to give the length of the box
# We allow the user to give input
# The input is converted so we can calculate with it later on
# We label the input as "x"
print(getBoxString("height"))
x = int(input())
# Secondly we will ask the user to give the width of the box
# We allow the user to give input
# The input is converted so we can calculate with it later on
# We label the input as "y"
print(getBoxString("width"))
y = int(input())
# Next we will ask the user to give the height of the box
# We allow the user to give input
# The input is converted so we can calculate with it later on
# We label the input as "z"
print(getBoxString("length"))
z = int(input())
# Now we simply calculate the volume of the box by multiplying the variables given by the user and label this as "volumecm"
volumecm = int(x * y * z)
# Next we calculate the volume of the box in litres by dividing "volumecm" by 1000
volumel = volumecm / 1000
# At last we return the volume of the box in cm^3 and litres to the user
print(f"The volume of the box is", volumecm, "cubic centimetres, this is equal to", volumel, "litres")
