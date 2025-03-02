# GM01203: C

@ George Madeley
@ Personal Studies
@ 6/20/24

### Introduction

This is a collection of notes that I, George Madeley, took when taking
the Codecademy C++ course. I do not take ownership of the material
covered and these notes should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: Learn C++](#learn-c)

[1 - Hello World](#hello-world)

[2 - Variables](#variables)

[3 - Conditionals and Logic](#conditionals-and-logic)

[4 - Loops](#loops)

[5 - Vectors](#vectors)

[6 - Function](#function)

[7 - Classes and Objects](#classes-and-objects)

[8 - References and Pointers](#references-and-pointers)

## Learn C++

### Hello World

#### Output

```text
std::cout << "Hello World!
";
```

std::cout is the character output stream pronounced "see-out".

#### Style Guides

Both Google and Microsoft have their own C++ style guides.

#### Code → Save → Compile → Execute

When you program in C++, you mainly go through four phases during
development:

1. Code,

1. Saving,

1. Compiling,

1. Executing.

#### Compile and Execute

To compile a file, you need to type g++ followed by the file name in the
terminal and press enter:

```text
g++ hello.cpp
```

The compiler will then create a machine code file called a.out. to
execute the new machine code file, all you need to do is type ./ and the
machine code file name in the terminal:

```text
./a.out
```

To name the executable file, we use the following command.

```text
g++ hello.cpp -o hello
```

To execute this file, we use the following command:

```text
./hello
```

#### Comments

To comment code, we use the following syntax.

```text
// This is a commd
/*
  This is also a comment
*/
```

### Variables

#### Declaring Variables

To declare a variable in C++, we do the following:

```text
int score;
```

Unlike C, C++ has string types.

#### Initialising Variables

To initialise a variable:

```text
int score = 1;
```

#### Arithmetic Operators

Here are some arithmetic operators:

  -----------------------------------------------------------------------
  **Name**                            **Code**
  ----------------------------------- -----------------------------------
  Addition                            \+

  Subtraction                         \-

  Multiplication                      \*

  Division                            /

  Modulo                              \%
  -----------------------------------------------------------------------

#### Chaining

How do we print a variable to the console?

```text
std::cout << score << "
";
```

The \<\< operator concatenates strings and string representations of
variables.

#### User Input

What about when we want a user's input?

```text
std::cout << "Enter Password: ";
std:cin >> password;
```

### Conditionals and Logic

#### If Statements

The following is the syntax for an if statement:

```text
if (condition) {
  // code here
}
```

#### Relational Operators

The following are a list of relational operators:

  -----------------------------------------------------------------------
  **Name**                            **Code**
  ----------------------------------- -----------------------------------
  Equal to                            ==

  Not equal to                        !=

  Greater than                        \>

  Less than                           \<

  Greater than or equal to            \>=

  Less than or equal to               \<=
  -----------------------------------------------------------------------

#### Else Clause

The following is the syntax for an else clause:

```text
if (condition) {
  // code here
} else {
  // code here
}
```

#### Else If

The following is the syntax for an else if statement:

```text
if (condition) {
  // code here
} else if (conditon) {
  // code here
} else {
  
}
```

#### Switch Statement

The following is the syntax for a switch statement.

```text
switch (variable) {
  case 1:
  // code block
  break;
  case 2:
  // code block
  break;
  default:
  // code block
  break;
}
```

#### Logical Operators

  -----------------------------------------------------------------------
  **Name**                            **Code**
  ----------------------------------- -----------------------------------
  AND                                 &&

  OR                                  \|\|

  NOT                                 !
  -----------------------------------------------------------------------

### Loops

#### While Loop

The following is the syntax for a while loop:

```text
while (condition) {
  // code here
}
```

#### Foor loop

The following is the syntax for a for loop:

```text
for (int i = 0; i < 200; i++) {
  // code here
}
```

### Vectors

#### Introduction

A vector is a sequence of elements that you can access by index.

#### Creating a vector

The std::vector lives in the \<vector\> header so we need to import that
library:

```text
##include <vector>
```

To create a vector, the syntax is:

```text
std::vector<int> name;
```

Vectors require a type. In the example above, type int is used.

#### Initialising a Vector

To initialise a vector, we use the following syntax:

```text
std::vector<double> location = {42.651, -1.749};
```

Let's say we know the size but not the values:

```text
std::vector<double> name (2);
```

#### Index

Indexing a vector is the same as indexing a list in other languages.

```text
std::vector name = {1, 2, 3};
name[index] = value;
```

#### Adding and Removing Elements

To add elements to the back of a vector:

```text
name.push_back(value);
```

To remove elements from the back of a vector:

```text
name.pop_back();
```

1. pop_back() has no return value.

#### Size()

The .size() function returns the number of elements in the vector.

We can still use the Array data structure from C. They work exactly the
same however, they are rigid, and you won't be able to increase or
decrease their size.

### Function

#### Declare and Define

To declare a function:

```text
void function_name(arguments) {
  // code here
}
```

#### Return Types

There are a bunch of return types such as:

- int,

- float,

- double,

- char,

- std::string,

- std::vector.

#### Parameters and Arguments

When defining a function, arguments need a type:

```text
void function_name(type argument) {
  // code here
}
```

#### Multi-file Programs

Its good to split your code up between different files but how does
compiling then work:

```text
g++ main.cpp other_file.cpp
```

Even though there are functions in the other file, we still need to
declare them above main() in our main.cpp just like in C.

#### Getting a head of yourself

A good practice is to move all of the function declarations into a
header file. This file has the execution .hpp.

Then, to include a header file in your main.cpp, you need the following
command:

```text
##include "my_functioins.hpp"
```

1. You do not need to include the .hpp file in the compilation command.

#### Default arguments

To add default arguments to functions, we use the following syntax:

```text
void intro(std::string name, std::string lang = "Japanese");
```

1. We only do this in the declaration.

#### Function Overloading

In C++, two functions can have the same name as long as their argument
types are different. This allows for optional arguments.

#### Function Templates

When two functions have different types but the same body, there is a
clear solution we can use: templates!

A template is a C++ tool that allows programmers to add data types as
parameters. Templates are entirely created in header files. Templates
let us choose the type of implementation right when you call the
function.

```text
template <typename T>
void function_name(T item) {
  // code here
}
```

### Classes and Objects

#### Getting Classy with C++

We can create an empty C++ class like this in a header file:

```text
class City {
  // code here
};
```

#### Class Members

Components of a class are called class members. You can access these
members by using:

```text
object.class_member;
```

There are two types of class members: Attributes and Methods.

```text
class City {
  int population;

  public:
  void add_resident() {
    population++;
  }
};
```

We declare methods inside the class, then define the methods outside the
class in a .cpp file of the same name.

```text
int City::get_population() {
  return population;
}
```

#### Creating Objects

To create an instance of a class, we use the following format:

```text
City aaccra;
accra.population = 2000000;
accra.get_population();
```

#### Access Control: Public and Private

C++ has public and private access modifiers used to protect methods and
attributes. By default, they are private. An example can be seen above.

#### Constructors

To create a constructor, in the .cpp file for the class, we create a
constructor method:

```text
City::City(std:string new_name, int new_pop) {
  name= new_namel
  population= new_pop;
}
```

To the initialise an object with a constructor:

```text
City ankara("Ankara", 5445000);
```

#### Destructors

A destructor is a special method that handles object destruction.

```text
// in .hpp
public:
  City(std::string name, std::string pop);
  ~City();

// in .cpp
City::~City() {
  // code here
}
```

### References and Pointers

#### Introduction

A computer memory is a sequence of bytes. We can number the bytes from
zero to the last one. Each number, known as an address, represents a
location in the memory.

#### References

In C++, a reference variable is an alias for something else, that is,
another name for an already existing variable.

```text
int &num1 = num2;
```

#### Pass-By-Reference

We can pass variables into a function by reference. Be default, it is
passed by value.

```text
void swap_num(int &i, int &j) {
  // code here
}
```

Pass-by-value creates a copy, but pas-by-reference is a reference.

#### Memory Address

When & is used in a declaration, it is a reference operator. When & is
not used in a declaration, it is an address operator.

```text
int a = 3;
int &b = a;
std::cout << &a << "
"; // prints the hexidecimal address
std::cout << b << "
"; // prints 3
```

#### Pointers

Pointers, just like in C, store the address of a variable:

```text
int gum = 8;
int* ptr = &gum;
```

#### Dereference

The dereference operator \* is used to obtain the value pointed to by a
variable.

```text
int blah = *ptr;
```

- When \* is used in a declaration, it is creating a pointer,

- When \* is not used in a declaration, it is a dereference operator.

#### Null Pointers

What if we need a pointer but we do not know what to point to, we can
use a null pointer.

```text
int* ptr = nullptr;
```

Declaring a pointer without initialising its value is dangerous so
instead, we use nullPtr.

1. nullptr was added in C++11.
