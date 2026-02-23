# GM01612: TypeScript

@ George Madeley
@ Personal Studies
@ 8/3/24

## Introduction

This is a collection of notes that I, George Madeley, took when taking the Codecademy TypeScript course. I do not take ownership of the material covered and these notes should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: TypeScript](#typescript)

[1 - Types](#types)

[2 - Functions](#functions)

[3 - Complex Types](#complex-types)

[4 - Union Types](#union-types)

[5 - Advanced Type Narrowing](#advanced-type-narrowing)

[6 - Advanced Object Types](#advanced-object-types)

## TypeScript

### Types

#### Introduction to TypeScript

- TypeScript riles have the .ts extension.
- We run our code through the TypeScript transpiler.
- The transpiler often outputs a JavaScript version of our code if possible

TypeScript is a superset of JavaScript code.

The TypeScript transpiler can be used on the command line by running the `tsc` command.

#### Type Inferences

When we declare a variable with an initial value, the variable can never be reassigned to value of a different data type. TypeScript recognises these data types:

- Bool
- Number,
- Null,
- String,
- Undefined

#### Type Shapes

An object shape describes, among other things, what properties and methods it does or doesn't contain. TypeScript will tell you if you're using a method hat is not associated with that object.

#### Any

If a variable is declared without an initial value, it can be assigned and reassign dot any type.

#### Variable Type Annotation

We can tell TypeScript what type something is or will be by using a type of annotation.

```typescript
let mustBeAString: string;
```

This declares the variable with type string without reassigning it a value.

#### The tsconfig.json File

The tsconfig.json file is always placed in the root of your project and you can customize what rules you want the TypeScript compiler to enforce.

```json
{
  "compilerOptions": {
    "target": "es2017",
    "module": "commonjs",
    "strictNullChecks": true
  },
  "include": ["src/**/*.ts"]
}
```

- `"compilerOptions"` - is a nested object that contains all the rules to enforce.
- `"target": "es2017"` - is telling the project to use the 2017 version of ECMAScript standards for JavaScript.
- The project will be using `"commonjs"` syntax for importing and executing modules.
- `"StrictNullChecks"`, variables can only have null or undefined values if they are explicitly assigned those values.

### Functions

#### Parameter Type Annotation

Function parameters may be given type annotation with the same syntax as variable declaration

```typescript
function greet(name: string) {
  console.log(`Hello, ${name}!`);
}
```

#### Optional Parameters

We can also pass in optional values to a function:

```typescript
function greet(name?: string) {
  console.log(`Hello, ${name || "Anonymous"}!`);
}
```

We use the `?` operator at the end of a parameter name to tell TypeScript it is an optional parameter.

#### Default Parameter

We can have default parameters where if a value is passed that is not `undefined` or the same type as the default value, the default value will be used:

```typescript
function greet(name = "Anonymous") {
  console.log(`Hello, ${name}!`);
}
```

#### Inferring Return Types

If we set a variable to a function where the return of that function is of type string, the variable cannot be a different data type.

#### Explicit Return Type

We can add an explicit type annotation after a functions closing bracket.

```typescript
function greeting(name?: string): string {
  return `Hello, ${name ? name : "World"}!`;
}
```

#### Void Return Type

It is also good practice to use type void on a function that does not return anything:

```typescript
function greet(name: string): void {
  console.log(`Hello, ${name}!`);
}
```

#### Documenting Functions

A documentation comment is denoted with the first line `/**` and a final line `*/`. It's common for each line to start with `*`. We place a function documentation comment right above the declaration of the function.

We use `@param` to describe each of the function's parameters, and we can use `@returns` to describe what the function returns.

```typescript
/**
 * Calculates the sum of two numbers.
 * @param a - The first number.
 * @param b - The second number.
 * @returns The sum of `a` and `b`.
 */
function getSum(a: number, b: number): number {
  return a + b;
}
```

### Complex Types

#### Array Type Annotation

Below is an example of TypeScript array annotation.

```typescript
let names: string[] = ["Alice", "Bob", "Charlie"];
```

An alternative method is to use the `Array<T>` syntax where `<T>` stands for type.

```typescript
let names: Array<string> = ["Danny", "Samantha", "John"];
```

#### Multi-Dimensional Arrays

What about multi-dimensional arrays?

```typescript
let arr: string[][] = [
  ["a", "b", "c"],
  ["d", "e", "f"],
  ["g", "h", "i"],
];
```

#### Tuples

What about arrays that have elements of different types?

```typescript
let ourTuple: [string, number, boolean] = ["Hello", 42, true];
```

When an array is typed with elements of specific types, it's called a tuple. You cannot alter a tuple length and you cannot change element type.

#### Array Type Inference

Just so you ware aware, type inference always returns an array. When we want tuples, we need to use explicit type annotations.

```typescript
let tup: [number, number, number] = [1, 2, 3];
let concatResult = tup.concat([4, 5, 6]);
```

In the example above, `concat()` returns an array. As a result, `concatResult` is an array allowing us to expand the tuple `tup`.

#### Rest Parameters

The rest parameter syntax allows a function to accept an indefinite number of arguments as an array.

```typescript
function smush(firstString, ...otherStrings) {
  return firstString + otherStrings.join("");
}
```

The rest parameter can be type safe by using the same type annotation as an array:

```typescript
function smush(firstString: string, ...otherStrings: string[]) {
  return firstString + otherStrings.join("");
}
```

#### Enums

We use Enums when we'd like to enumerate all possible values that a variable could have.

```typescript
enum Direction {
  North,
  East,
  South,
  West,
}
let whichWay: Direction;
whichWay = Direction.North;
```

As you can see, the variable is of type direction and can only equal a value defined in the Enum.

But here's a fun fact: though the variable is set to `North`, it also has the value of 0 as `North` was the first in the Enum. If it was `South`, it would also equal 2.

If you want to change the starting number, use the following code.

```typescript
enum Direction {
  North = 7,
  East,
  South,
  West,
}
```

You can manually set each value to its own number.

#### String Enums vs Numeric Enums

We can also assign Enums string values.

It is a common practice that the string value is a capitalisation of the Enum valise. I.e., `north="NORTH"`

Even though numeric Enums can be assigned numbers, string Enums cannot be assigned strings making them more secure.

#### Use Objects instead of Enums

Though enums are useful, they are a TypeScript provided features meaning at compile time, enums are turned into basic JavaScript objects. i.e.:

```typescript
enum Direction {
  North = 7,
  East,
  South,
  West,
}
```

is turned into

```javascript
var Direction = {
  North: 7,
  East: 8,
  South: 9,
  West: 10,
};
```

So why use objects over Enums? Because you get the added benefit of getting all of the objects keys, values, or entries and perform array operations on them. A common practice with enums is to get the maximum value but this can only be done statically, with objects, however, this can be done dynamically.

```typescript
enum Direction {
  North = 7,
  East,
  South,
  West,
}

const maxEnum = Direction.West;

const Direction = {
  North: 7,
  East: 8,
  South: 9,
  West: 10,
} as const;

const maxValue = Math.max(...Object.values(Direction));
```

#### Object Types

The properties of objects have the same type annotation as normal variables:

```typescript
let aPerson: {
  name: string;
  age: number;
};
```

The above code states that `aPerson` can only be an object with those properties and type.

#### Type Aliases

Type aliases are alternative type names that we choose for convenience:

```typescript
type MyString = string;
let myVar: MyString = "Hello World";
```

This is helpful when we have long complicated types that are repeatedly use like object and array types.

#### Function Types

Function types specify the argument types and return type of a function.

```typescript
type StringToNumberFunc = (arg0: string, arg1: string) => number;
```

#### Generic Types

Generics give us the power to define our own collections of object types:

```typescript
type Family<T> = {
  parents: [T, T];
  mate: T;
  children: T[];
};
```

If `T` was equal to string:

```typescript
let aStringFamily: Family<string> = {
  parents: ["alice", "bob"],
  mate: "charlie",
  children: ["dave", "eve"],
};
```

In our code, which actually write `T` in the type to use as a placeholder. We could declare a new variable with type `Family<Boolean>` and code would still work.

#### Generic Functions

We can also use generics to create a collection of type functions.

```typescript
function getFilledArray<T>(value: T, n: number): T[] {
  return Array(n).fill(value);
}
```

The above code creates an array of size `n` and fills it with value of type `T`. to invoke the function:

```typescript
getFilledArray<string>("cheese", 3);
getFilledArray<boolean>(true, 7);
```

### Union Types

#### Defining Unions

Unions allow a variable to be a value of two of more specified types. For instance, an employee ID variable could be of type number or string but not Boolean.

Unions allow use to define multiple type members by separating each type member with a vertical line.

```typescript
let ID: number | string;
```

#### Type Narrowing

A type guard is a conditional that checks if a variable is a certain type

```typescript
if (typeof margin === 'number') {
  ...
}
```

This is called type narrowing. Type narrowing is when TypeScript can figure out what type a variable can be at a given point in our code.

#### Inferred Union Return Types

If a function returns multiple different types, TypeScript will infer that the function returns a union of those types. As a result, there is no need for us to manually infer this return type.

#### Unions and Arrays

To create a union that supports multiple types of an array's value, wrap the union in parentheses followed by square brackets.

```typescript
const timesList: (string | number)[] = [dateNum, dateString];
```

#### Common Key Value Pairs

When we put type members in a union, TypeScript will only allow us to use the common methods and properties that all members of the union share. Number and Boolean can both use `.toString` but Boolean cannot use `.toFixed(2)`.

This rule also applies to objects.

#### Unions with Literal Types

We can use literal types with unions:

```typescript
type Color = 'green' | 'yellow' | 'red';

function changeLight(color: Color) {
  ...
}
```

If we tried to call `changeLight('purple')`, we would get an error.

### Advanced Type Narrowing

#### Type Guards

A type guard is conditional which checks the type of a variable before the program performs actions on that variable unique to that type.

```typescript
if (typeof data === 'string') {
  ...
}
```

#### Using in With Type Guards

Sometimes we want to see if a specific method exists on a type instead of a type like string. The in operator checks if a property exists on an object itself or anywhere within its prototype chain.

```typescript
type Tennis = {
  serve: () => void;
};
function play(sport: Tennis | Soccer) {
  if ("serve" in sport) {
    return sport.serve;
  }
}
```

#### Narrowing After a Type Guard

If the if statement contains a return statement, then we don't even need an else statement.

### Advanced Object Types

#### Interfaces and Types

Below is an example of an interface:

```typescript
interface Mail {
  postagePrice: number;
  address: string;
}
const catalog: Mail = ...
```

Interface only works on objects.

#### Interfaces and Classes

The interface keyword in TypeScript is especially good for adding types to a class. Since interface is constrained to type objects and using class is a way to program with objects, interface and class are a great match.

```typescript
interface Robot {
  identify: (id: number) => void;
}
class OneSeries implements Robot {
  identify(id: number) {
    console.log("OneSeries Robot");
  }
}
```

The implements keyword is then often used to apply and type Robot in OneSeries. OneSeries can have methods of its own but it needs to implement the methods and attributes of Robot.

Implements and interfaces allow us to create types that match a variety of class patterns.

#### Deep Types

To type an object nested inside another object, we could write an interface like this:

```typescript
interface Robot {
  about: {
    general: {
      id: number;
      name: string;
    };
  };
  getRobotId: () => string;
}
```

#### Composed Types

TypeScript allows us to compose types. We can define multiple types and reference them inside other types.

```typescript
interface About {
  general: General;
}
interface General {
  id: number;
  name: string;
  version: Version;
}
interface Version {
  versionNumber: number;
}
```

We can now read our code easier with named types and we can reuse smaller interfaces in other places in our code.

#### Extending Interfaces

Sometimes it's convenient to copy all the type members from one type into another type. We can accomplish this with the extends keyword.

```typescript
interface Shape {
  color: string;
}
interface Square extends Shape {
  sideLength: number;
}
const mySquare: Square = { color: "blue", sideLength: 10 };
```

#### Index Signatures

It's useful to write an object type that allows us to include a variable name for the property name. this feature is called index signatures. We may get data from an API that looks like this:

```typescript
{
  '40.712776': true;
  '41.203323': true;
  '40.417286': true;
}
```

We know that the property names will be strings and we will know the values will be Boolean, but we don't know what the property names will be. To type this object, we can utilize an index signature to type this object.

```typescript
interface SolarEclipse {
  [latitude: string]: boolean;
}
```

The latitude name is purely for readability

#### Optional Type Members

TypeScript allows some methods and attributes within an interface to be optional.

```typescript
interface OptionsType {
  name: string;
  size?: string;
}
```

As you can see, an optional type member is denoted with an `?` before the `:` operator.
