# JavaScript DOM Manipulation

## Overview
This project focuses on learning and practicing DOM manipulation using vanilla JavaScript. It covers selecting elements, modifying styles and content, handling events, and fetching data from APIs. The tasks progressively build your ability to interact dynamically with the DOM without reloading the HTML page.

---

## Resources
Before starting, these resources are recommended to understand the fundamentals:

- What is JavaScript?
- Introduction to the DOM
- Document Interface
- Element Class
- Locating DOM elements using selectors
- CSS Selectors
- CSS Diner (interactive selector game)
- DOM Scripting
- Network Requests
- Troubleshooting JavaScript

---

## Learning Objectives
By the end of this project, you will be able to:

- Select HTML elements using JavaScript
- Understand differences between ID, class, and tag name selectors
- Modify element styles and content dynamically
- Manipulate the DOM by adding/removing elements or classes
- Make network requests using `XMLHttpRequest` and the Fetch API
- Listen and respond to DOM and user events

---

## Requirements
- Use any code editor of your choice
- All files must run on Chrome (version 57.0 or later)
- Files should end with a newline character
- Include a `README.md` with meaningful project info in the root folder
- Code must follow semi-standard JavaScript style (no `var` usage)
- The page must not reload on any DOM manipulation or data fetching action

---

## Tasks Breakdown

### 0. Color Me
- Change header text color to red (#FF0000) using `document.querySelector`.

### 1. Click and Turn Red
- When the element with `id="red_header"` is clicked, change the header text color to red.

### 2. Add `.red` Class
- Add the `red` CSS class to the header when `id="red_header"` is clicked.

### 3. Toggle Classes
- Toggle header's class between `red` and `green` on click of `id="toggle_header"`.
- Header should always have exactly one class (`red` or `green`).

### 4. List of Elements
- Add a new `<li>Item</li>` to the `<ul class="my_list">` when clicking the element with `id="add_item"`.

### 5. Change the Text
- Update the header text to "New Header!!!" when clicking the element with `id="update_header"`.

### 6. Star Wars Character
- Fetch the name of the Star Wars character from `https://swapi-api.hbtn.io/api/people/5/?format=json`.
- Display the name inside the element with `id="character"` using the Fetch API.

### 7. Star Wars Movies
- Fetch all Star Wars movies from `https://swapi-api.hbtn.io/api/films/?format=json`.
- List their titles inside the `<ul id="list_movies">`.

### 8. Say Hello!
- Fetch the translation of "hello" from `https://hellosalut.stefanbohacek.dev/?lang=fr`.
- Display the translated word inside the element with `id="hello"`.
- The script should work when included in the `<head>` tag.

---

## Usage

1. Open the provided HTML files in Chrome.
2. Link the corresponding JavaScript files (e.g., `0-script.js`, `1-script.js`, etc.)
3. Interact with the page elements as described in each task.
4. Observe dynamic DOM updates and fetch results.

---

## Repository Structure

holbertonschool-higher_level_programming/
└── javascript-dom_manipulation/
├── 0-script.js
├── 1-script.js
├── 2-script.js
├── 3-script.js
├── 4-script.js
├── 5-script.js
├── 6-script.js
├── 7-script.js
├── 8-script.js
└── README.md


---

## Notes
- All DOM manipulation should be done using JavaScript without page reload.
- Use modern JS syntax (ES6+), avoid `var`.
- Use `document.querySelector` and related DOM APIs.
- Use the Fetch API for network requests and handle promises correctly.
