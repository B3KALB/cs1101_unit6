# Welcome to Unit 6 Learning Journal!

# Part 1
# Write a Python program that does the following. 

# Create a string that is a long series of words separated by spaces. 
# The string is your own creative choice. 
# It can be names, favorite foods, animals, anything. Just make it up yourself. 
# Do not copy the string from another source. 
string_beans = " Jen Blake Hank Hazel Brockway " # this is my initial string

# Turn the string into a list of words using split. 
splitem_up = string_beans.split()# here we use .split() method to seperate at the default " " 
print(splitem_up) # this displays our list with our strings in it

# Delete three words from the list, but delete each one using a different kind of Python operation. 
splitem_up.remove('Jen') # our first method for deleting a value from the list
print(splitem_up) # displays our updated list 

splitem_up.pop(1) # our second method of deleting a value from the list using .pop() and index
print(splitem_up) # displays our updated list

del splitem_up[1] # our third and last method for deleting a value from the list
print(splitem_up) # displays the updated list

# Sort the list. 
splitem_up.sort(reverse = True) # we use the .sort() method to reverse the strings in the list
print(splitem_up) # this displays our updated list

# Add new words to the list (three or more) using three different kinds of Python operations.
splitem_up.append('neJ') # this takes out updated list and adds the first value with the .append() method
print(splitem_up) # this displays our updated list

splitem_up.insert(2,'knaH') # this adds our second value to our list with the .insert() method
print(splitem_up) # this displays our updated list

hazelnut = ['lezaH'] # this creates a variable with a list with a string to pass in
splitem_up.extend(hazelnut) # this adds our third and final value to our list using the .extend() method
print(splitem_up) # this displays our updated list

# Turn the list of words back into a single string using join. 

addem_up = string_beans.join(splitem_up) # here we create a variable that we use to .join() our two lists

# Print the string. 
print(addem_up) # this displays a joined list that is both lists peppered together


# Part 2
# Provide your own examples of the following using Python lists. Do not copy them from another source. 

# Nested lists 
nest_it = ['1', ['22', ['333', '444'], '55', '66'], '7' '8' '9'] # here we have a nested list
print(nest_it) # this displays the whole list
print(nest_it[1]) # this displays the first nested list with the second nested list still in place
print(nest_it[1][1]) # this displays the most internaly nested list

# The “*” operator
multi = 4 * 5**2 # this uses the * in two ways, first as an eponenet of 5, second to multiply 4 times 25
print(multi) # this displays our sum of 100

# List slices 
show_time = 'code to love I' # this creates a variable and asigns it a mixed up string value
print(show_time[-1] + " " + show_time[8:12] + " " + show_time[-9:-7] + " " + show_time[0:4] + '.')
# here we use slice to recode our string and return the new string

# The “+=” operator 
num = 20 # here we assign the variable num the value of 20
num += 13 # here we add and return the value of num plus 13
print(f'I am {num} years old.') # here num has ben updated to its new vaule and displayed as my age

# A list filter 
points = [1, 2, 3, 6] # creates variable points and assigns a list to its value
not_a_td = filter(lambda point: point <= 5, points) # here we loop through the list points, the counter is 
# called point and the condition is less than or equal to 5, if condition is met, store to variable not_a_td
print(list(not_a_td)) # here we tell the display statement the type and the vaiable to return

# A list operation that is legal but does the "wrong" thing, and not what the programmer expects 
nums = [1, 2, 3, 4, 5] # here we assign our list to our variable nums
nums2 = nums.append(6) # here we attempt to add the new int to the list, but nope
print(nums2) # here we get None , not [1, 2, 3, 4, 5, 6]

nums = [1, 2, 3, 4, 5] # here we assign our list to our variable nums
nums.append(6) # this is the big difference, we dont assign the nums list to a new variable name
print(nums) # here we get the result we want [1, 2, 3, 4, 5, 6]

# Provide the Python code and output for your program and all your examples. 