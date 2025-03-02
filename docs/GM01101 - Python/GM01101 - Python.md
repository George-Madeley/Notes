# GM01101: Python

@ George Madeley
@ Personal Studies
@ 6/7/23

### Introduction

This is a collection of notes that I, George Madeley, took when taking
the Codecademy Python Beginner, Intermediate Python, and Advanced Python
courses. I do not take ownership of the material covered and these notes
should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: Python Beginner](#python-beginner)

[1 - Hello World](#hello-world)

[2 - Control Flow](#control-flow)

[3 - Lists](#lists)

[4 - Loops](#loops)

[5 - Functions](#functions)

[6 - Python Strings](#python-strings)

[7 - Modules](#modules)

[8 - Dictionaries](#dictionaries)

[9 - Files](#files)

[10 - Classes](#classes)

[Section 2: Intermediate Python](#intermediate-python)

[1 - Functional Arguments](#functional-arguments)

[2 - Namespaces and Scopes](#namespaces-and-scopes)

[3 - Functions Deep Dive](#functions-deep-dive)

[4 - Object Oriented Programming](#object-oriented-programming-1)

[5 - Unit Testing](#unit-testing)

[6 - Iterators and Generators](#iterators-and-generators)

[7 - Specialized Collections](#specialized-collections)

[8 - Resource Management](#resource-management)

[9 - Regular Expressions](#regular-expressions)

[Section 3: Advanced Python](#advanced-python)

[1 - Logging](#logging)

[2 - Functional Programming](#functional-programming)

[3 - Database Operations](#database-operations)

[4 - Concurrent Programming](#concurrent-programming)

## Python Beginner

### Hello World

#### Comments

To comment things in Python, we use a #.

```text
## This is a comment
```

#### Print

To print things in Python, we use the print() function.

```text
print("Hello World!")
```

#### Variables

We can create variables in Python just like in any other language
however, in Python, we do not need to specify the data type.

```text
name = "George"
```

#### Operations

Python has the following mathematical operations:

- **Add** +

- **Subtract** -

- **Multiply** \*

- **Divide** /

- **Exponent** \*\*

- **Modulo** %

#### Multiline Strings

We can create multi-line strings in Python:

```text
"""
This is a multi-line comment
"""
```

### Control Flow

#### Relational Operators

Relational operators are used to compare two values then return true or
false. The following are all the relational operators:

- **Equal to** ==

- **Not equal to** !=

- **Greater than** \>

- **Less than** \<

- **Greater than or equal to** \>=

- **Less than or equal to** \<=

#### Boolean Operators

Boolean operators compare two or more values and return true or false
based on the values. The following are all the Boolean operators:

- and **--** All values need to be true for the return to also be true.

- or **--** Only one value needs to be true for the return to also be
  true.

- not **--** If a value is true, the return is false and vice versa.

#### If statement

To write an if statement in Python, we use the following syntax:

```text
if condition:
  #Code goes here
else:
  #Code goes here
```

#### Elif Statement

To write an elif statement, referred to as else if, we use the following
syntax:

```text
if condition_1:
  # do something
elif condition_2:
  # do something else
else:
  # do another thing
```

#### Syntax Errors

SyntaxError means there is something wrong with the way your program is
written.

#### Name Errors

The Python interpreter reports a NameError when it detects a variable
that is unknown.

#### Type Errors

A TypeError is reported by the Python interpreter when an operation is
applied to a variable of an inappropriate type.

### Lists

#### What is a list?

A list is a data structure which allows us to store a collection of data
in a sequential order.

```text
heights = [55, 63, 58, 59]
```

#### What can a list contain?

A list can contain any data type:

```text
mixed_list = ["Mia", 13, 13.5, True]
```

#### List Methods

Lists have a series of built in methods that can be used to manipulate
or get data from a list.

##### Append()

The append() method adds a value to the end of a list.

1. It does not combine two lists into one.

```text
mylist = []
mylist.append(1)
```

##### Plus()

The plus() method concatenates two lists together.

```text
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
newList = list1 + list2
```

##### Remove

The remove() method removes an item with a specified value.

```text
list = ["Hello", "World"]
list.remove("Hello")
```

#### Access Elements

The location of an element is known as an index. And in Python, lists
are zero-indexed meaning the first element has an index of 0.

To access an element, we use its index in square brackets.

```text
list1[27]
```

But what about using negative index. Well, if we use the index -1, we
will get the last item in the list, -2, the second last and so on.

#### 2D-Lists

You can store lists inside of lists... listception. But how do you
access items? By starting with the outer list and working inwards:

```text
list2D[0][4]
```

#### Insert

The Python list method insert() allows us to add an element to a
specific index in a list. The insert() method takes two inputs:

1. The index you want to insert into,

1. The element you want to insert at the specific index.

    1.  It does not delete the previous value at that index but instead
        shifts it right.

```text
mylist.insert(2, "Hello")
```

#### Pop

The Python list method pop() removes and returns an element from a
specific index from the list.

```text
removedElement = mylist.pop(2)
```

If no index is used, the last element is popped off.

#### Range

The range() function takes a single input and generates numbers starting
at zero and ending at the number before the input. But this returns a
range object, not a list. So, to get a list, we need to convert it into
a list.

```text
numbers = list(range(10))
```

range() also allows us to have starting, stopping, and stepping values.

```text
numbers = list(range(1, 100, 10))
## [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
```

Its best to think of the stopping value as: "stop before this value."

#### Length

The len() function returns the length of a give list.

```text
size = len(myList)
```

#### Slicing Lists

Let us say we have the following list:

```text
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
```

But we only want letters b though to f, we can slice the list.

```text
sliced_list = letters[1:6]
```

If you just want to first n elements, we use the following:

```text
myList[:n]
```

If you want the last n elements, use:

```text
myList[-n:]
```

#### Counting

If you want to know how many times a given value appears in a list, we
can use the count() method.

```text
num_i = letters.count("i")
```

#### Sort

To sort a list, we can use the sort() method:

```text
myList.sort()
myList.sort(reverse=True)
```

sort() allows us to sort our list in reverse. Sort is a method by
sorted() is a function which returns a new sorted list.

```text
mySortedList = myList.sort()
```

#### Tuples

Tuples are just like lists but they are immutable.

```text
myTuple = (1, 2, 3, 4, 5)
```

As seen above, they are created using normal brackets. We can access
data from Tuples just like in lists.

We can extract all data from tuples:

```text
x, y, z, a, b = myTuple
```

To create a single element tuple, we need to add a trailing comma.

```text
singleTuple = (1,)
```

#### Zip

The zip() function combines two different lists together like so:

```text
names = ['Michael', 'Bob', 'Tracy']
ages = [20, 18, 19]
combinedList = list(zip(names, ages))
## [('Michael', 20), ('Bob', 18), ('Tracy', 19)]
```

This is great for for loops when you need to loop over two lists.

### Loops

#### For Loops

for loops in Python are remarkably like foreach loops in other
languages. Python simply loops over each item in a collection of data.

```text
for child in children:
  # do something with child
```

But what if se do not want to loop over a collection of data and instead
just want to loop x number of times, like a traditional for loop. To do
this, we use the range() function:

```text
for i in range(5):
  # do something
```

The above code will loop five times, but I will be 0, 1, 2, 3, and
finally 4.

#### While Loops

A while loop performs a set of instructions if a given condition is
true:

```text
while not gameOver:
  # do stuff
```

#### Infinite Loops

Infinite loops occur when a loop keeps on running and never ends.

#### Break

The break command can be used to break out of a loop even if the loop
has not finished:

```text
while True:
  break
```

#### Continue

The continue command can be used to skip to the next iteration of the
loop.

```text
for i in range(10):
  continue
```

#### Nested Loops

Nested loops are loops within loops... loopception.

```text
for y in height:
  for x in width:
    # do something
```

#### List comprehensions

Let us say we wanted to double all values in a list and return the
result in a new list. We may use a for loop but instead, we can do it in
one line:

```text
numbers = [1, 2, 3, 4, 5]
doubles = [x * 2 for x in numbers]
```

This is known as comprehension.

Comprehensions can even include conditionals:

```text
numbers = [1, 2, 3, 4, 5]
doubles = [x * 2 for x in numbers if x < 3]
```

The above example will only double and store in the numbers less than
three.

### Functions

#### Defining a Function

To define a function ins Python, we use the def keyword.

```text
def myFunction():
  # This is a function
```

#### Calling a Function

Whatever code is inside our function will not actually run until we call
our function. To call a function, we use the following command:

```text
myFunction()
```

#### Parameters and Arguments

Our functions can have parameters as seen below:

```text
def myFunction(parameter1, parameter2):
  # do something
```

When we call our function, we need to pass values to those parameters.
These values are called arguments.

```text
myFuncion(5, 3)
```

#### Types of Arguments

There are three types of arguments:

- **Positional Arguments --** Arguments that can be called by their
  position in the function definition.

- **Keyword Arguments -** Arguments that can be called by their name.

- **Default Arguments -** Arguments that are given default values.

#### Returns

Our functions can return values. This is done by using the return
keyword.

```text
return value
```

If we wanted to return multiple values, they will be returned as a
tuple.

```text
return posX, posY
```

### Python Strings

A string is a sequence of characters contained within a pair of "double
quotes" of 'single quotes.'

#### They are all Lists.

Strings are just lists meaning each character in a string can be
indexed. Not only can we index strings, but we can also slice them.

```text
string[firstIndex:lastIndex]
```

#### Concatenating Strings

We can also combine two strings via the + operator.

```text
newString = string1 + string2
```

#### String Length

We can also get the length of a string using the len() function.

#### Strings are immutable.

Strings are immutable meaning once they are created, they cannot be
changed.

#### Escape Characters

When working with strings, you will find that you want to include
characters that already have a special meaning in Python. For instance,
if we wanted to include quotes in our string:

```text
myString = "This is a \"Quote\""
```

#### Strings are iterable.

We can also use loops to iterate through each character in a string.

```text
for letter in myString:
  # do something with letter
```

#### The in Keyword

We can check if a letter or a string is inside another string by using
the in keyword.

```text
if letter in myString:
  # do something
```

#### Formatting Methods

There are three string methods that can change the casing of a string.
These are lower(), upper(), and title().

- lower() **--** returns the string with all lowercase characters.

- upper() **-** returns the string with all uppercase characters.

- title() **-** returns the string in title case, which means the first
  letter of each word is capitalized.

#### Splitting Strings

split() is performed on a string, takes one argument, and returns a list
of substrings found between. the given argument (which in the case of
split() is known as the delimited).

```text
myName = "George Madeley"
print(myName.split())
## ["George", "Madeley"]
```

#### Join

join() is the opposite of split(), it joins a list of string together
with a given delimiter.

```text
join(list_of_strings)
```

#### Strip

Stripping a string removes all whitespace characters from the beginning
an end.

```text
myName = "     George Madeley     "
print(myName.strip())
## "George Madeley"
```

You can also pass in an argument to strip() to strip a string of that
character.

#### Replace

replace() takes two arguments and replaces all instances of the first
argument in the string with the second argument.

```text
myName.replace("G", "J")
```

#### Find

find() takes a string argument and searches the string it was run on for
the given string. It then returns the first index value where that
string is located.

```text
"smooth".find("t")
```

### Modules

Python allows us to package code into files or sets of files called
modules. A module is a collection of Python declarations intended
broadly to be used as a tool. Modules are referred to as "libraries" or
"packages" -- a package is really a directory that holds a collection of
modules.

To use a module, you need the following syntax:

```text
from <module_name> import <object_name>
```

#### Modules Python Random

random allows you to generate numbers or select items at random.

```text
import random
```

- random.choice() which takes a list as an argument and returns a number
  from the list.

- random.randint() which takes two numbers as arguments and generates a
  random number between the two numbers you passed in.

#### Namespaces

Sometimes, module names are too complicated, so we assign a module a
nickname. A namespace isolates the functions, classes, and variables
defined in the module from the code in the file doing the importing.
Your local namespace is where you run your code.

```text
import <module_name> as <nick_name>
```

#### Decimals

When adding floats in Python, you must deal with floating-point
arithmetic. To avoid this, we can use the Decimal data type from the
decimal module.

```text
from decimal import Decimal
number = Decimal('0.20')
```

#### Files and Scope

Files are modules so you can give a file access to another file's
contents using the import statement.

### Dictionaries

A dictionary is an ordered set of key value pairs.

```text
menu = {"lagman": 120, "plov": 120, "borsh": 100}
```

#### Making a Dictionary

The key in a dictionary can be either a string or integer. The value can
be any data type.

#### Add a Key

To add a single key value pair to a dictionary, we can use the syntax:

```text
dictionary[key] = value
```

#### Adding Multiple Keys

If we wanted to add multiple key value pairs to a dictionary at once, we
can use the update() method.

```text
dictionary.update({
  "pantry": 22,
  "fridge": 32,
  "cabinet": 12
})
```

#### Dictionary Comprehension

Python allows you to create a dictionary using dictionary comprehension.

```text
students = {key:value for key, value in zip(names, heights)}
```

#### Safely get a Key

If we try and access a key that does not exist, we will get a KeyError.
To safely get a key without raising an error, dictionaries have a get()
method.

```text
dictionary.get("Key")
```

#### Delete a Key

To delete a key, dictionaries have the pop() method.

```text
dictionary.pop("key")
```

#### Get all Keys.

The keys() method returns a list of all the available keys in the
dictionary.

```text
dictionary.keys()
```

#### Get all Values.

The values() method returns a list of all available values in the list.

### Files

To read a file, we use the following commands:

```text
with open('filename') as varfile:
  # do something with varfile
```

When we exit out of the with code block, it automatically closes the
file for us.

#### Iterating through Lines

The read() method returns the file contents as one string. The
readlines() returns a list of each line as a string.

```text
with open('filename') as textFile:
  for line in textFile.readlines():
    print(line)
```

#### Reading a Line

The readline() pops off the first line and returns it. When there are no
more lines, an empty string in returned.

#### Writing a File

To write to a file, we must have to pass a second argument to the open()
function; w for write.

```text
with open('filename', 'w') as textFile:
  textFile.write('This is a test.
')
```

If a file with the same name already exists, the original file will be
wiped.

#### Appending to a File

To append text to a file, we use the argument a.

```text
with open('filename', 'a') as textFile:
  textFile.write('This is a new line.
')
```

#### With keyword

The with keyword invokes something called a context manager for the file
that we are calling open() on. This context manager is responsible for
opening and closing the file.

Leaving a file connection open unnecessarily can affect performance or
impact other programs on your computer.

#### CSV

CSV files are an example of a text file that impose structure to their
data. CSV stands for Comma-Separated Values and are usually the way that
data from spreadsheet software is exported into a portable format.

#### Reading a CSV

In Python, we can convert CSV data into a dictionary using the CSV
library's DictReader object.

```text
import csv
listOfEmailAddresses = []
with open('users.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    listOfEmailAddresses.append(row['email'])
```

#### Other CSV Files

Not all CSV files use commas to separate their values, some use tabs, or
semi-colons. How can we accommodate this? The DictReader function
provides a delimiter argument that allows us to set the delimiter of the
read file.

```text
import csv
listOfEmailAddresses = []
with open('users.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile, delimite=':')
  for row in reader:
    listOfEmailAddresses.append(row['email'])
```

#### Writing a CSV File

To write data to a CSV file, we need a list of dictionaries where each
dictionary has the same keys.

```text
import csv
with open('output.csv', 'w') as outputCSV:
  fields = ['name', 'age', 'job']
  writer = csv.DictWriter(outputCSV, fieldnames=fields)
  writer.writeheader()
  for item in myList:
    writer.writerow(item)
```

#### Reading a JSON file

To read JSON files, we use the inbuilt JSON library.

```text
import json
with open('JSONFile.json') as JSONFile:
  jsonData = json.load(JSONFile)
```

#### Writing a JSON File

To write data to a JSON file, you need to store the data in a
dictionary.

```text
import json
with open('output.json', 'w') as JSONFile:
  json.dump({'foo': 'bar'}, JSONFile)
```

### Classes

#### Types

We can get a variable's type by using the type() function.

#### Class

A class is a template for a data type. We define a class using the class
keyword.

```text
class my_class:
  pass
```

#### Instantiation

A class must be instantiated before it can do anything. We can create an
instance of our class using the following code:

```text
my_instance = my_class()
```

#### Object Oriented Programming

A class instance is also called an object. We can use the type() to get
the type of our object.

```text
print(type(my_instance))
## <class '__main__.my_class'>
```

1. \_\_main\_\_ means "the current file we are running."

#### Class Variables

A class variable is a variable that is the same for every instance of
the class. We can access all our objects data using:

```text
objectName.dataName
```

These variables are called attributes.

#### Methods

Methods are functions that are part of a class.

The first argument of a method is the class. This is done by using the
self keyword.

```text
class my_class:
  my_attribute = 65

  def my_method(self):
  print(self.my_attribute)
```

#### Methods with Arguments

Methods can have arguments just like functions, but they must come after
the self keyword.

#### Constructors

In Python, there are several methods termed magic or dunder methods
which perform special tasks.

The \_\_init\_\_() method initialises a newly created object. This is
called every time an object of that class is initialized.

This method is also termed as the constructor.

```text
class my_class:
  def __init__(self):
  pass
```

Any additional arguments \_\_init\_\_() has will be passed into the
class on initialisation.

```text
my_instance = my_class(argument1, ...)
```

#### Attribute Functions

hasattr() is a function which returns true if a given object has an
attribute with a given name.

```text
hasattr(object, "attribute_name")
```

The attribute name must be in quotes.

getattr() is a function which gets an objects attribute.

```text
getattr(object, "attribute_name", defualt_value)
```

The value of default is returned if the attribute does not exist.

#### Self

The self keyword refers to the object and not the class.

#### Dir

The dir can be used to get all an object's attributes as a list.

#### String Representations

When debugging your code, all your objects will have complicated names
like:

```text
<"__main__.my_class object at 0x7f8e9d9b6a90">
```

This is confusing but can be solved by using the \_\_repr\_\_() method.
This dunder method must have one argument, self, and must return a
string.

```text
class my_class:
  def __repr__(self):
  return self.name
```

## Intermediate Python

### Functional Arguments

A mutable object in Python refers to various containers that are
intended to be changed. Lists, Dictionaries, and Sets are all mutable,
but tuples, strings, and integers are not. Instead of changing their
value, a new one is created instead.

Default parameter values are evaluated left to right when the function
definition is executed. This means that the express is evaluated once,
when the function is defined, and the same "pre-computed" value is used
for each call. Meaning if you use an array as a default value, the
function will use the same array, *not* create a new one, when a value
is not provided.

Therefore, mutable types as default parameter values are always the same
object in every call of that function. Meaning, despite having a default
mutable argument, the operations will be performed on the same object.

```text
def add_grade(student, grade):
  student['grades'].append(grade)
  print(student['grades'])

def create_student(name, age, grades=[]):
  return {
  'name': name,
  'age': age,
  'grades': grades
  }

Chrisley = create_student('Chrisley', 15)
Dallas = create_student('Dallas', 16)

add_grade(Chrisley, 90)
add_grade(Dallas, 100)

## [90]
## [90, 100]
```

The output of the code, seen above, is because Chrisley and Dallas share
the same list object due to the default argument.

To solve this, use the None keyword.

```text
def create_student(name, age, grades=None):
  if grades is None:
  grades = []
  ...
```

#### Function Arguments

- **Positional Arguments --** arguments that are called by their
  position in the function definition.

- **Keyword Arguments --** arguments that are called by their name.

- **Default Arguments --** arguments that are given default values.

#### Variable Number of Arguments

There is an operator called the unpacking operator; \*. The unpacking
operator allows us to give our functions a variable number of arguments
by performing what is known as positional argument packing.

```text
def my_func(*args):
  print(args)
```

The unpacking operator is included in the argument but admitted in the
code black. When omitted, all the passed argument values will be stored
in a tuple.

We can also use this with positional arguments if they come first.

```text
def my_func(arg1, arg2, *args):
  ...
```

#### Variable Number of Keyword Arguments

To have a variable number of keyword arguments, we use a double
unpacking operator; \*\*. When there are omitted, the argument returns a
dictionary.

```text
def my_func(**kwargs):
  ...

my_func(this_Arg="hello", anything_goes=101)
```

Again, we can use this with positional arguments if the positional
arguments come first.

#### All Together

If we want to use them all together, we must define the arguments in
this order:

1)  Standard Positional Arguments

2)  Variable Number of Arguments: \*args

3)  Standard Keywork Arguments

4)  Variable Number of Keywork Arguments: \*\*kwargs

#### More Unpacking

We can use \* and \*\* to unpack lists and dictionaries respectfully:

```text
my_args = [3, 6, 9]

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(*my_args)
```

### Namespaces and Scopes

A namespace is a collection of name and objects that they reference. In
Python, namespaces are represented as dictionaries where the key is the
object name, and the value is the object itself.

#### Built in Namespaces

There are four main types of namespaces in Python, the first being
built-in namespace.

The built-in namespace covers all the keywords Python uses for functions
and others. To get a list of built-in names, use the following command:

```text
print(dir(__builtins__))
```

#### Global Namespace

The global namespace exists one level below the built-in namespace and
covers all the non-nested names we use. The global namespace only exists
if the interpreter is active.

#### Local Namespace

A local namespace is only active inside a code block like a function.
One cannot call a name from a local namespace outside of said namespace.

#### Enclosing Namespace

Enclosing namespaces are created specifically when we work with nested
functions.

#### Modifying Scope Behaviour

We can access enclosed scopes within our local scope, but we cannot
change the value without using the keyword nonlocal.

```text
def enclosing_function():
  var = 'value'
  def nested_function():
  nonlocal var
  var = 'new value'
  nested_function
  print(var)
  # prints 'new value'
```

Like nonlocal, Python provides a keyword to modify global scopes;
global.

### Functions Deep Dive

#### Lambda Functions

In Python, a lambda function is a one-line shorthand for functions.

```text
def add_two(num):
  return num + 2

add_two = lambda num: num + 2
```

Lambda functions are great for filtering.

```text
check_if_grade_pass =lambda grade: 'Passed!' if grade >= 70 else 'Failed!'
```

```text
check_if_grade_pass =lambda grade: 'Passed!' if grade >= 70 else 'Failed!'
```

#### Higher Order Functions

In Python, all functions are classified as first-class objects. This
means they have four important characteristics:

- Can be stored as variables.

- Can be passed as arguments to a function.

- Can be returned by a function.

- Can be stored in data structures.

#### Map

The map() function accepts two arguments: a function and an iterable
variable. The map() function calls the passed in function on every value
within the iterable variable and returns it:

```text
list1 = [3, 6, 9]
map1 = map(lambda x: x * 2, list1)
print(list(map1))
## prints [6, 12, 18]
```

#### Filter

filter(), just like map(), takes in two arguments: a function and an
iterable variable. The function calls the passed in function on all
values within the iterable variable. It then returns every value in
which true was the outcome.

```text
list1 = [3, 6, 9]
filter1 = filter(lambda x: x % 2 == 1)
print(list(filter1))
## prints [3, 9]
```

#### Reduce

reduce() combines all values into one.

```text
from functools import reduce
list1 = [3, 6, 9]
reduce1 = reduce(lambda x, y: x * y, list1)
print(reduce1)
## prints 3*6*9
```

### Object Oriented Programming

#### Inheritance

Inheritance allows classes to share common methods and attributes. A
child can inherit methods from a parent class but children classes
cannot share methods not from a parent class and a parent cannot access
methods defined in its children.

```text
class Animal:
  def eat(self):
  ...

class Dog(Animal):
  def bark(self):
  ...
```

In the above example, Dog has access to eat() but Animal does not have
access to bark().

#### Overriding Methods

An overridden method in a subclass is one that has the same definition
as the parent class but contains different behaviour.

```text
class Animal:
  def make_noise(self):
  print("Squeak")

class Dog(Animal):
  def make_noise(self):
  print("Woof")
```

#### Super()

super() gives us a proxy object. With this proxy object, we can invoke
the method of an objects parent class.

```text
class Animal:
  def __init__(self):
  ...

class Dog(Animal):
  def __init__(self):
  super().__init__(self)
```

The above example will call the parent definition of \_\_init\_\_().

#### Polymorphism

Polymorphism is the ability to apply an identical operation onto
different types of objects.

```text
class Cat:
  def make_noise(self):
  ...

class Dog(Animal):
  def make_noise(self):
  ...
```

#### Dunder Methods

The name dunder method is derived from the **d**ouble **under**score
that surround the name of each method.

Every class in Python has access to these methods.

```text
class my_class:
  def __add__(self, other):
  ...
```

#### Abstraction

Abstraction helps with the design of code by defining necessary
behaviours to be implemented within a class structure. Abstraction also
helps avoid leaving out or overlapping class functionality as class
hierarchies get larger.

- Abstraction does not allow you to initialise an abstract class.

- If an abstract class contains an abstract method, all child classes
  need to implement that method.

```text
from ABC import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name):
  self.name = name

  @abstractmethod
  def make_sound(self):
  pass
```

#### Encapsulation

Encapsulation is the process of making methods and data hidden inside
the object they relate to, i.e., private/public.

Python does not implement encapsulation; it does however have the
following conventions:

- **Public --** no underscore,

- **Protected --** one underscore,

- **Private --** two underscores.

#### Getters, Setters, and Deleters

Getters, setters, and deleters allow the programmer to define how the
user can interact with public, protected, and private methods.

#### The property() function

In python, we usually write our own getters, setters, and delete
functions and call them when required however, the property() function
accepts each method (plus a docstring) as its arguments and allows those
methods to be called automatically.

```text
weight = property(
  getWeight,
  setWeight,
  delWeight, 
  "I'm the 'weight' property."
)
```

Now, when we modify weight, it will call its corresponding setter,
getter, and delete functions.

#### The \@Property Decorator

Alternatively, we can define getters, setters, and deleters using the @
property decorator.

```text
@property
def weight(self):
  """ DocString """
  return self.__weight

@weight.setter
def weight(self, value):
  ...

@weight.deleter
def weight(self):
  ...
```

### Unit Testing

#### Exceptions

Exceptions are runtime errors because during program execution, only
when the offending code is reached.

A traceback is a summary that includes the exception type, a message,
and the series of function calls preceding the exception, along with
file names and line numbers.

#### Built in Exceptions

Exceptions are objects just like anything else. Most exceptions inherit
directly from a class called Exception.

#### Raising Exceptions

We can throw an exception at anytime using the raise keyword, even when
python would not normally throw it.

We can either call the class by itself or call a constructor and provide
a specific error message.

```text
raise NameError
## or
raise NameError("Custom message")
```

When no built-in exceptions make sense for the type of error our program
might experience, it might be better to use a generic exception with a
specific message.

```text
raise Exception('Custom message')
```

Use the best exception that provides the best explanation for the
expected error for both the user and anyone that will read the code.

#### Try/except

It is possible for programs to continue executing even after
encountering an exception. This process is known as exception handling
and is accomplished by using try and except clauses.

The code block within the try clause is run. If no error occurs, the
program skips the except clause and accompanying code block. However, if
an error does occur, the program stops running the try clause code block
and begins running then except code block.

#### Catching Specific Exceptions

It is best practice to catch a specific error within the except clause.

```text
try:
  ...
except NameError:
  ...
```

Python also allows us to capture the exception object using the as
keyword. The exception object hosts information about the specific error
that occurred.

```text
try:
  ...
except NameError as objectError:
  ...
```

#### Handling Multiple Exceptions

We can chain multiple except clauses together to handle other errors.

```text
try:
  ...
except NameError:
  ...
except ValueError:
  ...
```

#### The Ese Clause

We can use the else clause if we want to run a block of code only if no
errors have occurred.

#### The Finally Clause

We can use the finally clause to run a block of code regardless of
whether an error occurred or not.

#### User Defined Exceptions

User-defined exceptions are exceptions that we create to allow for
better readability in our program errors.

```text
class CustomError(Exception):
  pass
```

1. Best practise to end the name with Error.

Python also allows us to add our own methods to the custom Exception
class:

```text
class LocationTooFarErrror(Exception):
  def __init__(self, distance):
  self.distance = distance

  def __str__(self):
  return "Location too far: {}".format(self.distance)
```

#### The Assert Statement

As assert statement can be used to test that a condition is met. If the
condition evaluates to false, an AssertionError is raised with an
optional error message.

```text
result = 10 * 20
assert result == 200, 'Custom error message'
```

#### Unit Tests

A unit test validates a single behaviour and will make sure all the
units of a program are functioning properly.

To test a single function, we might create several test cases. A test
case validates that a specific set of inputs produces an expected output
for the unit we are trying to test.

#### Pythons Unittest Framework

The unittest module provides us with a test runner. A test runner is a
component that collects and executes tests and then provides results to
the user. The framework also provides many other tools for test
grouping, setup, teardown, skipping, and other features.

First, we must declare a class which inherits from unittest TestCase
class.

```text
import unittest

class TestFunctionName(unittest.TestCase):
  def test_1(self):
  pass
  
  def test_2(self):
  pass
```

We then store our unit tests as methods in this class.

Each method name must begin with the word test.

To call the test, we simply call unittest.main().

#### Equality and Membership

The framework relies on built-in assert methods instead of assert
statements to track results without raising exceptions.

- AssertEqual() -- takes two values as arguments and checks that they
  are equal.

- AssertIn() -- takes two arguments. It checks that the first argument
  is found in the second argument, which should be a container.

- AssertTrue() -- takes a single argument and checks if that argument is
  true.

#### Quantitative Methods

- AssertLess() -- takes two arguments and checks if the first argument
  is less than the second argument.

- AssertAlmostEqual() -- takes two arguments and checks that their
  difference, when rounded to seven decimal places, is zero. In other
  words, they are almost equal.

#### Exception and Warning Methods

- AssertRaises() -- takes and exception type as its first argument, a
  function reference as its second, and an arbitrary number of arguments
  as the rest. Runs the passed in function and checks if the provided
  exception was raised. If that exception was not raised or no exception
  was raised, the test fails.

- AssertWarns() -- takes a warning type as its fist argument, a function
  reference as its second, and an arbitrary number of values as the
  rest. Runs the passed in function and checks that the warning occurs.

#### Parameterizing Tests

By parameterizing tests, we can leverage the functionality of a single
test to get a large amount of coverage of different inputs.

```text
def test_times_ten(self):
  for num in [0, 1000000, -10]:
  with self.subTest():
    expectedResult = num * 10
    message = 'Some String'
    self.assertEqual(
        times_ten(num),
        expectedResult,
        message
      )
```

By using subTest(), each iteration of our loop is treated as an
individual test.

#### Test Fixtures

A test fixture is a mechanism for ensuring proper test setup and test
teardown. Test fixtures guarantee that our tests are running in
predictable conditions, and thus the results are dependable.

A method named setup() runs before each test case in the class.
Similarly, a method named teardown() gets called after each test case.

A method named setupClass() runs only once at the start of the tests
group and tearDownClass() runs once at the end.

```text
@classmethod
def setupClass(cls):
  ...
```

SetupClass() and tearDownClass() both need the \@classmethod decorator
and the cls argument instead of self.

#### Skipping Tests

The unittest framework provides two different ways to skip tests:

- The \@unittest.skip decorator.

- The skipTest() method.

```text
@unittest.skipUnless(condition, message)
def test_1(self):
  ...

@unittest.skipIf(condition, message)
def test_2(self):
  ...
```

#### Expected Failures

Sometimes, we want a test to fail but we do not want it to cloud our
results. To set up a test to have an expected failure, we can use the
\@expectedFailure decorator.

```text
@unittest.expectedFailure
def test_broken_feature(self):
  ...
```

### Iterators and Generators

An iterable object is an object that is capable of being looped through
one element at a time.

#### \_\_iter\_\_() and iter()

When a for loop loops through a dictionary it first needs to run that
object into an iterator object.

An iterator object is a special object that represents a stream of data
on which we can operate. This is done like so:

```text
dog_food_iterator = iter(dog_foods)
```

When we use the iter() function on our iterable object, it is calling
the method \_\_iter\_\_() defined within the iterable. This method
simply returns the iterator object.

#### \_\_next\_\_() and next()

How does the for loop know which item to fetch next? It does this by
calling the \_\_next\_\_() method.

The iterator object has a method called \_\_next\_\_() which returns the
iterators next value. We can also use the built in function next()
instead.

The \_\_next\_\_() method will raise an exception called StopIteration
when all items have been iterated through.

```text
dog_food_iterator = iter(dog_foods)
next_food = next(dog_food_iterator)
```

#### Custom Iterators

If we desire to create our won custom iterator class, we must implement
the iterator protocol, meaning we need to have a class that defines at
minimum the \_\_iter\_\_() and \_\_next\_\_() methods.

- The \_\_iter\_\_() method must always return the iterator object
  itself.

- The \_\_next\_\_() method must either return the next value or raise
  the StopIteration exception.

```text
class FishInventory:
  def __init__(self, fishList):
  self.fishList = fishList

  def __iter__(self):
  self.index = 0
  return self
  
  def __next__(self):
  if self.index >= len(self.fishList):
    raise StopIteration
  fish = self.fishList[self.index]
  self.index += 1
  return fish
```

#### Itertools

Python offers a convient, built-in module named itertools that provides
the ability to create complex iterator methods. There are three
categories to itertools iterators:

- **Infinite --** Infinite iterators will repeat an infinite number of
  times. They will not raise a StopIteration exception and will require
  some type of stop condition to exit from.

- **Finite --** Finite iterators are terminated by the input iterable(s)
  sequence length. This means the smallest length iterable used in a
  finite iterator will terminate the iterator.

- **Combinatoric --** Combinatoric iterators are iterators that are
  combinational, where mathematical functions are performed on the input
  iterables.

#### Infinite Iterators: Count

A useful itertool that is an infinite iterator is the count() itertool.
This infinite iterator will count from a first value until we provide
some type of stop condition.

```text
from itertools import count
count(start, [step])
```

#### Finite Iterators: Chain

A useful itertool that is a finite iterator is the chain() tool. This
finite iterator will take in one or more iterables and combine them into
a single iterator.

```text
from itertools import chain
chain(*iterables)
```

#### Combinatoric Iterator: Combinations

The combinations() itertool function will produce an iterator of tuples
that contain combinations of all elements in the input.

```text
from itertools import combinations
combinations(iterable, r)
```

The variable r represents the length of each combination tuple.

```text
from itertools import combinations
even = [2, 4, 6]
even_combinations = combinations(even, 2)
print(even_combinations)
## [(2, 4), (2, 6), (4, 6)]
```

#### Generators

A generator allows for the creation of iterators without having to
implement \_\_iter\_\_() and \_\_next\_\_() methods. There are two types
of generators in Python:

- Generator functions,

- Generator expressions.

#### Yield vs Return

Any code that is written after a yield expression will execute on the
next iteration of the iterator. Code written after a return statement
will not execute.

```text
def course_generator():
  yield 'Computer Science'
  yield 'Art'
  yield 'Engineering'

courses = course_generator()
for course in courses:
  print(course)
```

yield expressions will suspend the execution of the function and
preserve any local variables that exist within the function.

#### Next() and StopIteration

To return the next value from a generator object, we can use Pythons
built-in function next() which will cause the generator function to
resume its execution until the next yield express is found. If there are
no more yield expressions remaining, a StopIteration is raised.

#### Generator Expressions

Generator expressions allow for a clean, single-line definition and
creation of an iterator,

```text
a_generator = (i * i for i in range(4))
```

#### Send()

The .send() method allows us to send a value to a generator using the
yield expression. If you assign yield to a variable, the argument passed
to the .send() method will be assigned to that variable.

```text
def count_generator():
  while True:
  n = yield
  print(n)

my_generator = count_generator()
next(my_generator)
## prints None
my_generator.send(3)
## prints 3
```

The .send() method can control the value of the generator when a second
variable is introduced. One variable holds the iteration value and the
other holds the value passed through yield.

```text
def count_generator():
  count = 0
  while True:
  # returns count if a value for n is not provided
  n = yield count
  if n is not None:
    count = n
  count += 1
  print(n)

my_generator = count_generator()
print(next(my_generator)) # 0
print(next(my_generator)) # 1
print(my_generator.send(3)) # 4
print(next(my_generator)) # 5
```

#### Throw

.throw() provides the ability to throw an exception inside the generator
from the caller point.

```text
my_generator.throw(ValueError, "Custom Message")
```

#### Close

.close() is used to terminate a generator early. This works by raising a
GeneratorExit exception inside the generator function.

We can handle the exception by putting the yield expression inside a try
block.

#### Connecting Generators

To connect generators, we use the yield from statement.

```text
def cs_courses():
  yield 'Computerr Science'
  yield 'Artificial Intelligence'

def art_courses():
  yield 'Intro to Art'
  yield 'Selection Mediums'

def all_courses():
  yield from cs_courses()
  yield from art_courses()

combined_generator = all_courses()
```

#### Generator Pipelines

Generator pipelines allow us to use multiple generators to perform a
series of operations all within one expression. To pipeline generators,
the output of one generator can be the input of another generator
function.

```text
def number_generator():
  i = 0
  while True:
  yield i += 1

def even_number_generator(numbers)
  for n in numbers:
  if n % 2 == 0:
    yield n

even_numbers = even_number_generator(number_generator())
```

### Specialized Collections

#### Introduction to Sets

A set is a group of elements that are un-ordered and do not contain
duplicates.

```text
music_different = {
  70,
  'music times',
  'categories',
  True,
  48.7
}
```

#### Frozen Sets

A frozen set is just like a normal set, but it cannot be modified.

```text
frozen_music_different = frozenset(music_different)
```

#### Adding to a Set

The .add() method can be used to add an element to a set.

The .update() method can add multiple items to a set.

#### Removing from a set

The .remove() method searches for an element and removes it if it
exists, otherwise, a KeyError is thrown.

The .discard() method works the same way but does not throw an exception
if an element is not present.

#### Finding elements in a set

We cannot index elements; however, we can check is an item is present in
a set by using the in keyword.

#### Set Operations

![A blue circle with black background Description automatically generated](media/image136.png)

##### Union

We can combine or union to sets by using the .union() method which will
return a new set. We can also use \| instead of .union().

![A blue circle with black background Description automatically generated with medium confidence](media/image136.png)

##### Intersection

We can see what two sets have in common by using .intersection() method
or the & operator. Both return a new set.

![A blue circle with black background Description automatically generated](media/image136.png)

##### Difference

We can find all the items of one set that are not in the other by using
the .difference() method or the - operator.

![A blue circle with black background Description automatically generated](media/image136.png)

##### Symmetric Difference

We can find all elements that are not in either set by using the
.symmetric_difference() method or the \^ operator.Specialized Containers

Python has more containers than just lists, tuples, dictionaries, and
sets. To get access to these classes, we need to import the containers
module.

![](C:\Users\George\Documents\Personal\Coding\Python\Notes Converter\output\GM01101 - Python/media/image137.emf)

#### Dequeue

Dequeue is like a list bust elements in the middle cannot be accessed.
You can only append and pop elements from the front and/or back of the
deque.

#### Named Tuple

A named tuple is like an immutable dictionary.

![](C:\Users\George\Documents\Personal\Coding\Python\Notes Converter\output\GM01101 - Python/media/image138.emf)

What is going on? We create a subclass of named tuple called ActorData
with a list of field name. like column headings in a database. We then
create an instance of the ActorData class by passing in the values we
want stored. We can then access the data using the field names.

#### Default Dict

When using dictionaries and we try to access an element that does not
exist, we get a KeyError. Default dict is just like a dictionary but
instead of throwing a keyError, it just returns a default value.

![](C:\Users\George\Documents\Personal\Coding\Python\Notes Converter\output\GM01101 - Python/media/image139.emf)

We can also create a default dict from an already existing dictionary:

```text
import containers
```

#### Counter

The counter() function accepts a list and counts how many times each
item appears in the list. It returns a dictionary where each key is each
item, and the values are how many times they occurred.

#### User Dict

The UserDict container wrapper allows us to create our own version of a
dictionary.

```text
from collections import namedtuple

ActorData = namedtuple('ActorData', [   'name',   'birth',   'movie' ])
actor_data = ActorData(
  'Leonardo Dicaprio',
  1974,
  'Titantic'
)
print(actor_data.name)
## Leonardo Dicaprio
```

To create an instance of this class, you need to pass in an already
created dictionary into the constructor.

#### User List

The UserList wrapper container lets us create our own list. It has a
property self.data which allows us to access our own data.

```text
from collections import defaultdict
validate_prices = defaultdict(lambda: 'No price assigned')
```

The UserString wrapper container lets us create our own string. We can
access the string using self.data.

```text
my_defaultdict.update(my_dict)
```

### Resource Management

A context manager is an object that takes care of the assigning and
releasing of resources.

The with statement is a good example of a context manager.

#### Class Based Context Managers

The class-based approach of writing context managers requires explicitly
defining and implementing the following methods inside of a class.

- \_\_enter\_\_():

  - Allows for setup of context managers,

  - Begins the runtime context; the period for which our script runs.

- \_\_exit\_\_():

  - Ensures the breakdown of the context manager.

```text
from collections import UserDict

class CustomDict(UserDict):
  def display_info(self):
  # create new methods...
  ...
  def clear(self):
  # ... and override old ones.
  ...
  super().clear()
```

The code will execute in the following order:

Init -\> enter -\> with block -\> exit

#### Handling Exceptions

The \_\_exit\_\_() method has three required arguments in addition to
self.

- **An exception type:** which indicates the class of exception.

- **An exception value:** the actual value of error.

- **A traceback:** a report detailing the sequence of steps that caused
  the error and the details needed to fix the error.

If we want to throw an error when an error occurs, we can either return
false or do nothing if we want to suppress an error, we can return True.

#### Context Library

The context library module allows for the creation of a context manager
with the use of a generator function, and the context library decorator
\@contextmanager.

```text
class CustomList(UserList):
  ...
```

With this, we can sue the except clause to handle errors.

### Regular Expressions

#### Introduction to Regular Expression

A regular expression is a special sequence of characters that describe a
pattern of text that should be found, or matched, in a string or
document. By matching text, we can identify how often and where certain
pieces of text occur, as well as can replace or update these pieces of
text if needed.

#### Literals

The simplest text we can match with regular expressions are literals.
This is where our regular expression contains the exact text that we
want to match. The regex a, for example, will match the text a, and the
regex bananas will match the text bananas.

We can additionally match just part of a piece of text. Perhaps we are
searching a document to see if the word monkey occurs, since we love
monkeys. We could use the regex monkey to match monkey in the piece of
text The monkeys like to eat bananas.

Regular expressions operate by moving character by character, from left
to right, through a piece of text. When the regular expression finds a
character that matches the first piece of the expression, it looks to
find a continuous sequence of matching characters.

#### Alternation

Alternation, performed in regular expressions with the pipe symbol, \|,
allows us to match either the characters preceding the \| OR the
characters after the \|. The regex baboons\|gorillas will match baboons
in the text I love baboons but will also match gorillas in the text I
love gorillas.

#### Character Sets

Character sets, denoted by a pair of brackets \[\], let us match one
character from a series of characters, allowing for matches with
incorrect or different spellings.

The regex con\[sc\]en\[sc\]us will match consensus, the correct spelling
of the word, but also match the following three incorrect spellings:
concensus, consencus, and concencus. The letters inside the first
brackets, s, and c, are the different possibilities for the character
that comes after con and before en. Similarly for the second brackets, s
and c are the different character possibilities to come after en and
before us.

Thus, the regex \[cat\] will match the characters c, a, or t, but not
the text cat.

Placed at the front of a character set, the \^ negates the set, matching
any character that is not stated. These are called negated character
sets. Thus, the regex \[\^cat\] will match any character that is not c,
a, or t, and would completely match each character d, o, or g.

#### Wild for Wildcards

Wildcards will match any single character (letter, number, symbol, or
whitespace) in a piece of text. They are useful when we do not care
about the specific value of a character, but only that a character
exists!

Let us say we want to match any 9-character piece of text. The regex
\...\...\... will completely match orangutan and marsupial! Similarly,
the regex I ate . bananas will completely match both I ate 3 bananas,
and I ate 8 bananas!

What happens if we want to match an actual period, .? We can use the
escape character, \\, to escape the wildcard functionality of the . and
match an actual period. The regex Howler monkeys are really lazy\\. will
completely match the text Howler monkeys are really lazy..

#### Ranges

Ranges allow us to specify a range of characters in which we can make a
match without having to type out each individual character. The regex
\[abc\], which would match any character a, b, or c, is equivalent to
regex range \[a-c\]. The - character allows us to specify that we are
interested in matching a range of characters.

With ranges we can match any single capital letter with the regex
\[A-Z\], lowercase letter with the regex \[a-z\], any digit with the
regex \[0-9\]. We can even have multiple ranges in the same character
set! To match any single capital or lowercase alphabetical character, we
can use the regex \[A-Za-z\].

#### Shorthand Character Classes

Shorthand character classes represent common ranges, and they make
writing regular expressions much simpler. These shorthand classes
include:

- \\w: the "word character" class represents the regex range
  \[A-Za-z0-9\_\], and it matches a single uppercase character,
  lowercase character, digit, or underscore

- \\d: the "digit character" class represents the regex range \[0-9\],
  and it matches a single digit character

- \\s: the "whitespace character" class represents the regex range \[
  \\t\\r\\n\\f\\v\], matching a single space, tab, carriage return, line
  break, form feed, or vertical tab

For example, the regex \\d\\s\\w\\w\\w\\w\\w\\w\\w matches a digit
character, followed by a whitespace character, followed by 7-word
characters. Thus, the regex completely matches the text 3 monkeys.

In addition to the shorthand character classes \\w, \\d, and \\s, we
also have access to the negated shorthand character classes! These
shorthand's will match any character that is NOT in the regular
shorthand classes. These negated shorthand classes include:

- \\W: the "non-word character" class represents the regex range
  \[\^A-Za-z0-9\_\], matching any character that is not included in the
  range represented by \\w

- \\D: the "non-digit character" class represents the regex range
  \[\^0-9\], matching any character that is not included in the range
  represented by \\d

- \\S: the "non-whitespace character" class represents the regex range
  \[\^ \\t\\r\\n\\f\\v\], matching any character that is not included in
  the range represented by \\s

#### Grouping

Grouping, denoted with the open parenthesis ( and the closing
parenthesis ), lets us group parts of a regular expression together, and
allows us to limit alternation to part of the regex.

The regex I love (baboons\|gorillas) will match the text I love and then
match either baboons or gorillas, as the grouping limits the reach of
the \| to the text within the parentheses.

These groups are also called capture groups, as they have the power to
select, or capture, a substring from our matched text.

#### Quantifiers -- Fixed

Fixed quantifiers, denoted with curly braces {}, let us indicate the
exact quantity of a character we wish to match, or allow us to provide a
quantity range to match on.

- \\w{3} will match exactly 3-word characters

- \\w{4,7} will match at minimum 4-word characters and at maximum 7-word
  characters

An important note is that quantifiers are greedy. This means that they
will match the greatest quantity of characters they possibly can.

For example, the regex mo{2,4} will match the text moooo in the string
moooo, and not return a match of moo, or mooo. This is because the fixed
quantifier wants to match the largest number of os as possible, which is
4 in the string moooo.

#### Quantifiers -- Optional

Optional quantifiers, indicated by the question mark ?, allow us to
indicate a character in a regex is optional, or can appear either 0
times or 1 time.

For example, the regex humou?r matches the characters humo, then either
0 occurrences or 1 occurrence of the letter u, and finally the letter r.
Note the ? only applies to the character directly before it.

#### Quantifiers -- 0 or More, 1 or More

The Kleene star, denoted with the asterisk \*, is also a quantifier, and
matches the preceding character 0 or more times. This means that the
character does not need to appear, can appear once, or can appear many
times.

The regex meo\*w will match the characters me, followed by 0 or more os,
followed by a w. Thus, the regex will match mew, meow, meooow, and
meoooooooooooow.

Another useful quantifier is the Kleene plus, denoted by the plus +,
which matches the preceding character 1 or more times.

The regex meo+w will match the characters me, followed by 1 or more os,
followed by a w. Thus, the regex will match meow, meooow, and
meoooooooooooow, but not match mew.

#### Anchors

The anchors hat \^ and dollar sign \$ are used to match text at the
start and the end of a string, respectively.

The regex \^Monkeys: my mortal enemy\$ will completely match the text
Monkeys: my mortal enemy but not match Spider Monkeys: my mortal enemy
in the wild or Squirrel Monkeys: my mortal enemy in the wild. The \^
ensures that the matched text begins with Monkeys, and the \$ ensures
the matched text ends with enemy.

## Advanced Python

### Logging

The logging module adds functionality to logging items in our code, so
far, we have been using the print() function to log and debug our code
which is useful but can be tedious to cleanup.

#### Create a Logger

First, we need to import the module:

```text
class CustomString(UserString):
  ...
```

The getLogger() method accepts a single parameter called name. it return
a logger object with that name. we can create multiple objects with
different names.

It is best practice to use the \_\_name\_\_ variable for the name
argument.

```text
class ContextManager:
  def __init__(self):
  ...
  def __enter__(self):
  ...
  def __exit__(self, *exc):
  ...

with ContextManager as cm:
  ...
```

we now need to inform the logger where we want our logs to go. We do
this using the StreamHandler class which takes in an argument stream.

```text
from contextlib import contextmanager

@contextmanager
def open_file_contextlib(file, mode):
  opened_file = open(file, mode)
  try:
  yield opened_file
  finally:
  opened_file.close()
```

#### Log Levels

There are six log levels:

  -----------------------------------------------------------------------
  Level       Value   Reason
  ----------- ------- ---------------------------------------------------
  NOTSET      0       

  DEBUG       10      Should be used for debugging.

  INFO        20      For general operations.

  WARNING     30      To alert us to a current or impending, unexpected
                      error or issue.

  ERROR       40      To indicate serious problems that can cause
                      functionality within the software or application to
                      break.

  CRITICAL    50      For the most severe errors to issues.
  -----------------------------------------------------------------------

#### Logging Errors and Messages

The logging module has several methods that we can use to log messages
and errors with and assigned security level.

- Debug(message)

- Warning(message)

- Critical(message)

- Info(message)

- Error(message)The logging module also provides a method log(level,
  message) that allows us to log a specific log level and message.

```text
import logging
```

#### Setting the Log Level

We can set the log level of a logger object causing it to only display
log messages with level equal to or higher than the set level.

```text
logger = logging.getLogger(__name__)
```

#### Logging to a File

To write logs to a saved file, we can use the logging module class
FileHanlder(filename). We can then add this handler using the
addHanlder() method.

```text
import sys
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
```

#### Formatting the Logs

If no custom formatting is specified, Python uses the default formatting
for all log messages:

```text
logger.log(logging.INFO, "Custom Message")
```

We can create our own custom formatter object using the logging module's
Formatter class.

```text
logger.setLevel(logging.DEBUG)
```

#### Using Basic Config

The basicConfig() method allows for the basic configuration of the
logger object by configuring the log level, any handlers, log message
formatting

```text
file_handler = logging.FileHandler("my-program.log")
logger.addHandler(file_handler)
```

### Functional Programming

Functional programming is the programming paradigm like Object Oriented
Programming but instead of objects, we use functions.

#### Determine vs Imperative.

Imperative programming would be equivalent to making a cup of coffee
whilst declarative is you going to a Barista and ordering a cup of
coffee.

- Object Oriented Programming is imperative,

- Functional programming is declarative.

#### Passing in functions

As you know, we can pass in functions as arguments to other functions. A
great method is to declare the argument function with the other
functions parathesis using lambda.

Combining this with built-in functions like map(), reduce(), and
filter() can be highly effective.

```text
%(levelname)s:%(name)s:%(message)s
```

The function above simply sums all numbers in nums that are divisible by
three.

### Database Operations

Using the module sqlite3, we can create, read, update, and delete the
data in the SQLite relational database within the Python environment.

```text
formatter = logging.Formatter("[%(asctime)s]%(levelname)s:%(name)s:%(lineno)d:%(message)s")
stream_handler.setFormetter(formatter)
```

#### Connecting to SQLite in Python

We can connect to a new or pre-existing database with the
sqlite3.connect() API. If the database does not exist, it will create a
new blank database.

```text
logging.basicConfig(
  filename = 'calcualate.log',
  level = logging.DEBUG,
  format = "[%(asctime)s]%(levelname)s:%(name)s-%(message)s"
)
```

Next, we will read a way to call SQL statements on the data within the
database. To do this, we use something called a cursor object. Using a
cursor object, we can:

- Represent a database cursor.

- Call statements to our SQLite database

- Return the data in our Python environment.

```text
s = reduce(
  lambda x,y: x + y,
  filter(lambda k: l % 3 == 0, nums)
)
```

#### Executing SQL Statements

To start an SQL command, we must attach the .execute() method to your
cursor object. We then write our SQL commands as a string into
.execute()[^1].

```text
import sqlite3
```

#### Inserting Multiple Rows

We can insert multiple rows into our database using .executeMany().

```text
connection = sqlite3.connect("first.db")
```

#### Retrieving Data

The .fetchone() method, in combination with cursor.execute(), will fetch
one row of data. Specifically, it will pull the first rows of the data
table.

```text
cursor = connection.cursor()
```

If you want to pull more than one row, you can use the fetchmany()
method. This method will return the first n set of rows.

```text
cursor.execute('''
  CREATE TABLE toys(
  id INTEGER,
  name TEXT,
  price REAL,
  type TEXT
  )
''')
```

The .fetchall() method fetches every row of data from the data table.

```text
new_students = [(102, 'Joe', '2022-05-16', 'Pass'),
        ...]
cursor.executemany('''
  INSERT INTO students VALES (?,?,?,?,?)
''', new_students)
```

#### Committing Changes and Closing Database Connection

We must use the .commit() method to save any alteration made to the
database. If we do not commit these changes, they will be lost.

```text
cursor.execute("SELECT * FROM students").fetchone()
```

Once we have committed the changes, we can then close the connection.

```text
cursor.execute("SELECT * FROM students").fetchmany()
```

### Concurrent Programming

- Concurrency is the process in which we have multiple tasks running and
  completing during overlapped time periods.

- Parallelism is the process in which we simultaneously have multiple
  takes or separate parts of the same task running using multiple CPUs.

#### Life Cycle of a Process

Processes are put into one of five states:

- **New --** the program has been started and waits to be added into
  memory to become a full process.

- **Ready --** Process is fully initialized, loaded into memory, and
  waiting to be picked up by the processor.

- **Running --** currently being executed by the processor.

- **Blocked --** the process requires a contested resource for which it
  must wait.

- **Finished --** the process has been completed.

#### Process Layout and Process Control Block

When a process is initialised, its layout within memory has four
distinct sections:

- A text section for the compiled code.

- A data section for initialised variables.

- A stack of local variables defined within functions.

- A heap for dynamic memory locations.

Processes are also initialised with a Process Control Block that is
required by the operating system for managing the process.

When one process launches another, the original enters a parent-child
relationship with the newly launched process that shares much of the
above data.

#### Introduction to Threads

A thread represents the actual sequence of processor instructions that
are actively being executed.

A thread built into the existing process is considered a kernel thread.
There are also user threads that exist solely in user space but are not
controlled by the kernel.

#### The Threading Module

To create a thread instance in Python, we use the following code:

```text
cursor.execute("SELECT * FROM students").fetchall()
```

- target -- this is the function you want to execute on the thread.

- args **--** this is the argument or set of arguments applied to the
  target function.

After creating our thread instance, we also must "start" our thread
using .start().

```text
connection.commit()
```

#### Joining a Thread

We can use .join() to tell one thread to wait for this thread to stop
before moving on. We use .join() after each thread has already started.

```text
connection.close()
```

#### The Async IO module

The aysncio module uses async/await syntax. The async keyword declares a
function as a coroutine. Coroutines are functions that may return
normally with a value or may suspend themselves internally and return a
continuation. The await keyword suspends execution of the current task
until whatever is being "await-ed" on is completed.

```text
import threading
example_thread = threading.Thread(
  target = some_function,
  args = (some_arg)
)
```

1. The syntax has been updated in Python 3:

```text
example_thread.start()
```

#### Multiple Asynchronous Tasks

If we wanted to run multiple tasks:

```text
threads = []
args = [arg1, arg2, arg3]

for arg in args:
  t = threading.Thread(
  target = target_function,
  args = (args,)
  )
  t.start()
  threads.append(t)

for thread in threads:
  thread.join()
```

Asyncio.gather() groups all our tasks together and allows them to be run
concurrently.

#### The Multiprocessing Module

To create a process in Python, we do the following:

```text
import asyncio
async def hello_async():
  print("hello")
  await asyncio.sleep(1)
  print("how are you?")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_async())
```

To start the process:

```text
asyncio.run(hello_async())
```

#### Using Multiple Processes

This is the exact same as 4.5 - Joining a Thread but instead of threads,
it's a process.

[^1]: For more commands, go to section 4 of GM01012.
