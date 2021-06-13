# We will start by asking the user for a sentence as input, we will store the input under the variable "sentence"
sentence = input("Please state you sentence")
# Secondly we will split the sentence and store the output under the variable "split"
split = (sentence.split())
# Now we will count the amount of words and store the output under the variable "words"
words = len(split)
# At last we will return the amount of words in the sentence to the user
print("The amount of words in your sentence is", words)