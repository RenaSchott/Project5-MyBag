# MyBag

MyBag is an ecommerce website where different bags for different occassions can be bought.

The site includes helpful features such as a profile, about us and forums page.

Returning customers can make a faster checkout and they can see their order history. They can find useful informations in the forum and about us section.

![Responsivness](readme-images/responsivness.png)

View the live project here: <https://mybag-731453a72029.herokuapp.com/>


## Table of content

- [MyBag](#mybag)
  - [Table of content](#table-of-content)
  - [UX](#ux)
    - [Website owner goals](#website-owner-goals)
    - [E-commerce application type](#e-commerce-application-type)
    - [Agile planning](#agile-planning)
      - [Milestones](#milestones)
      - [User stories](#user-stories)
      - [Wireframes](#wireframes)
      - [Flow Chart](#flow-chart)
      - [Method](#method)
        - [POC (prove of concept)](#poc-(prove-of-concept))
        - [MVP (minimum viable product)](#mvp-(minimum-viable-product))
    - [Five planes of UX](#five-planes-of-UX)
      - [Strategy](#strategy)
      - [Scope](#scope)
      - [Structure](#structure)
      - [Skeleton](#skeleton)
      - [Surface](#surface)
  - [Features](#features)
    - [About us](#about-us)
    - [Checkout](#checkout)
    - [Checkout complete](#checkout-complete)
    - [Login](#login)
    - [Footer](#footer)
    - [Forum](#forum)
    - [Message](#message)
    - [Navbar/Header](#navbar/header)
    - [Forum post](#forum-post)
    - [Productmanagement](#productmanagement)
    - [Product details](#product-details)
    - [Profile](#profile)
    - [Shoppingcart](#shoppingcart)
    - [Welcome screen](#welcome-screen)
    - [Features left to implement](#features-left-to-implement)
  - [SEO](#seo)
    - [Search results for keywords](#search-results-for-keywords)
    - [Long-tail keyword testing](#long-tail-keyword-testing)
    - [Search for similar businesses](#search-for-similar-businesses)
  - [Marketing strategies](#marketing-strategies)
    - [Social media marketing](#social-media-marketing)
    - [Email marketing](#email-marketing)
  - [Used Technologies](#used-technologies)
    - [Framework, Libraries and Programs](#framework-libraries-and-programs)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)


## UX

### Website owner goals

As the owner of the website I want to sells different bags for everyone:
- Within the first two month I want to sell 100 bags.
- Within the first six month I want to have 100 registered repeat buyers and I want to sell 1000 bags.
- Each month I want to have at least 100 persons visiting my website.

### E-commerce application Type

- **Who is the customer?:**  
    - It is a business to customer model (B2C). We have to attract the consumers to choose to make impulsive purchases. Our customers are going to be of all kind of genders and all ages. People who want to buy quality bags anytime or those who want to buy a bargain can find what they are looking for on the website. Therefore the customers can get different kinds of informations on the products on our website. 
- **What will they buy?:** 
    - The physical products we are selling are different bags for different occassions and customers.
- **How will they pay?:** 
    - The customers can pay via one time payment. They can save their payment methods to make it easier for the next time.
- **Type:** 
    - Our application type is a typical online shop (e-commerce).

![The Business Model Canvas](readme-images/business-model-p5.png)

### Agile planning

The development of this project was done with an agile approach.

Here is an example of the Kanban board from an early development stage:
![Example of the Kanban board in an early stage](readme-images/kanban.png)

The project board can be found here: <https://github.com/users/RenaSchott/projects/5>.

#### Milestones
- **Preparation for P5:** All the preparation User Stories etc. is done for P5.
- **Deployment:** Early and final deployment for P5.
- **Viewing and navigation:** Built the site and fill it with products.
- **Registration and User Accounts:** Mahe a registration possible and create the user accounts with everything needed.
- **Sorting and Searching:** Make the site usable for shoppers.
- **Purchasing and Checkout:** Make the checkout and purchase of products possible
- **Admin and Store Management:** Make the site usabke for the store owner

The milestones can be found here <https://github.com/RenaSchott/Project5-MyBag/milestones>.

#### User stories

The user stories can be found here <https://github.com/RenaSchott/Project5-MyBag/issues>.

- As a developer I want to be able to write User Stories, Milestones and set up the Kanban Board for the project so that I can keep track of the progress of the project.
- As a developer I want to be able to use wireframes, flowchart and ERD so that I can built the wanted site.
- As a developer I want to be able to deploy my project early so that I can find problems and avoid stress in the end.
- As a developer I want to be able to finish the Readme File so that I can finish the project.
- As a developer I want to be able to make the final deployment so that I can submit a working project.
- As a shopper I want to be able to view a list of products so that I can select some to purchase.
- As a shopper I want to be able to view individual product details so that I can identify the price, description, product rating and product image.
- As a shopper I want to be able to quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I’d like to purchase.
- As a shopper I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.
- As a site user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.
- As a site user I want to be able to easily login or logout so that I can access my personal account information.
- As a site user I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
- As a site user I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful.
- As a site user I want to be able to have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information.
- As a shopper I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
- As a shopper I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
- As a shopper I want to be able to sort multiples categories of products simultaneously so that I can find the best-priced or best-rated products across broad categoried, such as „school bags“.
- As a shopper I want to be able to search for a product by name or description so that I can find a specific product I’d like to purchase.
- As a shopper I want to be able to easily see what I’ve searched for and the number of results so that I can quickly decide whether the product I want is available.
- As a shopper I want to be able to easily select quantity of a product when purchasing it so that I can ensure I don’t accidentially select the wrong product or quantity.
- As a shopper I want to be able to view items in my shopping cart to be purchased so that I can identify the total cost of my purchase and all items I will receive.
- As a shopper I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a shopper I want to be able to easily enter my payment information so that I can check out quickly and with no hassle.
- As a shopper I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
- As a shopper I want to be able to view an order confirmation after checkout so that I can verify that I haven’t made any mistakes.
- As a shopper I want to be able to receive an email confirmation after checking out I want to be able to  so that I can keep the confirmation of what I’ve purchased for my records.
- As a store owner I want to be able to add a product so that I can add new items to my store.
- As a store owner I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
- As a store owner I want to be able to delete a product so that I can remove items that are no longer for sale.
- As a store owner I want to be able to add/edit/delete a category so that I can change the items available in my store.
- As a store owner I want to be able to add/edit/delete advertisements so that I can promote different product or campaign.

#### Wireframes

Here are the drawings of the wireframes for the browsers and for smartphones:

**Homepage:**
![Drawing of the homepage](readme-images/wireframe1.png)
![Drawing of the homepage](readme-images/wireframe2.png)

**Register:**
![Drawing of the register page](readme-images/wireframe3.png)
![Drawing of the register page](readme-images/wireframe4.png)

**Log In:**
![Drawing of the log in page](readme-images/wireframe5.png)
![Drawing of the log in page](readme-images/wireframe6.png)

**Product Page:**
![Drawing of the product page](readme-images/wireframe13.png)
![Drawing of the product page](readme-images/wireframe14.png)

**Shopping Cart:**
![Drawing of the shopping cart](readme-images/wireframe7.png)
![Drawing of the shopping cart](readme-images/wireframe8.png)

**Personal user page:**
![Drawing of the personal user page](readme-images/wireframe11.png)
![Drawing of the personal user page](readme-images/wireframe12.png)

**Add review:**
![Drawing of the add review page](readme-images/wireframe9.png)
![Drawing of the add review page](readme-images/wireframe10.png)


#### Flow Chart

Here is the outlined flow chart:

![Drawn flowchart of the project](readme-images/flowchart-p5.png)

#### Entity Relationship Diagram

Here is the outlined ERD:

![Drawn entity relationship diagram of the project](readme-images/erd-p5.png)

#### Method

##### POC (prove of concept)

- Register
- Log in and out
- Adding reviews with ratings
- View items
- Edit shopping cart
- Edit items
- Edit categories
- Authentification
- payment method
- search and filter function
- image storage

##### MVP (minimum viable product)

- Search and filter items and categories
- Interacting with item
    - details
- Create new account
- Logging in and out of the page
    - Make a new order
        - Adding items
        - Deleting items
        - Change amount of items
    - View orders
        - view order list
        - view order details
        - view shipping and payment status
    - View personal details
        - Edit shipping adress
        - Edit billing adress
        - Edit payment method
- View shopping cart
    - via hover
        - view short overview
    - via clicking
        - view details
        - edit amount of each item
        - delete item
- Edit items/categories
    - delete
    - edit
    - add
        - images
        - description
        - amount    


### Five planes of UX

#### Strategy
The users are identified as parents or persons from around 10 to 65 years old which are used to order online and are in need for a new bag. Their needs are different bags on a site with simple and easy selection, payment methods, authentication system and information on the bags.

#### Scope
To achieve the strategy, we must bring online an easy to handle website. Therefore, we need a visible search bar as well as the information on free shipping displayed on the homepage. A menu for category filtering for women, men, children, occasions and sales must be included. The wanted products must show the minimum needed information such as price, material, image and rating for the customer to narrow down the wanted product. The product detail page should show everything needed for a purchase which includes the price, material, image, rating and the option to choose the amount wanted. The shopping bag, should be easily visible on the pages, as well as the option to register or login. In the shopping bag, all selected products must be visible with price and the chosen amount as well as the option to change the amount. The total price and the option for check out should be easily visible. An intuitive purchasing process must be included with different payment options and the purchase confirmation. For details, the [features](#features) section can be viewed.

#### Structure
For the interaction design, the user is actively requested on the homepage to start their shopping experience, which shows them all the available products. Before or after choosing this option, the user can use the search for specific materials or bag type or the category filter. The users can view all the details before their purchase.
For the information architecture, the potential customer can see all minimum needed information in the displayed list of products and more on the detailed products page.
Authenticated users can store their information.

#### Skeleton
As most common, the navigation, filter, register, login and search bars are within the top lines of the website. Number of search results are displayed in the left corner of the main section and the search results themselves are displayed in rows and column are adapted to the respective screen size, and they can be sorted. Which means in general, that standard layouts are used, which the users should be familiar with. The thoughts on the look of the website can be seen in the [wireframes](#wireframes) section.

#### Surface
For the font family Roboto is used and for the color scheme a beige background should smooth the black and white color scheme of the upper lines. The font color of the main part of the screen is black or dark red which gives a nice contrast to the white of the product card and the main background color.
All relevant options and information are altogether sorted in intuitive groups. 
The images and icons are mainly used to help navigation and for product details. Therefore, only necessary ones are used. 


## Features

Images are showing fullscreen and mobile screen.
The background color of nearly every page is a warm beige.

### About us

- The about us page gives an overview of the attitude of the company and it gives the user the opportunity to contact to company.
- The chosen colors are dark red for the text and grey for the line.

![Screen shot of about us page of the project](readme-images/aboutus.png)
![Screen shot of about us page of the project](readme-images/aboutusm.png)

### Checkout

- The checkout page gives the user the opportunity to review there ongoing purchase and to add their personal and payment information to complete their order.
- Saved personal information are integrated automatically. The user can edit them
- The chosen colors are mainly black and dark red.

![Screen shot of checkout page of the project](readme-images/checkout1.png)
![Screen shot of checkout page of the project](readme-images/checkout2.png)
![Screen shot of checkout page of the project](readme-images/checkout1m.png)
![Screen shot of checkout page of the project](readme-images/checkout2m.png)

### Checkout complete

- The checkout complete pages gives an overview of the completed purchase with every information displayed.
- The chosen colors are mainly black and dark red.

![Screen shot of ceckout complete page of the project](readme-images/checkoutcomplete.png)
![Screen shot of ceckout complete page of the project](readme-images/checkoutcompletem.png)

### Login

- The login page as an example of the styling of the allauth templates give the user the opportunity to login or to go to the register page.
- The template has a grey background ontop of the beige site background and the color is mainly white.

![Screen shot of an exemplary allauth page of the project](readme-images/exemplaryallauthtemplate.png)
![Screen shot of exemplary allauth page of the project](readme-images/exemplaryallauthtemplatem.png)

### Forum

- The forum page displays the forum entries as a list with their image, title, excerpt from the content, release date and the opportunity to view the complete post.
- Users can filter the posts via category.
- The background of each post is reen brown which gives a nice contrast to the site background and the black text color.

![Screen shot of forum page of the project](readme-images/forum.png)
![Screen shot of forum page of the project](readme-images/forumm.png)

### Message

- To get a better UX messages comment the users most important clicks.
- The user themself can close the message.
- The message has a white and slightly transparent background and the text color is red to get the users attention.

![Screen shot of an exemplary message of the project](readme-images/messageexample.png)
![Screen shot of an exemplary message of the project](readme-images/messageexamplem.png)

### Navbar/Header

- The header contains links to every page on the website where the user has access to it. Some menu part are collapsable on large screens and the wohle menu is collapsable on mobile view.
- For better readability only white and black was used.

![Screen shot of the navbar of the project](readme-images/navbar.png)
![Screen shot of the navbar screen of the project](readme-images/navbarm.png)

### Footer

- The footer gives the user the opportunity the visit the facebook page, read the privacy policy and to subscribe to the newsletter.
- The chosen colors are mainly black and white for better readability.

![Screen shot of the footer of the project](readme-images/footer.png)
![Screen shot of the footer of the project](readme-images/footerm.png)

### Forum post

- The detailed view of a forum post displays next to image, title, authot and release date, the whole content.
- The User can go back to the forum. or read a comment below the forum post.
- The authenticated users can leave a comment.
- The chosen colors are white as the background for the comments section and dark red and black for the text color.

![Screen shot of forum post of the project](readme-images/post1.png)
![Screen shot of forum post of the project](readme-images/post2.png)
![Screen shot of forum post of the project](readme-images/post1m.png)
![Screen shot of forum post of the project](readme-images/postm2.png)

### Productmanagement

- Authenticated superusers can add new products.
- Chosen colors are black and dark red.

![Screen shot of productmanagement page of the project](readme-images/productmanagement.png)
![Screen shot of productmanagement page of the project](readme-images/productmanagement2.png)
![Screen shot of productmanagement page of the project](readme-images/productmanagementm.png)
![Screen shot of productmanagement page of the project](readme-images/productmanagement2m.png)

### Product details

- The user can view every needed product detail for a purchase. They can choose to go back to products page or to add the product to the shopping cart.
- The authenticate superusers can choose to edit or delete this product.
- Chosen colors are black, white and mainly dark red.

![Screen shot of product detail page of the project](readme-images/productsdetail.png)
![Screen shot of product detail page of the project](readme-images/productsdetailm.png)

### Products

- Users can sort the products.
- All selected products are displayed with some information and the opportunity to go to the detail product page for more information.
- Users can see how many products are displayed. More information as category can be displayed at this place if chosen by the user.
- An arrow up in the bottom right corner brings the user back to the top of the page.
- The authenticate superusers can choose to edit or delete specific products.
- Chosen colors are black, white and dark red.

![Screen shot of products page of the project](readme-images/productspage.png)
![Screen shot of products page of the project](readme-images/productspagem.png)

### Profile

- Users can view their profile with their personal and order information.
- Personal information can be edited and updated.
- Order information are listed. The order number can be clicked for more details.
- Chosen colors are mainly black and dark red.

![Screen shot of profile page of the project](readme-images/profile.png)
![Screen shot of profile page of the project](readme-images/profile1m.png)
![Screen shot of profile page of the project](readme-images/profile2m.png)

### Shoppingcart

- Users can view their shopping cart.
- Main details are displayed.
- Products can be deleted or the user can update the wanted quantity.
- User can choose to go back to the products page or start the checkout.
- Chosen colors are black, white and dark red.

![Screen shot of products page of the project](readme-images/productspage.png)
![Screen shot of products page of the project](readme-images/productspagem.png)

### Welcome screen

- Welcomes the user and gives them the opportunity to start their shopping experience via button clicking.
- The background image is colorful and it should arouse the visitor's interest.

![Screen shot of the welcome screen of the project](readme-images/homepage.png)
![Screen shot of the welcome screen of the project](readme-images/homepage-m.png)

### Features left to implement

There is the possibility to integrate:

- **V2 (version 2)**
    - Advertisement
        - Add
        - Delete
        - Edit
    - Comment Management
        - Edit
        - Delete
    - Category Management
        - Add
        - Delete
        - Edit


## SEO

The Search Engine Optimization is a process to improve the visibility of the website during a fitting search on a search engine like Google. Improving the visibility helps to attrackt more potential customers.

### Search results for keywords
| Keywords                                    | Search results (approximately) |
| ------------------------------------------- | ------------------------------ |
| bag                                         | 6.690.000.000                  |
| bag for daily use                           | 2.370.000.000                  |
| bag for daily use for men                   | 1.150.000.000                  |
| bag for daily use for women                 | 2.080.000.000                  |
| bag for daily use for children              | 2.030.000.000                  |
| everyday bag                                | 864.000.000                    |
| business bag                                | 12.340.000.000                 |
| leather business bag                        | 189.000.000                    |
| event bag                                   | 2.080.000.000                  |
| sport bag                                   | 2.080.000.000                  |
| durable sport bag                           | 70.700.000                     |
| gym bag                                     | 434.000.000                    |
| school bag                                  | 1.540.000.000                  |
| bag as stylish gift                         | 210.000.000                    |
| bag as usefull gift                         | 173.000.000                    |
| bagpack                                     | 10.300.000                     |
| bagpack for women                           | 3.670.000.000                  |
| bagpack for men                             | 4.360.000.000                  |
| bagpack for children                        | 281.000.000                    |
| bagpack for daily use                       | 393.000.000                    |
| bagpack for daily use for men               | 143.000.000                    |
| bagpack for daily use for women             | 390.000.000                    |
| bagpack for daily use for children          | 264.000.000                    |
| everyday backpack                           | 69.500.000                     |
| backpack as stylish gift                    | 51.900.000                     |
| sport backpack                              | 131.000.000                    |
| backpack for school                         | 1.390.000.000                  |
| backpack for school girl                    | 115.000.000                    |
| backpack for school boy                     | 77.100.000                     |
| backpack as useful gift for school students | 517.000.000                    |

### Long-tail keyword testing

For the long-tail keyword testing the website Wordtracker was used. Examplary results are shown below. The competition and volume was not in general low. That is why the keywords used as meta tags were chosen based on these results and the results of the [Search results for keywords](#search-results-for-keywords).

![seo1](readme-images/seo1.png)

![seo2](readme-images/seo2.png)

![seo3](readme-images/seo3.png)

### Search for similar businesses

For comparison, different pages with different layouts were viewed. 
For example: zalando.de, bonprix.de, rucksack.de, taschenkaufhaus.de

## Marketing strategies

Paid marketing strategies were no options and requirements for this fictional project that is why the main strategies used are social media and email marketing to adress people of different ages and preferences. 

### Social media marketing

You can see below a mock facebook page where the promotion takes place with regular posts about our new collections and sales. This provides a chance for the customers to feel more connected with the business and stay easily informed about new sales or collections without the need to visit the main page regularly.

![facebookpage](readme-images/facebookpage.png)

### Email marketing

In the footer section of the main page a newsletter sign up section is included. Therefore the MailChimp Newsletter subscription service is used. The sign up is easy and completely optional.

## Used Technologies

### Framework, Libraries and Programs

- Frameworks  were used to speed up
    - Django
    - Bootstrap

- Libraries & Moduls
    - jQuery
    - Gunicorn
        - was used as python http server for WSGI applications
    - Pyscopg2
        - was used as PostgresSQL Database adapter
    - Pillow
        - was used for python imaging
    - Boto2
        - was used for integration with AWS services
    - Django-storages
        - was used as collection of custom storage backends for Django
    - Django-allauth
        - was used to create user authentication
    - Django-crispy-forms/Crispy-bootstrap5
        - was used to control rendering behavior of Django forms
    - Whitenoise
        - was used to serve static non-media files
    

- Programs
    - Balsamiq
        - was used to create the wireframes
    - Lucidchart
        - was used to create the flow chart
    - dbdiagram
        - was used to create the entity relationship diagram
    - GitHub
        - was used to store the project site
    - Gitpod
        - was used to write the code and commit it to GitHub
    - Heroku 
        - was used to deploy the project  
    - Validator W3
        - was used to validate the HTML
    - Validator W3C
        - was used to validate the CSS
    - JSHint
        - was used to validate the JavaScript
    - CI Python Linter
        - was used for finding errors
    - AWS (Amazon Web services (S3))
        - was used to host staic and media files
    - Wordtracker
        - was used for long-tail keyword testing
    - Languagetool
        - was used to check the spelling and grammar in the README file.
    - Stripe
        - was used as online payment platform
    - Gmail
        - was used for real email sending
    - Mailchimp
        - was used for automated newsletter subscription
    - Sitemap generator
        - was used for better SEO
    - Privacy Policy Generator
        - was used for SEO


## Testing

Testings can be found here: [TESTING.md](TESTING.md)


## Deployment

The deployment was done after the tutorial in the course content using [Heroku](https://www.heroku.com/), [AWS](https://aws.amazon.com/de/), [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) and [Whitenoise](https://whitenoise.readthedocs.io/en/latest/).

For deployment:
- some libraries have to be installed - for details see [Used Technologies](#used-technologies)
- create a new database <https://dbs.ci-dbs.net/>
- A Heroku account must be created.
- Set your GitHub repository to public.
- Create a db with CI database Maker.
- Hide sensitive information in the env.py with the .gitignore file and update the settings.py file.
- Within the project:
    - Connect to database
    - Create database tables
    - Add shop fixtures
    - Create a superuser
- Create an AWS Account and within set the IAM and S3 up for the project.
    - host static and media files
- Create a new app in Heroku with the following settings:
    - Add the DATABASE_URL to config vars in settings.
    - Add the SECRET_KEY and other config vars
    - Add AWS Keys
    - - The Heroku App must be linked to the correct repo in GitHub
    - Choose Automatic Deploys for easier handling.
    - Then deploy

The link to the live page can be found here: (<https://mybag-731453a72029.herokuapp.com/>)


## Credits

### Content

The content of this project was inspired by the "Boutique Ado" project and the content of the course. In general, the following websites were used for inspiration:
  - <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django>
  - <https://docs.djangoproject.com/en/4.2/ref/contrib/flatpages/>
  - <https://www.w3schools.com/>
  - <https://getbootstrap.com/docs/5.3/getting-started/introduction/>
  - <https://docs.djangoproject.com/>
  - <https://stackoverflow.com/>
  

Inspirations for specific problems were taken from the following websites:
  - <https://espere.in/Django-Allauth:-How-to-create-social-login-like-Facebook-Google-Github-and-Twitter-in-django/>
  - <https://docs.allauth.org/en/latest/installation/quickstart.html>
  - <https://www.strategyzer.com/library/the-business-model-canvas>
  - <https://docs.djangoproject.com/>
  - <https://stackoverflow.com/questions/16285939/aligning-li-next-to-each-other-not-working>
  
### Media

Images were downloaded from <https://pixabay.com/de/>

## Acknowledgements

- I would love to thank the following persons:
  - My mentor for his support
  - My facilitator for her support
  - The slack community for their fast answers and support