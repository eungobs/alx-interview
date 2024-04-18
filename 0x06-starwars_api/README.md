# 0x06. Star Wars API

## Description
This project involves interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. The script retrieves character data from the Star Wars API and prints the names of the characters in the specified movie.

## Concepts
- HTTP Requests in JavaScript
  - Making HTTP requests to external services using `request` module or alternatives like `fetch` in Node.js.
  - [A Complete Guide to Making HTTP Requests in Node.js](https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html)
- Working with APIs
  - Understanding RESTful APIs and interacting with them.
  - Parsing JSON data returned by APIs.
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- Asynchronous Programming
  - Managing asynchronous operations with callbacks, promises, and async/await syntax.
  - Handling API response data asynchronously.
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- Command Line Arguments in Node.js
  - Using `process.argv` array to access command-line arguments passed to a Node.js script.
  - [How to Parse Command Line Arguments in Node.js](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/)
- Array Manipulation and Iteration
  - Iterating over arrays and manipulating data structures to format and display character names.
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

By leveraging these concepts, the script efficiently retrieves, processes, and displays Star Wars characters from the specified movie using the Star Wars API, showcasing proficiency in working with external APIs and managing asynchronous code in JavaScript.

## Requirements
- Allowed editors: vi, vim, emacs
- Files interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- Mandatory README.md file at the root of the project folder
- Code should be semistandard compliant with semicolons and AirBnB style
- All files must be executable
- Length of files will be tested using `wc`
- Not allowed to use `var`

## Additional Resources
- [Mock Technical Interview](https://www.algoexpert.io/mock-interview)
- [Semi-Standard Documentation](https://github.com/standard/semistandard)
- [Request Module Documentation](https://www.npmjs.com/package/request)

## Tasks
### 0. Star Wars Characters
Write a script `0-starwars_characters.js` that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID, for example, `3` corresponds to "Return of the Jedi".
- Display one character name per line in the same order as the `characters` list in the `/films/` endpoint.
- Must use the Star Wars API
- Must use the `request` module
