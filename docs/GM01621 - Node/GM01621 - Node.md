# GM01621: Node.js

@ George Madeley
@ Personal Studies
@ 8/3/24

## Introduction

This is a collection of notes that I, George Madeley, took when taking the Codecademy Node.js course. I do not take ownership of the material covered and these notes should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: Node.js](#nodejs)

[1 - Introduction to Node.js](#introduction-to-nodejs)

[2 - Node.js Essentials](#nodejs-essentials)

[4 - Setting Up a Server With HTTP](#setting-up-a-server-with-http)

## Node.js

### Introduction to Node.js

#### What is Node.js?

Traditionally, JavaScript can only be run on the browser. However, the invention Node.js allowed developers to execute JavaScript code on the server (non-browser environments). Of course, the JavaScript code cannot access globals unique to the browser such as `window` but the Node.js runtime provides libraries that allow JavaScript to access the OS, filesystem, path, and many more.

Node.js is not the only JavaScript runtime environment. Since its invention, others have also been developed:

- **Node.js -** Written in C++,
- **Deno -** Witten in Rust,
- **Bun -** Written in Zig

#### The Node REPL

REPL is an abbreviation for Read-Eval-Print loop. It's a program that loops through three different states:

- A read state where the program reads an input from the user
- The eval state where the program evaluates the users input.
- The print state where the program prints out its evaluation to the console.

You can access the REPL by typing the command node. A `>` will appear in the terminal indicating the REPL is running and prompting your input.

Once you hit enter, your input is sent to the evaluation stage of REPL. However, if you want to enter multiple lines, you can use the .editor to enter multiple lines. This will send you to the 'editor' mode. Once you're ready, you send the lines by pressing Ctrl + D.

Every Node-specific global property sits inside the Node global object. This object contains several useful properties and methods that are available anywhere in the Node environment.

#### Running a Program with Node

Node also provides the ability to run JavaScript programs on your computer. To execute a program, we must navigate to the directory that contains our program. Then, we type the following command into our terminal.

```bash
node program.js
```

#### Core Modules

Modularity is a software design technique where one program has distinct parts, each providing a piece of the overall functionality. These separate modules come together to build a cohesive whole.

Node has several inbuilt modules called core modules. These are in the lib/ folder of Node's source code. Core modules can be required by passing a string with the name of the modules into the `required()` function.

```javascript
const events = require("events");
```

We can get a complete list of inbuilt modules by typing in the following command to REPL:

```javascript
require("module").builtinModules;
```

#### The Console Module

We don't need to require the console module as it is globally accessible and is very similar to the console object we've used in JavaScript.

#### The Process Module

Node has a global process object with useful methods and information about the current process.

The `process.env` property is an object which stores and controls information about the environment in which the process is currently running.

One condition is the add a property to `process.env` with the key NODE_ENV and a value of either production or development.

```javascript
if (process.env.NODE_ENV === "development") {
  console.log("Testing! Testing! Does Everything work?");
}
```

The `process.memoryUsage()` returns information on the CPU demands of the current process. It returns a property that looks similar to this:

```json
{
  rss: 26247168;
  heapTotal: 5767168;
  heapUsed: 3573032;
  external: 8772;
}
```

The `process.argv` property holds an array of command line values provided when the process was initiated. Something like below:

```bash
node myProgram.js testing several features
```

```javascript
console.log(process.argv[3]); // returns several
```

#### The os Module

The `os` module is not global and needs to be included into the file to gain access to its methods.

```javascript
const os = require("os");
```

With the `os` module, you can call methods like:

- `os.type()` - to return the computers operating system.
- `os.arch()` - to return the operating system CPU architecture.
- `os.networkInterfaces` - to return information about the network interfaces of the computer such as IP and MAC addresses.
- `os.homedir()` - to return the current user's home directory.
- `os.hostname()` - to return the hostname of the operating system.
- `os.uptime()` - to return the system up time in seconds.

```javascript
const os = require("os");
const local = {
  "Home Directory": os.homedir(),
  "Operating System": os.type(),
  "Last Reboot": os.uptime(),
};
```

#### The `util` Module

The `util` module can be required into the file like so:

```javascript
const util = require("util");
```

One important object is `types`, which provides methods for runtime type checking in Node.

```javascript
console.log(util.types.isDate(today));
```

The above example checks if the `today` variable is of type date and return true if so. Another important util method is `.promisfy()`, which turns callback function into promises.

### Node.js Essentials

#### The Events Module

Node provides an EventEmitter class which we can access by requiring in the events core modules:

```javascript
let events = require("events");
let eventEmitter = new events.EventEmitter();
```

Each event emitter instance has an `.on()` method which assigns a listener callback function to a named event. The `.on()` method takes as its first argument the name of the event as a string and, as its second argument, the data that should be passed into the listener callback function.

Each event emitter instance also has an `.emit()` method which announces a named event has occurred. It takes the name of the event as the first argument, and the data that should be passed into the listener callback function as the second argument.

```javascript
eventEmitter.on("new user", newUserListener);
eventEmitter.on("new user", "Lily Pad");
```

#### User Input/Output

In Node, we can also receive input from a users through the terminal using the `stdin.on()` method on the process object.

```javascript
process.stdin.on("data", (userInput) => {
  let input = userInput.toString();
  console.log(input);
});
```

#### The Error Module

The Node's environment's error module has all the standard JavaScript errs such as:

- `EvalError`,
- `SyntaxError`,
- `RangeError`,
- `ReferenceError`,
- `TypeError`,
- `URIError`

#### The `Buffer` Module

The `Buffer` module is used to handle binary data. A buffer object represents a fixed amount of memory that can't be resized. The buffer object will have a range of integers from 0 to 255 inclusive.

The `.alloc()` method creates a new buffer object with the size specified as the first parameter.

```javascript
const buffer = Buffer.alloc(5); //[0, 0, 0, 0, 0]
```

The `.toString()` method converts the buffer object into a human-readable string.

```javascript
const buffer = Buffer.aloc(5, "a");
console.log(buffer.toString()); // aaaaa
```

The `.from()` method is provided to create a new buffer object from the specified string, array, or buffer.

```javascript
const buffer = Buffer.from("hello");
//[104, 101, 108, 108, 111]
```

The `.concat()` method joins all buffer objects passed in an array into one `Buffer` object.

```javascript
const array = [buffer1, buffer2];
const bufferConcat = Buffer.concat(array);
```

#### The `fs` Module

The technique of isolating some applications from others is known as sandboxing. Sandboxing protects users from malicious programs and invasions of privacy.

The Node `fs` core module is an API for interacting with the file system. Each method available on the fs module has a synchronous and asynchronous version.

#### Readable Streams

To read files line-by-line, we can use the `.createInterface()` method from the readline core module. `.createInterface()` returns an `EventEmitter` set up to emit 'line' events.

```javascript
const readline = require("readline");
const fs = require("fs");
const myInterface = readline.createInterface({
  input: fs.createReadStream("input.txt"),
});
myInterface.on("line", (fileLine) => {
  console.log(`The line read: ${fileLine}`);
});
```

#### Writeable Streams

We can create a writeable stream to a file using the `fs.createWriteStream()` method:

```javascript
const fileStream = fs.createWriteStream("output.txt");
fileStream.write("This is the first line!");
fileStream.write("This is the second line!");
fileStream.end();
```

#### The Timers Module

There are times in which we want our code to be executed at a specific point in time.

When the `setImmediate()` is called, it executes the specified callback function after the current poll phase is complete. The method accepts two parameters: the callback function and the arguments for the callback function.

```javascript
setImmediate(() => {
  console.log.log("Hello, World!");
});
```

### Setting Up a Server With HTTP

#### Introduction to Setting Up a Server with HTTP

HTTP, short for Hypertext Transfer Protocol, is a request-response protocol that serves as the foundation of data exchange and communication within the client-server computing model.

1. The client submits a HTTP request message to the server,
2. The server receives the HTTP request, performs some functions on behalf of the client according to the request
3. The server returns a response message to the client containing important information about the processing of the request.

#### The Structure of HTTP

HTTP requests and responses have specified structures to help facilitate the exchange of information between a client and a server.

![A close-up of a notepad Description automatically generated](media/image24.png)

#### The Movement of HTTP

Various transfer protocols exist. Below are some of the most common:

- **TCP -** Transmission Control Protocol allows two hosts to connect and exchange data streams.
- **UDP -** User Datagram Protocol operates by using a connectionless communication model requiring no 'handshaking' which leads to unreliability.
- **TLS -** Transport Layer Security designed to facilitate secure data transmission via encryption.

#### The HTTP Module

The `.createServer()` creates an HTTP server.

```javascript
const server = http.createServer((req, res) => {
  res.send("server is running");
});
server.listen(8080, () => {
  const { address, port } = server.address();
  console.log(`Server is listening on: http://${address}:${port}`);
});
```

The req object contains all the information about the HTTP request ingested by the server. The res object contains methods and properties pertaining to the generation of a response by the HTTP server.

#### The Anatomy of the URL

A URL is made up of the following parts:

![A close-up of a white board with purple writing Description automatically generated](media/image26.png)

#### The URL Module

The core of the URL module around the URL class.

```javascript
const url = new URL("https://www.example.com?foo=1&bar=2");
```

Once instantiated, different parts of the URL can be accessed and modified via various properties which include:

- `.hostname` - gets and sets the host name of the url,
- `.pathname` - gets and sets the path portion of the url,
- `.searchParams` - gets the search parameter object representing the query parameter contained within the URL.

Below are examples:

```javascript
const host = url.hostname; // example.com
const path = url.pathname; // /p/a/t/h
const searchParams = url.searchParams; // {query: "string"}
```

#### The `querystring` Module

The `queryString` module provides utilities solely focused on parsing and formatting URL query strings. The core methods are listed below:

- `.parse()` - parses a URL query string into a collection of key-value pairs.
- `.stringify()` - produces a URL query string from a given object via iteration of the objects 'own properties'.
- `.escape()` - performs percent-encoding on a given query string.
- `.unescape()` - decodes percent-encoded characters within a given query string.

#### Routing

The process of handling requests in specific ways based on the information provided within the request is known as routing.

```javascript
const server = http.createServer((req, res) => {
  const { method } = req;
  switch(method) {
    case 'GET': ...
    case 'POST': ...
    case 'PUT': ...
    case 'DELETE': ...
    default: throw new Error(...);
  }
});
```

The path name allows the server to understand what resource is being targeted.

#### HTTP Status Codes

Response status codes are built into five classes.

1. **Informational** range from 100 -- 199
2. **Successful** range from 200 -- 299
3. **Redirects** range from 300 -- 399
4. **Client Errors** range from 400 -- 499
5. **Server Errors** range from 500 -- 599

#### Interacting with Another Backend API

Sometimes we may wat to communicate with external APIs. To do this, we use the `require()` function. It takes two arguments. The first is a configuration object containing details about the request and the second is a callback to handle the response.
