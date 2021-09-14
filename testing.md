# RecipePod - Testing section

[Main README.md file for RecipePod](README.md)

## Table of Contents

1. [**Manual Tests**](#manual-testing)
2. [**Client Stories Tests**](#client-stories-tests)
3. [**Automated Tests**](#automated-tests)
4. [**Bugs**](#bugs)
   - [**Solved Bugs**](#solved-bugs)
   - [**Unsolved Bugs**](#unsolved-bugs)

## Manual Tests

### Tests on Laptop

**All tests on laptop were repeated in Chrome and Firefox on two different screen sizes.**

### Tests on Mobiles and tablets

**All tests were performed on this developers Xiaomi mi 10 mobile device and iPad. All tests done on Laptop were performed on the mobile devices. Below are the specific tests for mobile devices.**

## Client Stories Tests

#### As a user, I want:

## Automated Tests

These were the validation services use to check the projects code.

- [W3C Markup Validation](https://validator.w3.org/) was used to check the HTML.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to check the CSS.
- [JSHint](https://jshint.com/) was used to check the JavaScript

## Bugs

#### Solved Bugs

**Bug 1** 
- Description: **The user can't see the recipe's category name when on the recipe page** 

* Fix: In the app.py file, within the the add_recipe view, the category_name key was incorrectly set to category.

    <div align="center">
    <img src="static/images/bug1.png">
    </div>

* This was easily fixed by changing the category key to category_name.

    <div align="center">
    <img src="static/images/bug1-fix.png">
    </div>

* Test: The user can now see the recipe's category name when on the recipe page.

    <div align="center">
    <img src="static/images/bug1-fix2.png">
    </div>

**Bug 2**
- Description: **The navbar was being covered by the page content**

    <div align="center">
    <img src="static/images/bug2.png">
    </div>

* Fix: The bug was resolved by adding a z-index of 5 to ensure there would be no overlap.

    <div align="center">
    <img src="static/images/bug2-fix.png">
    </div>

* Test: The navbar is no longer covered by the page content.

    <div align="center">
    <img src="static/images/bug2-fix2.png">
    </div>

**Bug 3** 
- Description: **The User Can't see their recipes they uploaded on their profile**

    <div align="center">
    <img src="static/images/bug3.png">
    </div>

* Fix: The bug was resolved by changing `{"created_by": session["user"].capitalize()}` to `{"created_by": session["user"].lower()}`
    - This was done because the session["user"] was being set to the capitalized version of the user's name. This was causing the user's name to be read incorrectly which made the code think the user hadn't created any recipes.

* Test: The user can now see their recipes they uploaded on their profile.

    <div align="center">
    <img src="static/images/bug3-fix.png">
    </div>


#### Unsolved Bugs

No noticed unresolved bugs during testing on all devices.
