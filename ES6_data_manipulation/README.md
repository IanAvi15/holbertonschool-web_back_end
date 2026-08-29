# ES6 Data Manipulation

## Description

This project covers advanced array and data structure manipulation techniques introduced in ES6+ JavaScript. It focuses on functional array methods and the specialized data structures available for handling collections of data.

## Learning Objectives

At the end of this project, you are expected to be able to explain the following, without the help of Google:

- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The `Set`, `Map`, and `WeakMap` data structures

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `node 20.x.x` and `npm 9.x.x`
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files end with a new line
- Code uses the `.js` extension
- Code is tested using `Jest` and the command `npm run test`
- Code is verified against lint using `ESLint`
- All functions must be exported

## Setup

### Install NodeJS 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Verify the installation:

```bash
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```

### Install Jest, Babel, and ESLint

In the project directory:

```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

Then install all dependencies:

```bash
npm install
```

## Usage

Run a file:

```bash
npm run dev <filename>.js
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

## Author

Ian Aviles