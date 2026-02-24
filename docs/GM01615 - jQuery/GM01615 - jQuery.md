# GM01615: jQuery

@ George Madeley
@ Personal Studies
@ 8/3/24

## Introduction

This is a collection of notes that I, George Madeley, took when taking the Codecademy jQuery course. I do not take ownership of the material covered and these notes should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: jQuery](#jquery)

[1 - Introduction to JQuery](#introduction-to-jquery)

[2 - Effects](#effects)

[3 - Advanced Event Handlers](#advanced-event-handlers)

[4 - Style Method](#style-method)

[5 - Traversing the DOM](#traversing-the-dom)

## jQuery

### Introduction to Jquery

#### What is jQuery?

jQuery is a JavaScript library that makes it easy to add dynamic behaviours to HTML elements.

#### jQuery Library

To load jQuery, we use a script tag as follows:

```html
<script
  src="https://code.jquery.com/jquery-3.5.1.min.js"
  integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
  crossorigin="anonymous"
></script>
```

The jQuery library is loaded from the jQuery content delivery Network (CDN). A CDN is a collection of serves that can deliver content. The integrity of servers that can deliver content. The integrity and cross origin properties in the example ensure that file is delivered without any third-party manipulation.

#### `.Ready()`

The jQuery `.ready()` method waits until the html page's DOM is ready to manipulate. You should wrap all JavaScript behaviours inside of the `.ready()` method.

```javascript
$(document).ready(() => {
  ...
});
```

#### Targeting by Class

We pass a string into `$()` to target elements by id, class, or tag. Once targeted, we can uses `.` notation to attack a handler method that triggers a call back function.

```javascript
$(".someClass").handlerMethod();
```

#### Targeting by Id

To select by id, we prepend the element's id name the `#` symbol.

```javascript
$("#someId").hide();
```

#### jQuery Objects

the `$` symbol is an alias for the jQuery function. The `$` symbol and jQuery are interchangeable.

```javascript
const $jQueryObject = $(".someClass");
```

It is best practise to name jQuery object variables with a leading `$` symbol.

#### Event Handlers

The jQuery `.on()` method adds event handlers to jQuery object. The method takes a string of the event and a callback function.

```javascript
$("login").on("click", () => {
  $loginForm.show();
});
```

### Effects

#### `.hide()`

When you hide an element, your browser will render the element as if it does not exist.

```javascript
$(".hide-arrow").on("click", () => {
  $(".show-information").hide();
});
```

#### `.show()`

Luckily, the `.show()` method does the opposite of `.hide()`. If an element on your page is hidden, `.show()` will make it appear.

```javascript
$(".show-arrow").on("click", () => {
  $(".shoe-information").show();
});
```

#### `.toggle()`

The `.toggle()` method toggles between shown and hidden.

```javascript
$(".toggle-button").on("click", () => {
  $(".shoe-information").toggle();
});
```

#### Fading

The `.fadeIn()` method is called on an HTML element. Instead of instantly showing the element, `.fadeIn()` and `.fadeOut()` make the element appear or disappear over a given period of time.

```javascript
$("div").fadeOut(1000);
```

#### `.fadeToggle()`

`.fadeToggle()` is similar to the `.fade()` method, however, it combines `.fadeIn()` and `.fadeOut()`.

```javascript
$("div").fadeToggle(1000);
```

#### Sliding

By using sliding effects, an element on your web page will slide up or down into place instead of appearing or disappearing.

```javascript
$(".menu-content").slideDown("slow");
```

### Advanced Event Handlers

#### Introduction to Event Handlers

An event listener is a method that listens for a specified event to occur, like a click event. A callback function is a function that executes when something triggers the event listener.

#### On 'mouseenter'

The `mouseenter` event triggers a callback function when a user enters the area that targeted element occupies.

#### On 'mouseleave'

The `mouseleave` event listener can detect when a user's mouse leaves the area that an element occupies.

#### Chaining Events

Instead of re-declaring the HTML element you're selecting, you can append one event to another.

```javascript
$(".example-class")
  .on("mouseenter", () => {
    $(".example-class-one").show();
  })
  .on("mouseleave", () => {
    $(".example-class-one").hide();
  });
```

If you want to make something zoom in when someone hovers over it, use the following code:

```javascript
$(".example-class").addClass("photo-active");
```

#### Current Target

When we call an event handler callback function, we can pass in an event object. `currentTarget` is an attribute of event which targets the HTML element in which the event has occurred from i.e., if you used `mouseenter` on a button, `currentTarget` would refer to that button.

```javascript
$(".example-class").on("mouseenter", (event) => {
  $(event.currentTarget).addClass("active");
});
```

### Style Method

#### `.css()`

To modify CSS properties of an element, jQuery provides a method called `.css()`. This method accepts an argument for a CSS property name and a corresponding CSS value.

```javascript
$(".example-class").css("color", "red");
```

The `.css()` method can accepts many CSS property/value pair at once. You must pass the `.css()` method a JavaScript object with a list of key/value pairs:

```javascript
$(".example-class").css({
  color: "red",
  "font-size": "20px",
  "background-color": "#000",
});
```

#### `.animate()`

The first argument of the `.animate()` method is a JavaScript object of CSS property/value pair that represents an elements end state. The second argument determines how long the animation takes to complete.

```javascript
$(".example-class").animate(
  {
    opacity: 0.25,
    left: "+=50",
  },
  500
);
```

#### `.addClass()`

Its best to keep all the CSS styles in one file. This is where `.addClass()` comes in. this method adds classes to a given HTML element.

#### `.removeClass()`

`.removeClass()` method removes a class from a given HTML element.

#### `.toggleClass()`

The `.toggleClass()` method adds a class if an element does not already have it, and removes it if an element does already have it.

```javascript
$(".example-class").toggleClass("active");
```

### Traversing the DOM

#### `.children()`

The jQuery `.children()` method allows us to target these elements.

```javascript
const $kids = $("#holder").children();
```

#### `.parent()` and `.siblings()`

The `.parent()` an `.siblings()` methods target the element parent and sibling element respectfully.

#### `.closest()`

To select an element close to the current, we can use jQuery's
`.closest()` method. The `.closest()` method will travel up the DOM tree to find a specified selector closest to it.

```javascript
$(".example-class").closest(".another-class");
```

#### `.next()`

The `.next()` method only targets the next sibling.

#### `.find()`

The `.find()` method targets singular or multiple elements that are descendants of an element. It traverses all descendants of a specified element.

```javascript
$(".myList").find("li");
```
