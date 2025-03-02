# GM01603: Sass

@ George Madeley
@ Personal Studies
@ 12/3/24

### Introduction

This is a collection of notes that I, George Madeley, took when taking
the Codecademy Sass course. I do not take ownership of the material
covered and these notes should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: Sass](#sass)

[1 - Create a Sass Style Sheet](#create-a-sass-style-sheet)

[2 - Mixins and the & Selector](#mixins-and-the-selector)

[3 - Functions and Operations](#functions-and-operations)

[4 - Sustainable Sass](#sustainable-sass)

## Sass

### Create a Sass Style Sheet

#### Introduction to Sass Style Sheet

Sass or Syntactically Awesome Stylesheets is an extension language for
CSS. With Sass, you can write clean sustainable CSS code.

#### Compiling Sass

Sass must first be converted, or compiled, to CSS before the browser can
directly understand it. To do this, we use the following command:

```text
sass main.scss main.css
```

The Sass command takes in two arguments:

- The input (main.css),

- The location of where to place that output.

#### Nesting Selectors

Nesting is the process of placing selectors inside the scope of another
selector:

- In Sass, its helpful to think of the scope of selector as any of the
  code between its opening and closing brackets {}.

- Selectors that are nested inside the scope of other selectors are
  referred to as children and vice versa for parent.

```text
.parent {
  color: blue;
  .child {
    font-size: 12px;
  }
}
```

In CSS, the code above will look like:

```text
.parent {
  color: blue;
}

.parent .child {
  font-size: 12px;
}
```

Nesting allows you to see the clear DOM relationship between two
selectors while also removing the repetition observed in CSS.

#### Nesting Properties

You can also nest common CSS properties if you append a : colon suffix
after the name of the property.

```text
div {
  font: {
    family: Roboto, sans-serif;
    size: 20px;
  }
}
```

#### Variables in Sass

In Sass, \$ is used to define and reference a variable.

```text
$translucent-white: rgba(255, 255, 255, 0.3);
```

#### Maps and Lists

Lists can be separated by either spaces or commas. Maps are very similar
to lists, but instead each object is a key-value pair.

### Mixins and the & Selector

#### The & Selector in Nesting

In CSS, a pseudo-element is used to style parts of an element, for
example:

- Styling the content ::before or ::after the content of an element.

- Using a pseudo class such as :hover to set the properties of an
  element when the users mouse is touching the area of the element.

In Sass, the & character is sued to specify exactly where a parent
selector should be inserted.

```text
.notecard {
  &:hover {
    @include transform(rotate(5deg));
  }
}
```

#### What is Mixins?

Mixin lets you make groups of CSS declarations that you want to reuse
throughout your site:

```text
@mixin backface-visibility {
  backface-visibility: hidden;
  ...
}

.notecard {
  @include backface-visibility;
  ...
}
```

#### Mixin Arguments

An argument, or parameter, is a value passed to the mixin that will be
used inside the mixin, such as \$visibility in this example:

```text
@mixin backface-visibility($visbility) {
  backface-visibility: $visbility;
  ...
}
```

The syntax to pass in a value is as follows:

```text
@include backface-visibility(hidden);
```

#### Default Value Arguments

A default value is assigned to the argument if no value is passed in
when the mixin is included.

```text
@mixin backface-visibility($visbility: hidden) {
  backface-visibility: $visbility;
  ...
}
```

#### Mixin Facts

In general, here are five important facts about arguments and mixins:

- Mixins can take multiple arguments,

- Sass allows you to explicitly define each argument in your \@include
  statement.

- When values are explicitly specified you can send them out of order.

- If a mixin definition has a combination of arguments with and without
  a default value, you should define the ones with no default value
  first.

- Mixin can be nested

#### List Arguments

Sass allows you to pass in multiple arguments in a list or a map format.

#### String Interpolation

String interpolation is the process of placing a variable string in the
middle of two other strings. In a mixin content, interpolation is handy
when you want to make use of variables in selectors or file names.

```text
@mixin photo-content($file) {
  content: url(#{$file}.jpg);
  object-fit: cover;
}
```

#### The & Selector in Mixins

The & selector gets assigned the value of the parent at the point where
the mixin is included. If there is no parent selector, then the value is
null and Sass will throw an error.

### Functions and Operations

#### Introduction to Functions and Operations

Functions and operations in Sass allow for computing and integrating on
style.

#### Arithmetic and Colour

The alpha parameter in a colour like RGBA is a mask denoting opacity. It
specifies how one colour should be merged with another when the two are
on top of each other.

- fade-out() makes a colour more transparent by taking a number between
  0 and 1 and decreasing the opacity by that amount.

- fade-in() does the opposite.

- adjust-hue(\$color, \$degrees) changes the hue of a color. \$degrees
  must be a number between -360 and 360.

#### Colour Functions

Here is how Sass computers colours:

1. The operation is performed on the red, green, and blue components.

1. It computes the answer by operating on every two digits.

```text
color: #010203 + #040506 + #070809;
```

#### Arithmetic

The Sass arithmetic operations are:

- Addition +

- Subtraction --

- Multiplication \*

- Division /

- Modulus %

Units must be compatible. Also,
$\mathbf{10px \times 10px = 100p}\mathbf{x}^{\mathbf{2}}$ just like with
meters.

#### Division can be Special

In CSS, the / character can be used as a separator. In Sass, the
character is also used in division.

#### Each Loops

Each loops in Sass iterate on each of the values on a list:

```text
@each $item in $list {
  ...
}
```

The value of \$item is dynamically assigned to the value of the object
in the list according to its position and iterate of the loop.

#### For Loops

For loops in Sass can be used to style numerous elements or assigning
properties all at once.

```text
@for $i from $begin through $end {
  ...
}
```

#### Conditionals

If() is a conditional function that can only branch one of two ways
based on a condition. You can use it inline to assign the value of a
property:

```text
width: if($condition, $value-if-true, $value-if-false);
```

We can also use \@else-if, \@if, and \@else.

```text
@if($suit == hearts || $suit == diamonds) {
  color: red;
}
@else {
  color: black;
}
```

### Sustainable Sass

#### Sass Structure

As your webpage grows in complexity, so will the styles that go along
with it. It's best to keep code organised.

#### \@import in Sass

Sass extends the existing CSS \@impot rule to allow including other Scss
and Sass files.

#### Organise with Partials

Partials in Sass are the files you split up to organise specific
functionality in the code base.

- They use a \_ prefix notation in the file name that tells Sass to hold
  off on compiling the file individually and instead import it.

```text
_filename.scss
```

- To import this partial into the main file, omit the underscore.

```text
@import "variables"
```

#### \@extend

\@extend allows you to extend the ruleset of one element to another
without infringing on that elements own ruleset.

```text
.lemonade {
  border: 1px yellow;
}
.strawberry {
  @extend .lemonade;
  border-color: red;
}
```

#### %Placeholders

Placeholders behave just like a class or id selector, but use the %
notation instead of \# or a period. Placeholders prevent rules from
being rendered to CSS on their own and only become active once they are
extended anywhere and id or class should be extended.

##### In Sass:

```text
a%drink {
  ...
}
.lemonade {
  @extend %drink;
  ...
}
```

##### In CSS

```text
a.lemonade {
  ...
}
.lemonade {
  ...
}
```

#### \@extends vs \@mixins

Extending result in a cleaner and more efficient output with as little
repetition as possible. As a rule of thumb:

- Try to only create mixins that take in an argument, otherwise you
  should extend.

- Always look at your CSS output to make sure you extend in behaving as
  you intended.
