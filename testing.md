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

#### Testing Navigations

**If the user is not logged in**

- When you open the app, you should see the main page. [x]
- Click on the "Home" button. You should see the home page. [x]
- Click on the "Recipes" button. You should see the recipes page. [x]
- Click on the "Register" button. You should see the register page. [x]
- Click on the "Login" button. You should see the login page. [x]

**If the user is logged in**

 - When you open the app, you should see the main page. [x]
 - Click on the "Home" button. You should see the home page. [x]
 - Click on the "Recipes" button. You should
 see the recipes page. [x]
 - Click on the "Profile" button. You should see the profile page. [x]
 - Click on the "Logout" button. You should see the login page. [x]

 **If the user has admin permissions**

 - When you open the app, you should see the main page. [x]
 - Click on the "Home" button. You should see the home page. [x]
 - Click on the "Recipes" button. You should see the recipes page. [x]
 - Click on the "Profile" button. You should see the profile page. [x]
 - Click on the "Manage Categories" button. You should see the manage categories page. [x]
 - Click on the "Logout" button. You should see the login page. [x]



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

#### **Bug 1** 
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

#### **Bug 2**
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

#### **Bug 3** 
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


#### **Bug 4**
- Description: **The delete category button would only delete the first category and not the selected category**

* Fix: The section of code uses a for loop to iterate through the categories and a modal that pops up when the user clicks the delete button to ask the user if they want to delete the category. The for loop was duplicating the objectID of the categories and was causing the bug. I resolved the bug by adding the objectID to the anchor and modal ID.

* Test: The user can now delete the category they selected.


#### **Bug 5**
- Description: **When the user edits a category the edited category is there but so is the old category**

* Fix: the issue was I had copied the `add_category.html` file as a template for the `edit_category.html` file. This caused the bug because the action in the form tag was directing to `{{ url_for('add_category') }}` when it should have directed to `{{ url_for('edit_category') }}`. I resolved the bug by changing the action to `{{ url_for('edit_category') }}`.

* Test: The user can now edit the category they selected  and it is updated in the database.

#### Unsolved Bugs

No noticed unresolved bugs during testing on all devices.
