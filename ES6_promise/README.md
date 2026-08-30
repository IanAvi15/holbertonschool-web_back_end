# ES6 Promise

## Description

This project covers asynchronous JavaScript programming using Promises and the `async`/`await` syntax introduced in ES6+.

## Learning Objectives

At the end of this project, you are expected to be able to explain the following, without the help of Google:

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The `await` operator
- How to use an `async` function

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `node 20.x.x` and `npm 9.x.x`
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
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
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
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

## Response Data Format

`uploadPhoto` returns a response with the format:

```js
{
  status: 200,
  body: 'photo-profile-1',
}
```

`createUser` returns a response with the format:

```js
{
  firstName: 'Guillaume',
  lastName: 'Salva',
}
```

## Author

Ian Aviles