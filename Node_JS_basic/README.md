# Node JS Basic

## Description

This project covers the fundamentals of running JavaScript with Node.js, including modules, file reading, command line arguments, environment variables, and building small HTTP servers with both plain Node.js and Express.

## Learning Objectives

At the end of this project, you are expected to be able to explain the following, without the help of Google:

- Run JavaScript using NodeJS
- Use NodeJS modules
- Use a specific Node JS module to read files
- Use `process` to access command line arguments and the environment
- Create a small HTTP server using Node JS
- Create a small HTTP server using Express JS
- Create advanced routes with Express JS
- Use ES6 with Node JS with Babel-node
- Use Nodemon to develop faster

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using `node` (version 20.x.x)
- All files end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code uses the `.js` extension
- Code is tested using `Jest` and the command `npm run test`
- Code is verified against lint using `ESLint`
- Code needs to pass all the tests and lint — verify the entire project by running `npm run full-test`
- All functions/classes are exported using this format: `module.exports = myFunction;`
- The following files are included in the repository: `package.json`, `babel.config.js`, `.eslintrc.js`, and `database.csv`

## Setup

Install dependencies:

```bash
npm install
```

## Usage

Run a file:

```bash
node <filename>.js
```

Run in dev mode (with Babel + Nodemon):

```bash
npm run dev
```

Run tests:

```bash
npm run test
```

Run lint:

```bash
npm run lint
```

Run the full test suite (lint + tests):

```bash
npm run full-test
```

## Provided Files

- `database.csv` — sample student data used across several tasks
- `package.json` — project scripts and dependencies
- `babel.config.js` — Babel configuration for ES6 support
- `.eslintrc.js` — ESLint configuration

## Tasks

| # | Task | File |
|---|------|------|
| 0 | Executing basic javascript with Node JS | `0-console.js` |

## Author

Ian Aviles