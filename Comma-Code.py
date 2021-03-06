# Write a function that takes a list value as an argument and returns a string with all the 
# items separated by a comma and a space, with and inserted before the last item. 
# For example, 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it. 
# Be sure to test the case where an empty list [] is passed to your function.

# List for test
spam = ['apples', 'bananas', 'tofu', 'cats']
a = [1, 2, 3, 4, 5]
b = ['Hi', 'Hola', 'Hallo', 'Ciao']
c = ['One', 'Two', 1, 2]
d = []

# Create the function.
def commaCode(list):
    list.insert(-1, 'and')    # Insert the string 'and' before the last item of the list.
    for i in list[:-2]:       # Print every element on the list (before the inserted string 'and') separated by a comma and a space.
        print(str(i) + ', ', end='')
    for a in list[-2:]:       # Print the inserted string 'and' plus the last element on the list.
        print(str(a) + ' ', end='')
    print()                   # Print a space between each Test List

# Test        
commaCode(spam)
commaCode(a)
commaCode(b)
commaCode(c)
commaCode(d)
