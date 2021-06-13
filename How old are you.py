# We start by importing the datetime module, this will allow the code to provide correct information regarding the year
import datetime
now = datetime.datetime.now()
# Now we define the variable "year"
year = (now.year)
# Next we introduce ourself, ask the name of the user and allow for input which we label as "name"
name = input("Hi, I'm a very easy computer program, you can call me Python, can I know your name?")
# Next we ask for the year of birth which we label as integer named "x" so we can calculate with it later on
x = int(input("Hi, nice to meet you! May I ask you what your year of birth is?"))
# Now we return the age of the user
print(x, "What a nice year to be born! Being born in", x, "means that you will be", year - x, "years old this year!")
# The following part is additional and only serves to create a dialogue with the user
print("Are you feeling old already? ;-) Yes or no")
y = input("")
z = int(2020)
q= year - z
if y == "yes":
    print("You shouldn't! My code was written in", z, "Which means that I will be", q, "years old this year")
elif y == "no":
    print("Very good!")
else: print("I don't understand that but I hope the answer was no!")
print: "rosie"


