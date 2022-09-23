#userINput

"""
Type code	Python type
‘u’	Unicode character
‘b’	Int
‘B’	Int
‘h’	Int
‘l’	Int
‘L’	Int
‘q’	Int
‘Q’	Int
‘H’	Int
‘f’	Float
‘d’	Float
‘i’	Int
‘I’	Int
"""
import array as ma
abc = ma.array('d', [2.5, 4.9, 6.7])

abc.append(10.2)
print(abc[3])
print(abc.count)
#print 1 index
print(abc[1])
#print all array items
print("----------")
for x in abc:
    print(x)
defg= ma.array('q',[3,9,6,5,20,13,19,22,30,25])
print("-------------------")
print(defg[3:])
print(defg[-5:])
#inserting the array items at any index
defg.insert(2, 150)
#replacing the array items value
defg[0]=99
print(defg[1:4])
print(defg[7:10])

#array concetanation
first = ma.array('b', [4, 6, 8])
second = ma.array('b', [9, 12, 15])
numbers = ma.array('b')
numbers = first + second
print(numbers)
#delete items by index
#pop() del() method in Python delete the array item
print("----------")
numbers.pop(2)
print(numbers)
print("----------")

#delete elements by value
#The syntax is
#arrayName.remove(value)
numbers.remove(15)
print(numbers)
print("----------")

# Check with
# arrayName.index(value)
# arrayName.reverse()
#Count the occurrence of a Value in Array
# array.count(x)

# Take users input and add the items into array then display it
# Sort the array by ascending order
# Sort the array by Descending Order
# Try to findout the Greatest Number
# Try to findout the Smallest Number
a=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(a[0])
print(a[-1])
print("======================")



v = 4
w = 5
x = 8
y = 2
z = 0
z = v+(w * x) / y;
print("Value of (v+w) * x/ y is ",  z)

"""
num1 = int(input("Enter the first Number: "))
if(num1%2== 0):
    print("{0} is Even ".format(num1))
else:
    print("{0} is Odd ".format(num1))
"""
"""
num1 = int(input("Enter the first Number: "))
num2=  int(input("Enter the second Number: "))
num3=  int(input("Enter the second Number: "))
if(num1>=num2 and num1>=num3):
    print("{0} is greater than {1} and {2}".format(num1, num2, num3))
elif(num2>=num3 and num2>=num1):
    print("{0} is greater than {1} and {2}".format(num2, num1, num3))
else:
    print("{0} is greater than {1} and {2}".format(num3, num2, num1))
"""