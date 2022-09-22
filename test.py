print("I am print I am from testpy file")
# Python Single line Comment
# Print 8 New Lines
print (8 * "\n")
print ("Welcome to Python Training")
# print end line
print ("Welcome to", end = ' ')
print ("Training", end = '!')
x='Y'
#String variables can be declared either by using single or double quotes:
print(type(x))

paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print(2 * paragraph,  end="\n");

'''
This is a multiline
comment.
'''

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

#Multiple Assignment
a = b = c = 1
#Multiple Assignment
d,e,f = 1,2,"john"
print(f);#John
"""
Python has five standard data types −
•	Numbers
•	String
•	List
•	Tuple
•	Dictionary

"""

str = 'Hello World!'
print(str)          # Prints complete string
print(str[0])      # Prints first character of the string
print(str[2:5])    # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)     # Prints string two times
print(str + "TEST") # Prints concatenated string

#list
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)          # Prints complete list
print (list[0] )      # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd
print (list[2:] )     # Prints elements starting from 3rd element
print (tinylist * 2)  	# Prints list two times
print (list + tinylist) # Prints concatenated lists

"""
The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. 
"""
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print(tuple)               # Prints the complete tuple
print(tuple[0])           # Prints first element of the tuple
print(tuple[1:3])         # Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])          # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)       # Prints the contents of the tuple twice
print(tuple + tinytuple)

"""Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). """
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict['one'])       # Prints value for 'one' key
print(dict[2])       # Prints value for 2 key
print(tinydict)         # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values())
"""Python language supports the following types of operators.
•	Arithmetic Operators
•	Comparison (Relational) Operators
•	Assignment Operators
•	Logical Operators
"""
#** Exponent
x=2**3
print(x)

# // Floor Division
y=9//2
print(y)


a = True

b = False

print(('a and b is',a and b))

print(('a or b is',a or b))

print(('not a is',not a))


# Python Members operator in

x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")
if ( y not in list ):
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

#Python Identity Operators
x = 20
y = 20
if x is y:
    print("x & y  SAME identity")
y=20
if x is not y:
    print("x & y have DIFFERENT identity")
