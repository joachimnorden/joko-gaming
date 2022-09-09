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

5. [Design](#design)

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

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-startpage.jpg" width="1000" height="100%">
</p>

### **Products**

- The products page shows all products available for purchase
- Each product has an image, title, rating and price
- Each product card will take a user to the product details page 

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-products.jpg" width="1000" height="100%">
</p>


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

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-pdv.jpg" width="1000" height="100%">
</p>

### **Checkout Page**
- The checkout page is accessible through the shopping bag
- A user can enter and save their personal details, see a summary of what's in the shopping bag and enter their card credentials to finish the purchase.

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-checkout.jpg" width="1000" height="100%">
</p>

### **User Profile**

- A logged-in user can access Profile page, Wishlist and Change Password from the navbar
- The profile page is where the user can update their default shipping/billing address and see order history
- Wishlist displays the list of items the user has saved to their wishlist, with the ability to remove the product from the list

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-user-account.jpg" width="400" height="100%">
</p>

### **Admin**

- Admin can preform full CRUD functionalliy without having to enter the default 'admin panel' from django
- Admin can add products from 'Product Managment' link in the account menu from the navigation bar
- Admin can add category from 'Product Managment' link
- Admin can add FAQ's from 'FAQ's' link
- Admin can edit/delete products from products page and products details page
- Admin can edit/delete FAQ from 'FAQ Management' and FAQ's page, mark them as published or draft

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-admin-panel.jpg" width="1000" height="100%">
</p>

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
<img src="assets/documents/readme_docs/visual-sitemap-joko-gaming.jpg" width="1000" height="100%">
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

# Marketing 
- Links to all the social media sites can be found both in the footer.
- The facebook link takes you to the Joko Gaming business page which can be found [here](https://www.facebook.com/Joko-Gaming-104812362377260/).

<p align="center">
<img src="assets/documents/readme_docs/joko-gaming-facebook-page.jpg" width="1000" height="100%">
</p>

- The newsletter sign up form can also be found in the footer

<p align="center">
<img src="assets/documents/readme_docs/newsletter-signup-form.jpg" width="1000" height="100%">
</p>

# Search Engine Optimisation
I have created a sitemap.xml and robots.txt file to help search engines locate the site. To keep user's information safe, any pages that could contain sensitive information has been disallowed in the robots.txt.


# Design

## Design choice
Bootstrap provides a flexible framework for building upon and wherever possible its structure has been used and modified to achieve the desired functionality and feel.

## Color schema

The color scheme is dark with green as a contrast color.

Color pallet from [Colors](https://coolors.co/139035-696969-ffd700-d7b500-252525)

- #14B582 - green color for main call to action and new labels
- #0F0F0F - used as a background color with opacity to highlight footer and hero text
- #EA2020- used for sale labels
- #D7B500 - used for review stars
- #555555 - used as font color

<p align="center">
<img src="assets/documents/readme_docs/Colors.jpg" width="1000" height="100%">
</p>

The aim was to provide a solid colour base which could bring the other elements on the site to life.

## Fonts 
- Russo One Slab - Used onas logo, headers and in navbar
- Lato - main font 


# Technologies Used

## Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)


## Frameworks, Libraries & Programs Used
[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[AWS](https://aws.amazon.com/) – was used to store static files 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project

[Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

[Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[jQuery](https://jquery.com/) - Used to write JS code

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Balsamiq](https://balsamiq.com/) - was used to create site wireframes.

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - was used to validate HTML

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - was used to validate CSS

## Extensions 

[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - was used to to create, configure, and manage AWS services

[Pillow](https://pillow.readthedocs.io/en/stable/) - This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

[Stripe](https://stripe.com/docs) - was used to make and process payments

## Deployment

### Github

First you will need to create a new repository.

1. Log into Github.
2. On the 'Repositories' tab click 'New'. This takes you to the create a new repository page.
3. Name the repository and click 'Create repository'.
4. Your new repository is now set up and ready to use.

#### Forking

To fork the project you must;
1. Sign in to Github and go to my [repository](https://github.com/Iris-Smok/JoyfulBookstore-PP5)
2. Locate the Fork button at the top right of the page.
3. Click the button then click 'Create fork'. 
4. The fork is now in your repositories.

#### Clone
To clone the project you must;

1. Sign in to Github and go to my [repository](https://github.com/Iris-Smok/JoyfulBookstore-PP5)
2. Above the list of files click 'Code'.
3. This will bring up a few options as to how you would like to clone. You can select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
4. Open git bash
5. Type 'git clone' and then paste the URL you copied. Press Enter.

For more information on cloning check out the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Django

This project uses the Django framework. To install django, follow these steps:

1. In your IDE type the command:  
    `pip3 install django`
2. Then to name your project type:  
    `django-admin startproject *Your project name here*`  
This will add your django project folder to your file explorer
3. Next you will need to add a gitignore file. To do this enter the command line:  
    `touch .gitignore`
4. Inside this file add these 3 lines:  
    ``` 
    *.sqlite3
    *.pyc
    __pycache__
    ```
5. To check everything is up and running, run the command:  
    `python3 manage.py runserver`
    This should expose port 8000. Open that port and you should be welcomed by Django's success page.
6. Next you need to perform the initial migrations. This is done by running the command:
    `python3 manage.py migrate`
7. Finally, in order to have access to the admin panel you will need to create a superuser. This is done by running the command:
    `python3 manage.py createsuperuser`
    This will then ask you to create a username and password with an optional email address.
8. Once these steps are completed you can push your changes to github by running the commands, in order:
    ```
    git add .
    git commit -m "initial commit"
    git push
    ```

#### All Auth

Inside the django framework is a package called Allauth. This package handles all the registration and sign in processes. The steps to install Allauth can be found [here](https://django-allauth.readthedocs.io/en/latest/installation.html).



### Heroku

Heroku is used to deploy the final project.

1. First you will need to sign in to Heroku. If you do not have an account you can sign up for free [here](https://signup.heroku.com/).
2. Once you are logged in, click the button 'New' and select 'Create new app'.
3. Name the app, then select what region is closest to you and click 'Create App'.
4. Then on the resources tab, navigate to the 'Add-ons' section and search for 'Heroku Postgres'.
5. Select 'Heroku Postgres', then under 'Plan name' choose 'Hobby Dev - Free' and click 'Submit Order Form'.

To use Postgres you will need to install dj_database_url and psycopg2. This should be done in whatever IDE you are using.

1. In your IDE type the command:  
    `pip3 install dj_database_url`
2. Then once that is installed type the command:  
    `pip3 install psycopg2-binary`
3. Then, to make sure Heroku install all your apps requirements when you deploy it, run the command:  
    `pip3 freeze > requirements.txt`
4. Next, navigate to your setting.py file in your main project folder. At the top of the file add the line:  
    ```
    import dj_database_url
    ```
5. Then scroll down the file till you find your database settings. Comment out the default configuration and underneath insert the code:  
    ```
    DATABASES = {
        'default': dj_database_url.parse(*Enter Database URL here*)
    }
    ```
    The database URL can be found in the settings tab of your app in heroku, under Config Vars. Make sure to have the link in quotation marks.  
    **Important!** If you want to migrate any data from your current database to the Postgres database in Heroku, make sure you run this line before connecting to Postgres:  
    `./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`  
6. Once that's saved, you will now need to run migrations because you have connected to a new database. This is done by running the command:  
    `python3 manage.py migrate`
    If you had previously saved your data to import into the postgres database, you can now run the command:  
    `./manage.py loaddata db.json`
7. Now that's setup you will now need to create a superuser for the new database. The command is:  
    `python3 manage.py createsuperuser`
    *Note, once the superuser is created, it's a good idea to sign into the admin panel, locate the user, and check the option that says their email is verified. This is needed otherwise Allauth won't allow the user to sign into the store.* 
8. Before you commit these changes, you will need to remove the Databases section in the settings.py and uncomment the original database. This is to stop your Postgres database URL from ending up in version control.
9. Now we can create an if statement in our settings.py to run the postgres database when using the app on heroku or sqlite if not. Scroll back to the database section and refactor the code to look like this:  
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
    ```
10. Next we will have to install another package called gunicorn, which will act as our web server. To do so, run the command:  
    `pip3 install gunicorn`
    And then remember to freeze the requirements with:  
    `pip3 freeze > requirements.txt`
11. Now we can create our Procfile to tell Heroku to create a web dyno. In your root directory create a file named 'Procfile' and inside insert the code:  
    `web: gunicorn **'your_projects_name_here'**.wsgi:application
12. Then, back in heroku, navigate to settings and in the config vars input the key DISABLE_COLLECTSTATIC with the value 1, and click 'Add'.
This is to stop heroku from collecting any static files when you deploy.
13. You will also need to add heroku to your allowed hosts in your settings.py. Back in your project, in the settings file, scroll down to ALLOWED_HOSTS, and inside the brackets insert the url to your app, followed by 'localhost'. It should look something like this:     
    ```
    ALLOWED_HOSTS = ['your-project-name.herokuapp.com', 'localhost']
    ```
14. Now add, commit and push these changes, followed by a push to heroku with the command:  
    `git push heroku main'
    Your app will now be deployed, albeit without any static files, but this will be fixed when setting up AWS, documented below. 
15. If you want your project to be automatically deployed to heroku when pushing your work to github you can. To do so, In heroku go to the deploy tab, and in the 'deployment method' section connect it to github. You will need to search for your repository and once found click 'connect'. Then scroll down and click 'Enable automatic deploys'. Now when you push to github your code will automatically deploy to Heroku as well. 


### AWS

Amazon web services are used to store all our static and media files. 

#### S3

1. First you will need to sign up to AWS which you can do [here](https://aws.amazon.com/).
2. Once you have created an account and logged in, under the All Services>Storage menu, click the link that says S3.
3. On the S3 page you will need to create a new bucket. To do this click the orange button that says 'Create Bucket'.
4. Name the bucket and select the closest region to you. To keep things simple I recommend naming the bucket after your project's name.
5. Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred. 
6. Uncheck the 'Block all public access' checkbox and check the warning box to acknowledge that the bucket will be made public, then click create bucket. 
7. Once created, click the bucket's name and navigate to the properties tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
8. Now navigate to the permissions tab, scroll down to the Cross-origin resource sharing (CORS) section, click edit and paste in the following code:  
    ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
9. Then scroll back up to the 'Bucket Policy' section. Click 'edit' and then 'Policy generator'. This should open the AWS policy generator page.
10. From here under the 'select type of policy' dropdown menu, select 'S3 Bucket Policy'. Then inside 'Principle' allow all principals by typing a *.
11. From the 'Actions dropdown menu select 'Get object'. Then head back to the previous tab and locate the Bucket ARN number. Copy that, return to the policy generator and paste it in the field labelled Amazon Resource Name (ARN).
12. Once that's completed click 'Add statement', then 'Generate Policy'. Copy the policy that's been generated and paste it into the bucket policy editor.
13. Before you click save, add a '/*' at the end of your resource key. This is to allow access to all resources in this bucket.
14. Once those changes are saved, scroll down to the Access control list (ACL) section and click 'edit'.
15. Next to 'Everyone (public access)', check the 'list' checkbox. This will pop up a warning box that you will also have to check. Once that's done click 'save'. 

#### IAM

1. Now that your bucket is ready we need to create a user to access it. In the search bar at the top of the window, search for IAM and select it.
2. Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'.
3. Name the group 'manage-*your-project-name*' and click 'Create group' at the bottom of the page. 
4. Then from the sidebar click 'Policies', then 'Create policy'.
5. Go to the JSON tab and click 'import managed policy'. Search for 'S3' and select 'AmazonS3FullAccess' and click import.
6. Once this is imported you will need to edit it slightly. Go back to your bucket and copy your ARN number. Head back to this policy and update the Resource key to include your ARN, and another line with your ARN followed by a /*. It should end up looking something like this: 
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "YOUR-ARN-NO-HERE",
                    "YOUR-ARN-NO-HERE/*"
                ]
            }
        ]
    }
    ```
7. Click 'Next: Tags', 'Next: Review', and on this page give the policy a name. This could be something as simple as the project name followed by the word policy, and then a short description eg: Access to S3 bucket for 'YOUR PROJECT' static files. Then click 'Create policy'. 
8. This will take you back to the policy page where you should be able to see your newly created policy. Now we need to attach it to the group we created.  
9. Click 'User groups', and click the group you created earlier. Go to the permissions tab and click 'Add permission' and from the dropdown click 'Attach policies'. 
10. Find the policy you just created, select it and click 'Add permissions'.
11. Finally you need to create a user to put in the group. Select users from the sidebar and click 'Add user'.  
12. Give your user a user name, check 'Programmatic Access', then click 'Next: Permissions'. 
13. Select your group that has the policy attached and click 'Next: Tags', 'Next: Review', then 'Create user'.
14. On the next page, download the CSV file. This contains the user's access key and secret access key which you will need later. 

#### Connecting AWS to django

Now that you have created a S3 bucket with its user group attached, we need to connect it to django.

1. First you will need to install two packages. Boto3 and Django storages. Do this by running these commands:  
    ```
    pip3 install boto3
    pip3 install django-storages
    ```
    And remember to freeze the requirements with:  
    ```
    pip3 freeze > requirements.txt
    ```
2. You will then need to add 'storages' to your installed apps section inside your settings.py file. Do that now. 
3. Next, we will need to add some additional settings to the same file to let django know what bucket it's communicating with. 
4. Somewhere near the bottom of the file you should write an if statement to check if there is an environment variable called USE_AWS. This variable does not exist yet but we will add it later. Inside the if statement, write the following settings so it looks like this:  
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
        AWS_S3_REGION_NAME = 'insert-your-region-here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```
5. Next, hop back to heroku and in the settings tab, under config vars, you will need to add some keys with values that were downloaded earlier in the CSV file.
6. Add the key, AWS_ACCESS_KEY_ID with the value that was generated in the CSV file earlier. Then add the key AWS_SECRET_ACCESS_KEY, and again add the value that was generated in the CSV file. Once they have both been added, add the key USE_AWS, and set the value to True.
7. You can now also remove the DISABLE_COLLECTSTAIC variable, since django should now collect static files automatically and upload them to S3.
8. Now head back to the settings.py file in your django project and head back to the if statement we wrote earlier and inside the statement add this line setting:  
    ```
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
    This is to tell django where our static files will be coming from in production.
9. Next we need to create a file to tell django that we want to use S3 to store our static files whenever someone runs collectstatic and also that we want any uploaded product images to go there also.
10. In the root directory of your project create a file called 'custom_storages.py'. Inside this file you will need to import your settings as well as the s3boto3 storage class. So at the top of the file insert the code:  
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    ```
11. Then underneath the imports insert these two classes:  
    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
    The STATICFILES_LOCATION and MEDIAFILES_LOCATION have yet to be defined, so lets do that now.
12. Back in the settings.py file, underneath the bucket config settings but still inside the if statement, add these lines:  
    ```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    ```
13. Next, you will also need to override and explicitly set the URLs for static and media files using your custom domain and new locations. To do this add these two lines inside the same if statement:  
    ```
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
14. If you now save, add, commit and push your changes, you should see that your S3 bucket now has a static folder with all your static files inside. Next, we need to handle the Media files but first, inside the if statement add the following code. This helps to speed things up by letting the browser know that its ok to cache static files for a long time:    
    ```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    ```
15. Back in S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'. 
16. Inside the new media folder you just created, click 'Upload', 'Add files', and then select all the images that you are using on your site.
17. Then under 'Permissions' select the option 'Grant public-read access' and click upload. You may need to also check an acknowledgment warning checkbox too. 
18. Once that is finished you're all set. All your static files and media files should be automatically linked from django to your S3 bucket.

s
### Stripe

Stripe is needed to handle the checkout process when a payment is made. You will need a stripe account which you can sign up for [here](https://stripe.com/en-gb).

#### Payments

1. To set up stripe payments you can follow their guide [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

#### Webhooks

1. To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
2. Then in the side-nav under the Developers title, click on 'Webhooks', then 'Add endpoint'.
3. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:  
    ```
    https://your-app-name.herokuapp.com/checkout/wh/
    ```
4. Then click '+ Select events' and check the 'Select all events' checkbox at the top before clicking 'Add events' at the bottom. Once this is done finish the form by clicking 'Add endpoint'.
5. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
6. Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
7. Add these values under these keys:  
    ```
    STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
    STRIPE_SECRET_KEY = 'insert your secret key'
    STRIPE_WH_SECRET = 'insert your webhooks secret key'
    ```
8. Finally, back in your setting.py file in django, insert the following near the bottom of the file:  
    ```
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```

# Credits

### Content 

All product data (name, description, price, images) are taken from [Best Buy](https://bestbuy.com/)

### Media
All images were taken from [Pexels](https://www.pexels.com/)

## Acknowledgements

- Big thanks to everybody from the Code Institute Slack community 
- Big thanks to my friends and family for supporting me