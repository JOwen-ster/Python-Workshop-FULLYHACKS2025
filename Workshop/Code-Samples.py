# All code sameples in my slideshow presentation

def countEvensToTen():
    for i in range(11):
        if i % 2 == 0:
            print(i)

    return 'Counted to 10'

countEvensToTen()

myInteger = 4

myString = 'Python'

myFormattedString = F'Hello {myString}'

myBoolean = True

myAnything = None

# Or you can use TYPE HINTS with your code
myInteger: int = 4

myString: str = 'Python'

myFormattedString: str = F'Hello {myString}'

myBoolean: bool = True

# the | means "or"
myAnything: None | any = None

# Variables
number = 27

if number < 0:
    print(F'{number} is less than 0')
elif number % 2 == 0:
    print(F'{number} is even')
else:
    print(F'{number} is odd')

message = 'Python'
is_python = True

if message == 'Python' and is_python:
    print('Both are true')
else:
    print('At least one is false')


if message == 'Python' or is_python:
    print('At least one is true')
else:
    print('Both are false')


if not message == 'Python':
    print('The message is not Python')
else:
    print('The message is Python')

name = 'Python'

match name:
    case 'JavaScript':
        print('The name is JavaScript')
    case 'C++':
        print('The name is C++')
    case 'Python':
        print('The name is Python')
    case _:
        print('Language is unknown')

# input() always returns what you type as a string
user_input = input('Enter a number: ')

try:
    number = int(user_input) # dangerous
    number = isinstance(number, int)
    print(F'{number} is an integer')
except ValueError:
    print(F'{user_input} is not an integer')
finally:
    print('Program completed.')


number = 1

while number < 10:
    print(number)
    number += 1

while True:
    if number == 10:
        print(number)
        break
    print(number)
    number += 1

while number <= 10:
    if number % 2 == 0:
        number += 1
        continue

    print(number)
    number += 1

# range(start, stop(exclusive), step)
# start default is 0
# step default is 1
for i in range(11):
    print(i)

words = ['Python', 'Java', 'C++', 'JavaScript']

for string in words:
    print(string)

for index, string in enumerate(words):
    print(index, string)


if 'Python' in words:
    print('Python is in the list!')

mytuple = ('a', 'b', 'c')

mylist = ['JavaScript', 'Python', 'C++']

# pass in a tuple as a argument to the set function
# you can also define a set using {'a', 'b', 'c'} 
myset = set(('JavaScript', 'Python', 'C++'))

mydictionary = {
    'key': 'value',
    'key2': 'value2'
}

mytuple = (7.2, 'b', True)

print(mytuple[1]) # prints 'b'
print(mytuple[0:2]) # prints (7.2, 'b')
print(mytuple[:2]) # prints (7.2, 'b')
print(mytuple[1:]) # prints ('b', True)
print(mytuple[-1]) # prints True (last item)
print(mytuple[::-1]) # prints (True, 'b', 7.2)
# or used reversing
print(reversed(mytuple)) # returns a reversed tuple

print(mytuple.index('b')) # prints 1

if 'b' in mytuple:
    print('b is in the tuple')

for element in mytuple:
    print(element)

mylist = ['apple', -12, False]

if mylist[1] > 0:
    print('The number is positive')
else:
    print('The number is negative')

mylist[0] = 'banana'
mylist.append('orange')
mylist.insert(1, 'peach')
mylist.remove(False) # specify existing value to remove
mylist.pop(1) # specify index to remove
mylist.sort() # sort the list
mylist.reverse() # reverse the list

for element in mylist:
    print(element)

mySet = {'a', 'b', 'c'}

mySet.add('d')

mySet.remove('a')

for element in mySet:
    print(element)

mydict = {
    "key1": "value1",
    "key2": 2,
    "key3": True
}

mydict['key3'] = 'replaced value3'
mydict['key4'] = 4.0 # new value added since its not an existing key

if 'key2' in mydict:
    print("yes")

if 'value2' in mydict.values():
    print("yes")

for k, v in mydict.items():
    print(k, v)

for k in mydict.keys():
    print(k)

for v in mydict.values():
    print(v)


def myMethod():
    print('Hello, World!')

myMethod()

def addTwoNumbers(number1=4, number2=12):
    result = number1 + number2
    return result

addTwoNumbers(20, 25) # number1 = 20, number2 = 25
addTwoNumbers(20)    # number1 = 20, number2 = 12
addTwoNumbers(number2=25) # number1 = 4, number2 = 25
addTwoNumbers()      # number1 = 4, number2 = 12

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

myStudentObject = Student('Python', 18)
print(myStudentObject.getName())

# 1.
import numpy

from numpy import array

import numpy as np

from numpy import array as np_arr

# 1. usage.
myArray = numpy.array([1, 2, 3, 4, 5])

# 2. usage.
myArray = array([1, 2, 3, 4, 5])

# 3. usage.
myArray = np.array([1, 2, 3, 4, 5])

# 4. usage.
myArray = np_arr([1, 2, 3, 4, 5])
