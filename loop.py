#for
#while
#do while
#example for while loop
x=0
while x<4:
    print(x)
    x=x+1

x=1
print("-----------")
for x in range(2,7):
    print(x)
print("-----------")

Months = ["Jan","Feb","Mar","Apr","May","Jun", "Jul", "AUG", "Sep", "Oct", "Nov", "Dec"]

for m in Months:
    print(m)

for x in range (10,20):
    if (x == 15): break
    print(x)
print("--------")
for x in range (10,20):
    if (x == 15): continue
    print(x)
#enumerate
"""enumerate() IN PYTHON is a built-in function used for assigning an index to each item of the iterable object. It adds a loop on the iterable objects while keeping track of the current item and returns the object in an enumerable form."""
print("-----------")
for i, m in enumerate (Months):
    print(i, m)

#repeating multiple times for same statement
for i in '123':
    print("laba", i, )
#•	While loops are executed based on whether the conditional statement is true or false.
#•	For loops are called iterators, it iterates the element based on the condition set
#•	Python For loops can also be used for a set of various other things (specifying the collection of elements we want to loop over)
#•	Breakpoint is used in For Loop to break or terminate the program at any particular point
#•	Continue statement will continue to print out the statement, and prints out the result as per the condition set
#•	Enumerate function in “for loop” returns the member of the collection that we are looking at with the index number

my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')

print('Loop is Terminated')
for i in range(1,6):
    for j in range(i):
        print(" * ", end = ' ')
    print()

print("------------")
i=5
j=5
for i in range(i):
    for j in range(j):
        print(" * ", end = ' ')
    print()
    i = i - 1
    i=j

print("------------")
i=5
j=5
for i in range(i):
    for j in range(j):
        if i%2==0:
            print(" * ", end = ' ')
        else:
            print(" # ", end=' ')
    print()
    i = i - 1
    i=j


