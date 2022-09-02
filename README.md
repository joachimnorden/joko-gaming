
# Table of Contents 
1. [UX](#ux)
    - [Strategy](#strategy)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)
    - [Wireframes](#wireframes)
    - [Database schema](#database-schema)
    - [Models](#models)

4. [Web marketing](#web-marketing)
    - [Newsletter](#newsletter)
    - [Facebook](#facebook)
    - [SEO](#seo)

5. [Surface](#surface)

6. [Technologies Used](#technologies-used)

7. [Code validation](#code-validation)

8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)

11. [Credits](#credits)


responsive image and link to live site


# About
This is a full-stack e-commerce project built using Django, Python, HTML, CSS and JavaScript. I have created a website for 'Joko Gaming' that has been designed to sell gaming products such as mouses, keyboards and headsets.


#
# UX
## Strategy
The target audience for 'Joko Gaming' are:

- parents who would like to buy quality gaming accessories to their children
- Young adults, age 15 - 25

These users will be looking for:
- An informative website, with information that is easy-to-find & concise
- A website that offers high-end, quality computer accessories
- Ability to view & purchase computer accessories that are for sale
- Ability to make a user account in order to see billing history, make a whishlist and write reviews 
- A way to sign up for the Joko Gaming newsletter

This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

## User Stories


# Scope

## Features

### **Home Page**

*Navigation bar:*
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Products', 'Categories' and 'sales' and icons for search bar, account and shopping bag

*Account - Login/Register:*
- The Login/Register feature is located in the upper right corner and offers the user to log in or register for an account as well as log out of the site
- When the user is logged in the links for 'Login' and 'Register' will instead be 'My Profile' and 'Logout', add Whishlist
- The admin user has extra access that allow them to add, update and remove products from the store

*Shopping bag:*
- The shopping bag is always visible for the user in the top right corner throughout all the pages. An easy access to see what has been added, update the quantity or remove products from the shopping bag.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screens

*Hero:*
- A big hero-image advertising what the website is about
- A 'Shop Now' button for fast access to the products

*Testimonails*
- A carousel with testimonials from industry professionals and customers

*Footer:*
- Appears on every page with links to social media, FAQ's, shipping info and privacy policy
- Social media links are opened in a new tab to avoid dragging users from the site

### **Products**

- The products page shows all products available for purchase
- Each product has an image, title, rating and price
- The site will paginate all products display 10 at a time
- Each product card will take a user to the product details page 


### **Categories**

- Categories dropdown from navbar, allowing the user to access specific categories
- Categories: 
    - Headsets
    - Mouses
    - Keyboards
    - Other

### **Sales**

- Fast access to see products with a discount.

### **Product Details Page**
- The Product Details Page displays all the information about the selected product
- Product info will be image, title, rating, category and description
- Users will be able to add product to the shopping bag or whishlist aswell as change quantity.
- A Commenting section is located at the bottom available to all. Logged in users can also leave a comment

### **Checkout Page**
- The checkout page is accessible through the shopping bag
- A user can enter and save their personal details, see a summary of what's in the shopping bag and enter their card credentials to finish the purchase.

### **Admin User**
- Admin user can preform full CRUD functionalliy without having to enter the default 'admin panel' from django. 
- Admin user can add products from a 'Product Management' link in the account menu from the navigation bar 
- Admin user can edit/delete products from the products page and product details page