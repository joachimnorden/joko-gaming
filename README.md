
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

**Epic: Admin/Store Owner**

| ID  | Content                                                                                                                                                   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | As a **store owner** I want to be able to log in so that I can have full access to the store                                                              |
| 2   | As a **store owner** I want to be able to add new products so that I can add new items to my store                                                        |
| 3   | As a **store owner** I want to be able to add new categories so that items is easy to find                                                                |
| 4   | As a **store owner** I want to be able to add FAQ's to the site so that I can answer questions a user might have                                          |
| 5   | As a **store owner** I want to be able to edit/update a product so that I can change product prices, descriptions, images and other product criteria      |
| 6   | As a **store owner** I want to be able to edit/delete categories so that I can change category names and keep the site up to date                         |
| 7   | As a **store owner** I want to be able to edit/delete FAQ's so that I can change questions and answers                                                    |

**Epic: Navigation**

| ID  | Content                                                                                                                                                   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8   | As a **shopper** I want to be able to easily navigate through the site so that I can view desired content                                                    |
| 9   | As a **shopper** I want to be able to quickly identify deals so that I can take advantage of special saving on products                                      |
| 10  | Aa a **shopper** I want to be able to view a list of products so that I can select some to purchase                                                          |
| 11  | As a **shopper** I want to be able to view a specific category of products so that I can quickly find products without having to search through all products |
| 12  | As a **shopper** I want to be able to sort products by rating, price and name so that I can easily find what I'm looking for                                 |
| 13  | As a **shopper** I want to be able to search for a product by name or description so that I can find a specific product i'd like to purchase                 |
| 14  | As a **shopper** I want to be able to easily see what i've searched for and the number of results so that I can see whether the product I want is available  |
| 15  | As a **shopper** I want to be able to view individual product details so that I can see the price, description, product rating, product image and reviews    |
| 16  | As a **shopper** I want to be able to read FAQ's so that I can find answers to common questions before or after purchase                                     |

**Epic: Purchase**
| ID | Content |
| --- | ------------------------------- |
| 17 | As a **shopper** I want to be able to easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong quantity |
| 18 | As a **shopper** I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will recieve         |
| 19 | As a **shopper** I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout             |
| 20 | As a **shopper** I want to be able to easily enter my payment information so that I can checkout quickly and with no hassles                                         |
| 21 | As a **shopper** I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes                                |
| 22 | As a **shopper** I want to be able to recieve an email confirmation after checking  so that I can keep the confirmation of what I've purchased for my records        |

**Epic: User Interaction**

| ID  | Content                                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 23  | As a **user** I want to be able to see ratings and reviews of products so that I can read the opinions of other users                  |
| 24  | As a **user** I want to be able to sign up for a newsletter so that I can keep track of newly added products and sales                 |
| 25  | As a **user** I want to be able to unsubscribe from the newsletter so that I can stop recieving emails it i've lost interest           |
| 26  | As a **logged-in User** I want to be able to leave ratings and reviews so that I can share my experience with others                   |
| 27  | As a **logged-in User** I want to be able to save selected products to my whishlist so that I can remember what i've been interested in |

**Epic: Accounts**

| ID  | Content                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------------ |
| 28  | As a **user** I want to be able to easily register for an account so that I can have a personal account and be able to view my profile                                   |
| 29  | As a **user** I want to be able to easily login or logout so that I can access my personal account information                                                           |
| 30  | As a **user** I want to be able to easily recover my password in case i forgot it so that I can recover access to my account                                             |
| 31  | As a **user** I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful                      |
| 32  | As a **user** I want to be able to have a personalized user profile so that I can view my personal order history and order confirmations and save my payment information |

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