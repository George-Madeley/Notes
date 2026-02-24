# GM01622: Express.js

@ George Madeley
@ Personal Studies
@ 8/3/24

## Introduction

This is a collection of notes that I, George Madeley, took when taking the Codecademy Express.js courses. I do not take ownership of the material covered and these notes should only be used for educational purposes.

### Contents

[Introduction](#introduction)

[Contents](#contents)

[Section 1: Express.js](#expressjs)

[1 - Routes](#routes)

[2 - Middleware](#middleware)

[Section 2: Intermediate Express.js](#intermediate-expressjs)

[1 - OWASP Top 10](#owasp-top-10)

[2 - Authentication, Authorization, and Encryption](#authentication-authorization-and-encryption)

[3 - Session Authentication in Express.js](#session-authentication-in-expressjs)

[4 - Password Authentication](#password-authentication)

[5 - OAuth2.0 in Express.js](#oauth20-in-expressjs)

## Express.js

### Routes

#### Starting a Server

Express.js is a Node.js module, so to use it, we will need to import it into our program.

```javascript
const express = require("express");
const app = express();
```

In order for out server to start responding, we have to tell the server where to listen for new requests by providing a port number argument to a method called `app.listen()`. The second argument is a callback function that will be called once the server is running and ready to receive responses.

```javascript
const port = 4001;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

#### Writing Your First Route

To tell our server how to deal with any given request, we register a series of routes. Routes define the control flow for requests based on the request path and HTTP verb.

Express.js uses `app.get()` to register routes to match GET requests.
Express.js routes usually take two arguments, a path, and a callback function to handle the request and send a response.

```javascript
const moods = [   { mood: 'excited about express.js'},   { mood: 'route-tastic!' } ];
app.get('/moods', (req, res, next) => {
  ...
});
```

- `req` represents the request sent to the server,
- `res` represents the response that the Express.js server should eventually send to the client.

#### Sending a Response

Express.js servers send responses using the `.send()` method one the response object. `.send()` will take any input and include it in the response body.

```javascript
const monsters = [
  { type: "werewolf" },
  { type: "hydra" },
  { type: "chupacabra" },
];
app.get("/monsters", (req, res, next) => {
  res.send(monsters);
});
```

`.json()` can be used instead of `.send()`.

#### Matching Route Paths

Express.js searches through routes in the order they are registered in your code. It will find the fist registered route with a matching action and route. If there are no matching routes, a 404-error message will return.

#### Getting a Single Expression

Parameters are route path segments that begin with `:` in their express route definition. They act as wildcards, matching any text at that path segment. For example, `/monsters/:id` will match both `/monsters/1` and `/monsters/45`.

Express.js parses any parameters, extracts their actual values, and attaches the as an object to the request object: req.params. the objects keys are any parameter names in the route, and each key's value is the actual value of that field per request.

```javascript
const monsters = {
  hydra: { height: 3, age: 4 },
  dragon: { height: 200, age: 350 },
};
app.get("/monsters/:name", (req, res, next) => {
  console.log(req.params); // { name: 'hydra' }
  res.send(monsters[req.params.name]);
});
```

#### Setting Status Codes

Response codes provide information to clients about how their request was handled. The res object has a `.status()` method to allow us to set the status code, and other methods like `.send()` can be chained from it.

```javascript
app.get("/monsters/:name", (req, res, next) => {
  const monsterInventory = monsters[req.params.name];
  if (monsterInventory) {
    res.send(monsterInventory);
  } else {
    res.status(404).send("Monster not found");
  }
});
```

#### Matching Longer Paths

Route parameters will match anything in their specific part of the path,
so a route matching `/monster/:name` would match all following request paths:

`/monsters/hydra`
`/monsters/jormungandr`
`/monsters/manticore`
`/monsters/123`

#### Other HTTP Methods

PUT requests are used for updating existing resources.

#### Using Queries

Query strings appear at the end of the path in URLS, and they are indicated with a `?` character.

`/monsters/1/name=chimer&age=1`

Query strings for not count as the route path.

The Express.js server parses the query strings into a JavaScript object an it attaches it t the request body as the value of req.query.

```javascript
app.put("/monsters/:id", (req, res, next) => {
  const monsterUpdate = req.query;
  monsters[req.params.id] = monsterUpdate;
  res.send(monsters[req.params.id]);
});
```

The above code replaces the JSON in monsters at `req.params.id` with the value of `req.query`.

#### Matching By HTTP Verb

Express.js matches routes using both path and HTTP method verb.

#### Creating an Expression

POST is the HTTP method verb for creating new resources. Because POST routes create new data, their paths do not end with a route parameter, but instead end with the type of resource to be created.

The HTTP status code for a newly created resource is 201 Created.

```javascript
app.post("/expressions", (req, res, next) => {
  const receivedExpression = createElement("expressions", req.query);
  if (receivedExpression) {
    expressions.push(receivedExpression);
    res.status(201).send(receivedExpression);
  } else {
    res.status(400).send();
  }
});
```

#### Deleting Old Expressions

DELETE is the HTTP method verb used to delete resources.

The server sends a 204 No Content status code is deletion occurs without error.

Routers are mini versions of Express.js applications -- they provide functionality for handling route matching, requests, and sending responses but they do not start a separate server or listen on their own ports.

#### Express.Router

An Express.js router provides a subset of Express.js methods. To create an instance of one, we invoke the `.Router()` method on the top-level Express.js import. To use a router, we mount it at a certain path using `app.use()` and pass in the router as the second argument. This router will not be used for all paths that begin with that path segment.

```javascript
const monstersRouter = express.Router();
app.use('/monsters', monstersRouter);
monstersRouter.get('/:id', (req, res, next) => {
  ...
});
```

We will keep each router in its own file, and require them in the main application. This allows us to keep our code clean and our files short.

#### Matching Nested Routers

Make sure that if you have a get method for `/expression/:id`. If you move it into a router of `/expression`, you change the path to `/:id`.

### Middleware

#### Drying Code with Functions

Code that performs the same operation in multiple places is repetitive, and the quality coders credo is "Don't Repeat Yourself" (DRY). If a program performs similar tasks without refactoring into a function, it is said to "violate DRY".

#### Drying Routes with `app.use()`

Middleware is code that executes between a server receiving a request and sending a response. It operates on the boundary between those two HTTP actions.

Middleware can perform logic on the request and response objects, such as: inspecting a request, performing some logic based on the request, attaching information to the response, attaching a status to the response, sending the response back to the user or simply passing the request and response to another middleware.

#### `Next()`

The middleware stack is processed in the order they appear in the application file.

The `next()` method will hand off the processing of the request and the construction of the response to the next middleware in the stack.

#### Route Level `app.use()` Single Path

`app.use()` takes an optional path parameter as its first argument. We can now write middleware:

```javascript
app.use("/sorcerer", (req, res, next) => {
  console.log("User has hit endpoint /sorcerer");
  next();
});
```

#### Route Level `app.use()` Multiple Paths

`app.use()` can take an array of paths. This allows us to include multiple paths for one middleware function.

#### Middleware Stacks

Our callback functions don't have to be anonymous. We can also have multiple callback functions in our middleware:

```javascript
const authenticate = (req, res, next) => {
  ...
}
const getSpell = (req, res, next) => {
  ...
}
app.get('/spells/:id', authenticate, getSpell);
```

#### OpenSource Middleware

##### Logging

We will replace the logging code in the workspace with morgan, an open-source library for logging information about the HTTP request-response cycle in a server application.

`morgan()` is a function that will return a middleware function.

##### Body Parsing

The `body-parser` module allows us to easily parse the body of a `req` object.

#### Error Handling Middleware

Error handling middleware needs to be the last `app.use()` in your file.

```javascript
app.use((err, req, res, next) => {
  console.log(err.stack);
  res.status(500).send("Something broke!");
});
```

If we anticipate an operation might fail, we can invoke our error-handling middleware. We do this by passing an error object as an argument to `next()`.

```javascript
return next(undefinedError);
```

#### `Route.param()`

When a specific parameter is present in a route, we can write a function that will perform the necessary lookup and attach it to the req object in subsequent middleware that is run.

```javascript
app.param("spellId", (req, res, next, id) => {
  let spellId = Number(id);
  try {
    const found = spellBook.find((spell) => {
      return spell.id === spellId;
    });
    if (found) {
      req.spell = found;
      next();
    } else {
      next(new Error("No spell found"));
    }
  } catch (err) {
    next(err);
  }
});
```

The above code intercepts any url with a parameter `:spellId`. The code above finds the spell and stores it in the req object at req.spell.

#### Merge Parameters

We might want to access some property of complex object. We can do this with a nested router. In order to pass parameters, the parent router has access to, we pass a special configuration object when defining the router.

```javascript
const sorcererRouter = express.Router();
const familiarRouter = express.Router({ mergeParams: true });
sorcererRouter.use("/:sorcererId/familiars", familiarRouter);
app.use("/sorcerers", sorcererRouter);
```

## Intermediate Express.js

### OWASP Top 10

#### Introduction to OWASP Top 10

The OWASP Top 10 is a project maintained by the Open Web Application Security Project (OWASP). The top ten is a collection of the ten most serious vulnerabilities for web applications.

#### Injection

Injection is when an attacker injects malicious code into an interpreter in order to gain access to information or damage a system.

#### Broken Authentication

Broken authentication is a broad term for vulnerabilities that allow attackers to impersonate other users. vulnerabilities like insecure default credentials, lack of rate limiting for login attempts, and session hijacking all fall into this category.

#### Sensitive Data Exposure

Sensitive data exposure refers to insufficient protections being put in place for that data.

#### XML External Entities (XML)

XML External Entities (XXE) is a type of vulnerability that allows maliciously crafted data to produce unintended behaviours on the backend of a website. XXE involves an attacker uploading a maliciously crafted XML file.

#### Broken Access Control

Broken Access Control is when authorization is improperly enforced,
allowing users to access broken privileges they should not have.

#### Security Misconfiguration

Examples of security misconfiguration includes things like:

- Forgetting to protect cloud storage,
- Leaving unnecessary features enabled on server software,
- Disabling automatic updates,
- Displaying overly detailed error messages that give details about the way the backend is set up.

#### Cross Site Scripting (XSS)

Cross-Site Scripting (XSS) is a web vulnerability that targets the browser-side of th website. XSS happens when a browser is tricked into running malicious JavaScript. It usually happens when a website allows user input without sanitizing and un-harming dangerous input.

Preventing XSS involves making sure that special characters like `<`, `>`, `"`, `=`, and more are properly escaped to prevent a browser from parsing them as code rather than regular text.

#### Insecure Deserialization

Serialization is the process of turning an object within a program into formatted data. Deserialization is the process of turning formatted data into an object within code. Insecure deserialization is when this process can be exploited to cause unintended behaviour.

#### Using Components with Known Vulnerabilities

Using components with known vulnerabilities means using software or package versions that are known to be vulnerable.

#### Insufficient Logging and Monitoring

Insufficient Logging and Monitoring refers to overall lack of tools that monitor, record, and report events within a system. Events include logins and login attempts, webpage requests, and more. Having these logs allows monitoring software to scan for suspicious behaviour, such as 1000 login attempts in five seconds or connections to or form known malicious IP addresses.

### Authentication, Authorization, and Encryption

#### Authentication

Authentication is the verification of who you are.

Authentication relies on one or more factors to verify identity, and these factors come in three main types:

- Knowledge is something you know, like a username and password.
- Possession is something you have, like a security card or mobile device.
- Inherence is something you are, which generally refers to biometric data such as fingerprints.

#### Authorization

Authorization is the verification of what you are allowed to do.

#### Encryption

Encryption is the process of transforming data into a format that in unreadable unless you have the correct key to decrypt it.

#### Single Sign-On and OAuth2

The most recent advancement in authentication is single sign-on (SSO). This is where you use sign-in with Google, Facebook etc. the current standard for SSO is OAuth2.0.

### Session Authentication in Express.js

#### Web Sessions

A web session refers to a series of user interactions over a time frame. Session data is stored server-side and associated with a session ID.

#### Sessions and Cookies

Cookies are tiny pieces of data -- text files of max 4kB -- the browser stores that are automatically sent with HTTP requests to a web application.

Cookies are set by the HTTP response header in key-value pairs. A session cookie is set with the first HTTP response from the server and persists until the browser is closed or the cookie expires.

```text
Set-Cookie: sessionId=34jgL79b
```

This is how a session is implemented with cookies:

1. A user goes to a store. The web server creates a session and a session id.
2. In the server's response, it tells the browser to store a cookie with the session id (should not include any personal information)
3. The session id cookie automatically attaches to each subsequent HTTP request to the server.
4. When the server reads the session id cookie sent with the next HTTP request, it returns the session data associated with the id.
5. The process continues if the session is active.
6. The session and session id cookie expires after a user closes out the browser, logs out, or a predetermined session length pass.

#### Cookie Security

The first step to securing a cookie could be adding an expiration date or duration so a cookie doesn't persist longer than it needs to. We ca specify that information through the set-cookie header in an HTTP response like so:

```text
Set-Cookie: Key=Value;
Expires=Wed, 09 Jun 2021 10:18:14 GMT;
```

The `HttpOnly` attribute for the Set-Cookie header makes sure that the cookie's data is not accessible to a script running client-side. This helps prevent XSS attacks.

#### What is localStorage?

Local Storage is a form of client-side storage. Data is stored in key-value pairs. Local Storage will persist even after a user exits the browser and will continue to persist until the browser cache is deleted.

Session storage, which uses the same syntax as Local Storage, can hold session data. This storage clears once the browser closes, so, for many cases this is more secure.

Setting a key-value pair in local storage is easy as this:

```javascript
localStorage.setItem('<key-name>', <value>);
```

We can get a key-value pair like so:

```javascript
localStorage.getItem("<key-name>");
```

#### Cookies vs localStorage vs sessionStorage

|                       | Cookies    | Local Storage                       | Session Storage           |
| --------------------- | ---------- | ----------------------------------- | ------------------------- |
| Read by server        | Yes        | No                                  | No                        |
| Capacity              | 4kB/Domain | 10MB/Domain                         | 5MB/Domain                |
| Expiry                | Custom     | Never or manual deletion in browser | When a session tab closes |
| Browser compatibility | HTML 4/5   | HTML 5                              | HTML 5                    |
| Access Form           | Any Window | Any Window                          | Same Tab                  |

#### Installing `express-session`

To implement session within an Express.js application, we can use the NPM module, expression-session, as a middleware. This allows us to store users' session data server-side under a session identifier and easily retrieve it.

```bash
npm install express-install
```

```javascript
const session = require("express-session");
```

#### Express Session Configuration

Let's explore a few options we can configure:

- `secret` - is a key used for signing and/or encrypting cookies to protect our session id.
- `resave` - setting this option to true will force a session to be saved back to session data store, even when no data was modified.
- `saveUninitialised` -- if its set to true, the server will store every new session, even if there are no changes to session objects.

```javascript
app.use(
  session({
    secret: "D53gx141G",
    resave: false,
    saveUninitialized: false,
  })
);
```

The secret should be stored as an environment variable.

#### Storing Session Data

Let's configure how the middleware saves session data. Sessions are typically stored in three ways:

- In memory
- In a database like MongoDB or MySQL.
- A memory cache like Redis or Memcached.

`express-session` provides an in-memory store called, `MemoryStore()`. If no other store is specified, then this is set as the default storage.

```javascript
const store = new session.MemoryStore();
```

Once instantiated, we can add it in the configuration of our session:

```javascript
app.use(
  session({
    ...store,
  })
);
```

#### Authentication and Sessions

##### Cookies

We can add a cookie property in our session middleware like so:

```javascript
app.use(
  session({
    cookie: {
      maxAge: 1000 * 60 * 60 * 24 * 7, // 1 week
      secure: true,
      sameSite: "none",
    },
  })
);
```

maxAge sets the number of milliseconds until the cookie expires. Secure means it's only sent to the server with HTTPS. SameSite property and setting it to "none" to allow a cross-site cookie through different browsers.

Other cookie properties include:

- `Cookie.expires`,
- `Cookie.httpOnly`,
- `Cookie.sameSite`

##### Logging In

Once a user has logged in, we'll add a property, authenticated within our session object, and assign it to true. We'll also set user in the session data and assign it the username and password we received.

```javascript
req.session.authenticated = true;
req.session.user {
  username,
  password,
};
```

#### Accessing Session Data

Data in a session is serialized as JSON when stored, so we're able to access data in nested objects.

One common use case of session data is to protect specific routes.

```javascript
function authorizedUser(req, res, next) {
  if ((req, session.authorized)) {
    res.next();
  } else {
    res.status(403).json({
      msg: "You're not authorized to view this page",
    });
  }
}
```

### Password Authentication

#### Introduction to Password Authentication

Passport.js is a flexible authentication middleware for Node.js that can be added to any express based application. With Passport.js we can implement authentication using the concepts of strategies.

Passport strategies are separate modules created to work with different manes of authentication.

#### Configuring Passport.js

To start using the traditional authentication module, we install the passport and the passport-local packages.

```bash
npm install passport passport-local
```

Once imported, we require the passport and `passport-local` packages in our JavaScript file.:

```javascript
const passport = require("passport");
const LocalStrategy = require("passport-local").Strategy;
```

We can initialize by calling:

```javascript
app.use(passport.initialize());
```

We want to allow for persistent logins, and we can do this by calling `session()` on our passport module.

```javascript
app.use(passport.session());
```

#### Passport's Local Strategy

We can now set up the passport-local strategy for authenticating with a username and password. First, we can configure the local strategy by creating a now instance of it and passing it as middleware into password:

```javascript
passport.use(new LocalStrategy(
  function(username, password, done) {
    ...
  }
));
```

Done is a callback function.

The purpose of the done callback is to supply an authenticated user to passport if a user is authenticated. The logic within the anonymous function flows this order:

1. Verify login details in the callback function
2. If login details are valid, the done callback is invoked, and the user is authenticated.
3. If the user is not authenticated, pass false into the callback function.

The done callback takes in two arguments:

- An error or null if no user is found.
- A user of false if no user is found.

```javascript
passport.use(
  new LocalStrategy(function (username, password, done) {
    db.users.findByUsername(username, (err, user) => {
      if (err) return done(err);
      if (!user) return done(null, false);
      if (user.password !== password) {
        return done(null, false);
      }
      return done(null, user);
    });
  })
);
```

#### Serializing and Deserializing Users

If a user logs in a refresh the page, the user data won't persist across HTTP requests, we can fix this by serializing and deserializing users.

Serializing a user determines which data of the user object should be stored in the session, usually the user id. The `serializeUser()` function sets an id as the cookie in the user's browser, and the `deserializeUser()` function uses the id to look up the user in the database and retrieve the user object with data.

```javascript
passport.serializeUser((user, done) => {
  done(null, user.id);
});
```

Once configured, the user id will then be stored in passports internal session.

```javascript
req.session.passport.user = { id: "xyz" };
```

For any subsequent request, the user object can be retrieved from the session via the deserializeUser() function.

```javascript
passport.deserializeUser((id, done) => {
  db.users.findById(id, (err, user) => {
    if (err) return done(err);
    done(null, user);
  });
});
```

#### Passport Logging In

To log a user in we first need a POST request that takes in user credentials. We can add passport middleware to process the authentication and if successful, serialise the user for us:

```javascript
app.post(
  "/login",
  passport.authenticate("<insert_strategy_here>", {
    failureRedirect: "/insertPathHere",
  }),
  (req, res) => {
    res.redirect("profile");
  }
);
```

Once implemented, we can update the `"/profile"` endpoint to make use of the serialized user found in the request object req.user.

```javascript
app.get("/profile", (req, res) => {
  res.render("profile", { user: req.user });
});
```

#### User Registration

The following is how we can add a new user:

```javascript
app.post("/register", async (req, res) => {
  const { username, password } = req.body;
  const newUser = await db.users.createUser({
    username,
    password,
  });
  if (newUser) {
    res.status(201).json({
      msg: "User created",
      user: newUser,
    });
  } else {
    res.status(500).json({
      msg: "User not created",
    });
  }
});
```

#### Logging Out

Passport.js exposes a logout function within the request object: `req.logout`. the function can be called from any route handler to terminate a login session. It removes the req.user property and clears the login session.

```javascript
app.get("/logout", (req, res) => {
  req.logout();
  res.redirect("/");
});
```

By terminating the session, the user will have to re-authenticate in order to create a new session.

#### Introduction to `bcrypt`

Using `bcrypt`, we can protect our users by hashing and salting passwords. Using multiple rounds of hashing ensures that an attacker must deploy massive funds and hardware to be able to crack your passwords.

#### Hash Function

`bcrypt` is a hashing algorithm. A hash function only works one-way.

We only stored the hashed password in the database. To authenticate a user, we hash the entered password and compare it to the value stored in the db. If they match, the user is authenticated.

#### Salts and Rainbow Table Attacks

Rainbow tables are large lookup databases that consist of pre-computed password-hash combinations which correlate plaintext passwords with their hashes.

Rainbow tables are massive lookup tables that can crack complex passwords significantly faster than using traditional password cracking methods.

A salt is a random value that is added to the input of a hashing function I order to make each password has unique even in the instance of two users choosing the same passwords. Salts help us mitigate hash table attacks by forcing attackers to re-compute them using the salts for each user.

#### Using bcrypt to Hash Passwords

bcrypt uses a salt and salt rounds to secure a password.

A salt is a value that is concatenated to a password before hashing to make it less vulnerable to rainbow table and brute-force attacks.

A salt round can be described as the amount of time needed to calculate a single bcrypt hash. The higher the salt rounds, the more time is necessary to crack a password.

The built-in `genSalt()` function automatically generates a salt for us. Once we have a salt generated, make a call to `bcrypt.hash()`. This function takes in a password string and a salt.

```javascript
const passwordHash = async (password, saltRounds) => {
  try {
    const salt = await bcrypt.genSalt(saltRounds);
    return await bcrypt.hash(password, salt);
  } catch (err) {
    console.error(err);
  }
  return null;
};
```

#### Verifying Passwords

`bcrypt` provides us with a handy function called `compare()` which takes in a plaintext password, password, and a hashed password, hash. `bcrypt.compare()` deduces the salt from the provided hash and is able to then hash the provided password correctly for comparison.

```javascript
const comparePasswords = async (password, hash) => {
  try {
    const matchFound = await bcrypt.compare(password, hash);
    return matchFound;
  } catch (err) {
    console.error(err);
  }
  return false;
};
```

### OAuth2.0 in Express.js

#### Introduction to OAuth

OAuth is an authorisation framework that provides specific authorization flows which allow unrelated servers to access authenticated resources without sharing any passwords. It works by allowing applications to authenticate with third-party services in exchange for an access token which can be passed with an HTTP request to access protected content.

- **Resource Owner -** the user who authorizes an application to an account.
- **Resource Server -** the API server that accepts access tokens and verifies their validity.
- **Authorization Server -** the server that issues access tokens.
- **Client -** the application that requests the access token.

#### Implementing OAuth

We will be using the oauth2-server

```bash
npm install oauth2-server
```

```javascript
const OAuth2Server = require("oauth2-server");
```

#### Creating an OAuth 2.0 Server Instance

We'll create an instance of the OAuth2Server object.

```javascript
const oauth = new OAuth2Server();
```

OAuth2Server can be supplied with additional options in the constructor.

To pass tokens inside the URL, we'll set the `allowBearerTokensInQueryString` attribute to true. The access token lifetime can also be configured. This is in seconds.

```javascript
const oauth = new OAuth2Server({
  model: require("./model.js"),
  allowBearerTokensInQueryString: true,
  accessTokenLifetime: 60 * 60,
});
```

#### Registering Client to Application

OAuth defines two types of clients -- confidential clients and public clients. When a developer registers a client in an OAuth application, they'll need:

- **A Client Id -** a public identifier for apps that is unique across all clients and the authorization server.
- **A Client Secret -** a secret key known only to the application and the authorization server.

```javascript
module.exports = {
  confidentialClients: [
    {
      clientId: "confidentialApplication",
      clientSecret: "topSecret",
      grants: ["password", "client_credentials"],
    },
  ],
};
```

#### `getClient()`

OAuth2Server requires certain functions implemented in the model regardless of the authorization flow used. The `getClient()` function is an example of a required model function for all flows. The function is used to retrieve a client using a client id and/or a client secret combination.

```javascript
const getClient = (clientId, clientSecret) => {
  let sClients = db.confidentialClients.filter((client) => {
    return (
      clients.clientId === clientId && clients.clientSecret === clientSecret
    );
  });
  return sClients[0];
};
```

#### `SaveToken()`

This function stores the access token as an object to a database when an access token is obtained.

```javascript
const saveToken = (token, client, user) => {
  token.client = {
    id: client.clientId,
  };
  token.user = {
    username: user.username,
  };
  db.tokens.push(token);
  return token;
};
```

#### `getUserFromClient()`

the client credentials grant type must have the `getUserFromClient()` function implemented to be used. The `getUserFromClient()` function is invoked to retrieve the user associated with the specific client.

```javascript
const getUserFromClient = (client) => {
  return {};
};
```

#### Obtaining Token Handler

We need to create a callback function to handler obtaining the access token whenever a URL is requested in our application.

```javascript
const obtainToken = (req, res) => {
  const request = new OAuth2Server.Request(req);
  const response = new OAuth2Server.Response(res);

  return oauth
    .token(request, response)
    .then((token) => {
      res.json(token);
    })
    .catch((err) => {
      res.status(err.code || 500).json(err);
    });
};
```
