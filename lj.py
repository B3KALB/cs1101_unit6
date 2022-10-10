# Welcome to Unit 6 Learning Journal!

# Part 1
# Write a Python program that does the following. 

# Create a string that is a long series of words separated by spaces. 
# The string is your own creative choice. 
# It can be names, favorite foods, animals, anything. Just make it up yourself. 
# Do not copy the string from another source. 
string_beans = " Jen Blake Hank Hazel Brockway "

# Turn the string into a list of words using split. 
splitem_up = string_beans.split()
print(splitem_up)

# Delete three words from the list, but delete each one using a different kind of Python operation. 
splitem_up.remove('Jen')
print(splitem_up)
splitem_up.pop(1)
print(splitem_up)
del splitem_up[1]
print(splitem_up)

# Sort the list. 
splitem_up.sort(reverse = True)
print(splitem_up)

# Add new words to the list (three or more) using three different kinds of Python operations.
splitem_up.append('neJ')
print(splitem_up)
splitem_up.insert(2,'knaH')
print(splitem_up)
hazelnut = ['lezaH']
splitem_up.extend(hazelnut)
print(splitem_up)

# Turn the list of words back into a single string using join. 

addem_up = string_beans.join(splitem_up)
# Print the string. 
print(addem_up)


# Part 2
# Provide your own examples of the following using Python lists. Do not copy them from another source. 

# Nested lists 
nest_it = ['1', ['22', ['333', '444'], '55', '66'], '7' '8' '9']
print(nest_it)
print(nest_it[1])
print(nest_it[1][1])

# The “*” operator
multi = 4 * 5**2
print(multi)

# List slices 
show_time = 'code to love I'
print(show_time[-1] + " " + show_time[8:12] + " " + show_time[-9:-7] + " " + show_time[0:4] + '.')

# The “+=” operator 
num = 20
num += 13
print(f'I am {num} years old.')

# A list filter 
points = [1, 2, 3, 6]
not_a_td = filter(lambda point: point <= 5, points)
print(list(not_a_td))

# A list operation that is legal but does the "wrong" thing, and not what the programmer expects 
nums = [1, 2, 3, 4, 5]
nums2 = nums.append(6)
print(nums2)

nums = [1, 2, 3, 4, 5]
nums.append(6)
print(nums)
# Provide the Python code and output for your program and all your examples. 