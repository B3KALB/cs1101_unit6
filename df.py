
# Welcome to the Unit 6 Discussion Forum!

# Use the terms "equivalent" and "identical" to distinguish between objects and values. 
# Illustrate the difference further using your own examples with Python lists and the “is” operator.
# is operator

a = [1, 2, 3] # This sets the first list to variable a
b = [1, 2, 3] # This sets the second list to variable b 
equivalent = a == b # equivalenrt checks if values are the same
identical = a is b # identical checks is the identifiers are the same

print(equivalent) # this prints the boolean value for equivalent
print(identical) # this prints the boolean value for identical
# output
# True  
# False
	
b = a # here we are reasigning variable b to variable a 
equivalent = a == b # equivalenrt checks if values are the same
identical = a is b # identical checks is the identifiers are the same

print(equivalent) # this prints the boolean value for equivalent
print(identical) # this prints the boolean value for identical
# output
# True
# True
	
# Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

b[0] = 10 #here we ar changing the value of b index 0 to 10
print(a) # here we are printing a to show how when you refer after aliasing, b is a 
# output
# [10, 2, 3]

# Finally, create your own example of a function that modifies a list passed in as an argument. 
def modify_a_list(a): # this creates our function modify_a_list with the arument passed in
    z = a[2] + a[1] + a[0] # here we refer and add all the indexes from a and asign those to var z
    a.append(z) # here we add our new int to our refered to list 
    print(a) # this print shows the new list with a and z
modify_a_list(a) # this calls the function and passes in the argument a
# output
# [10, 2, 3, 15]

# Hence, describe what your function does in terms of arguments, parameters, objects, and references. 

# Create your own unique examples for this assignment. Do not copy them from the textbook or any other source.

# The code and its output must be explained technically whenever asked. 
# The explanation can be provided before or after the code, or in the form of code comments within the code. 
# For any descriptive type question, Your answer must be at least 150 words.

# End your discussion post with one question related to programming fundamentals learned in this unit 
# from which your colleagues can formulate a response or generate further discussion. 
# Remember to post your initial response as early as possible, preferably by Sunday evening, 
# to allow time for you and your classmates to have a discussion.