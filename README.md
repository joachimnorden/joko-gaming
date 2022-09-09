<h1 align="center">Joko Gaming</h1>

You can find live site [here](https://joko-gaming.herokuapp.com/)

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
| 1   | As a **store owner** I want to be able to **log in** so that I can **have full access to the store**                                                              |
| 2   | As a **store owner** I want to be able to **add new products** so that I can **add new items to my store**                                                        |
| 3   | As a **store owner** I want to be able to **add new categories** so that I can **make items is easy to find**                                                                |
| 4   | As a **store owner** I want to be able to **add FAQ's to the site** so that I can **answer questions a user might have**                                          |
| 5   | As a **store owner** I want to be able to **edit/update a product** so that I can **change product prices, descriptions, images and other product criteria**      |
| 6   | As a **store owner** I want to be able to **edit/delete categories** so that I can **change category names and keep the site up to date**                         |
| 7   | As a **store owner** I want to be able to **edit/delete FAQ's** so that I can **change questions and answers**                                                    |

**Epic: Navigation**

| ID  | Content                                                                                                                                                   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8   | As a **shopper** I want to be able to **easily navigate through the site** so that I can **view desired content**                                                    |
| 9   | As a **shopper** I want to be able to **quickly identify deals** so that I can **take advantage of special saving on products**                                      |
| 10  | Aa a **shopper** I want to be able to **view a list of products** so that I can **select some to purchase**                                                          |
| 11  | As a **shopper** I want to be able to **view a specific category of products** so that I can **quickly find products without having to search through all products** |
| 12  | As a **shopper** I want to be able to **sort products by rating, price and name** so that I can **easily find what I'm looking for**                                 |
| 13  | As a **shopper** I want to be able to **search for a product by name or description** so that I can **find a specific product i'd like to purchase**                 |
| 14  | As a **shopper** I want to be able to **easily see what i've searched for and the number of results** so that I can **see whether the product I want is available**  |
| 15  | As a **shopper** I want to be able to **view individual product details** so that I can **see the price, description, product rating, product image and reviews**    |
| 16  | As a **shopper** I want to be able to **read FAQ's** so that I can **find answers to common questions before or after purchase**                                     |

**Epic: Purchase**
| ID | Content |
| --- | ------------------------------- |
| 17 | As a **shopper** I want to be able to **easily select the quantity of a product when purchasing it** so that I can **ensure I don't accidentally select the wrong quantity** |
| 18 | As a **shopper** I want to be able to **view items in my bag to be purchased** so that I can **identify the total cost of my purchase and all items I will recieve**         |
| 19 | As a **shopper** I want to be able to **adjust the quantity of individual items in my bag** so that I can **easily make changes to my purchase before checkout**             |
| 20 | As a **shopper** I want to be able to **easily enter my payment information** so that I can **checkout quickly and with no hassles**                                         |
| 21 | As a **shopper** I want to be able to **view an order confirmation after checkout** so that I can **verify that I haven't made any mistakes**                                |
| 22 | As a **shopper** I want to be able to **recieve an email confirmation after checking** so that I can **keep the confirmation of what I've purchased for my records**        |

**Epic: User Interaction**

| ID  | Content                                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 23  | As a **user** I want to be able to **see ratings and reviews of products** so that I can **read the opinions of other users**                  |
| 24  | As a **user** I want to be able to **sign up for a newsletter** so that I can **keep track of newly added products and sales**                 |
| 25  | As a **user** I want to be able to **unsubscribe from the newsletter** so that I can **stop recieving emails it i've lost interest**           |
| 26  | As a **logged-in User** I want to be able to **leave ratings and reviews** so that I can **share my experience with others**                   |
| 27  | As a **logged-in User** I want to be able to **save selected products to my whishlist** so that I can **remember what i've been interested in** |

**Epic: Accounts**

| ID  | Content                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------------ |
| 28  | As a **user** I want to be able to **easily register for an account** so that I can **have a personal account and be able to view my profile**                                   |
| 29  | As a **user** I want to be able to **easily login or logout** so that I can **access my personal account information**                                                           |
| 30  | As a **user** I want to be able to **easily recover my password in case i forgot it** so that I can **recover access to my account**                                             |
| 31  | As a **user** I want to be able to **receive an email confirmation after registering** so that I can **verify that my account registration was successful**                      |
| 32  | As a **user** I want to be able to **have a personalized user profile** so that I can **view my personal order history and order confirmations and save my payment information** |

# Scope

## Features

### **Homepage**

*Navigation bar:*
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Products', 'Categories' and 'special offers' a search bar and icons for account and shopping bag

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

*Testimonials*
- A testimonials sections having comments and recommendations from industry professionals and customers

*Footer:*
- Appears on every page with links to social media, newsletter sign up form, FAQ's, shipping info and privacy policy
- Social media links are opened in a new tab to avoid dragging users from the site

### **Products**

- The products page shows all products available for purchase
- Each product has an image, title, rating and price
- Each product card will take a user to the product details page 


### **Categories**

- Categories dropdown from navbar, allowing the user to access specific categories
- Categories: 
    - Headset
    - Mouse
    - Keyboard
    - Other

### **Special Offers**

- Special Offers dropdown from Navbar, allowing the user to access specific offer
- From the dropdown menu user can select :
    - Sale
    - New arrivals

### **Product Details Page**
- The Product Details Page displays all the information about the selected product
- Product info will be image, title, rating, category and description
- Users will be able to add product to the shopping bag or whishlist aswell as change quantity and colors if available.
- A Commenting section is located at the bottom available to all. Logged in users can also leave a comment

### **Checkout Page**
- The checkout page is accessible through the shopping bag
- A user can enter and save their personal details, see a summary of what's in the shopping bag and enter their card credentials to finish the purchase.

### **User Profile**

- A logged-in user can access Profile page, Wishlist and Change Password from the navbar
- The profile page is where the user can update their default shipping/billing address and see order history
- Wishlist displays the list of items the user has saved to their wishlist, with the ability to remove the product from the list

### **Admin**

- Admin can preform full CRUD functionalliy without having to enter the default 'admin panel' from django
- Admin can add products from 'Product Managment' link in the account menu from the navigation bar
- Admin can add category from 'Product Managment' link
- Admin can add FAQ's from 'FAQ's' link
- Admin can edit/delete products from products page and products details page
- Admin can edit/delete category from 'Category Management' link
- Admin can edit/delete FAQ from 'FAQ Management' and FAQ's page, mark them as published or draft


## Future Features

- Add a subscribtion model to gaming guides and tutorials
- Add product image carousel on product detail page


# Structure

Simplicity helps users to quickly and easily access the app and navigate within the app.

The website is made from 7 apps:

- Products
- Checkout
- Home
- Profiles
- Faq
- Bag
- Wishlist


## Sitemap

<p align="center">
<img src="assets/documents/README_docs/visual-sitemap-joko-gaming.jpg" width="1000" height="100%">
</p>

## Wireframes

All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes are linked here:

- [Homepage](assets/documents/readme_docs/301725581_5445706365465377_2612677724086160542_n.png)
- [Product list page](assets/documents/readme_docs/300514560_588530342950907_6639597091498167681_n.png)
- [Product details page](assets/documents/readme_docs/301692060_560646862515226_8829632733422704231_n.png)
- [Shopping bag](assets/documents/readme_docs/286304102_2231528163671681_6884067683633208498_n.png)
- [Checkout](assets/documents/readme_docs/300977215_605713857785279_1259445599883392670_n.png)
- [Sign in](assets/documents/readme_docs/304799689_1000221404006645_6853603326264657597_n.png)

## Database schema

<p align="center">
<img src="assets/documents/readme_docs/QuickDBD-export.png" width="1000" height="100%">
</p>

# Business Model

This is an e-commerce store with a B2C (Business to Consumer) model, as the business is selling products, guides and tutorials directly to consumers