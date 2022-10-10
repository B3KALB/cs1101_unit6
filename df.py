
# Welcome to the Unit 6 Discussion Forum!

# Use the terms "equivalent" and "identical" to distinguish between objects and values. 
# Illustrate the difference further using your own examples with Python lists and the “is” operator.
# is operator

a = [1, 2, 3]
b = [1, 2, 3]
equivalent = a == b
identical = a is b

print(equivalent)
print(identical)
	
b = a
equivalent = a == b
identical = a is b

print(equivalent)
print(identical)
	
# Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

b[0] = 10
print(a)

# Finally, create your own example of a function that modifies a list passed in as an argument. 
def modify_a_list(a):
    z = a[2] + a[1] + a[0]
    a.append(z)
    print(a)
modify_a_list(a)
# Hence, describe what your function does in terms of arguments, parameters, objects, and references. 

# Create your own unique examples for this assignment. Do not copy them from the textbook or any other source.

# The code and its output must be explained technically whenever asked. 
# The explanation can be provided before or after the code, or in the form of code comments within the code. 
# For any descriptive type question, Your answer must be at least 150 words.

# End your discussion post with one question related to programming fundamentals learned in this unit 
# from which your colleagues can formulate a response or generate further discussion. 
# Remember to post your initial response as early as possible, preferably by Sunday evening, 
# to allow time for you and your classmates to have a discussion.