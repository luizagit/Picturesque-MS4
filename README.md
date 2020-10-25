# Picturesque-MS4

![# Milestone 4 - Picturesque-MS4](design/picturesque_mockup.jpg)

This full-stack website represents the last milestone project I designed at Code Institute Full Stack Development course, specifically the Full Stack Frameworks with Django.

## Deployment website

[Click here to view the project live](https://picturesque-app-ms4.herokuapp.com)

## The Goal of This Website
The idea behind Picturesque project was building an e-commerce web application targeting my personal photos that will feature the ability to filter based on desired photography category, a live functional payment system, a complete authentication ecosystem that includes email confirmation and user profile, finally real time notifications to complete our user's experience.

The web application is carved into the following sections:
- Home page. It presents what the website has to offer by inviting the user to explore the photo collections 
- Login/Registration page. Allow users to sign in or sign up. 
- Store page. It gives our users the possibilty to filer based on price, rating, category or simply explore all photos.
- Gallery page. It is focused on the artwork side by offering the ability to only choose for viewing specific photography topics including deals or new shots with the business element in mind to quickly sort based on price low to high or high to low, rating, name or category.
- Photo Detail page. After clicking/choosing a photo the user lands on a page focused on that particular photography where there is a title, price, category, rating, description, a quantity adjustment mechanism, possilibity to add the photo to the photobag for future purchase and of course a botton to go back and explore other pics that will hopefully share the same fate. 
- Photo Bag page. Here the user can see a summary of the photos he/her is willing to purchase and can further adjust the quantity, see the total sum in euro for the photos, delivery cost involved and this can be 0 if a certain threshold is met, the secure checkout button that will send the user to the final step before he/her can enjoy the purchased bits of art.
- Checkout page. Here is the checkout form that needs to be filled with the user details regarding identification, delivery address and payment card info. The user can also get in touch with the order details emphasizing the items in the photobag that are about to be purchased.
- Profile page. It is the section where user's default delivery information and order history are preserved.
- Picturesque Management page. Here the web application superuser/django admin can add photos.

## UX
### Exploring Photos and Navigation
- As a customer, I would like to view all the photos available and be able to select the ones that resonate with my taste.
- As a customer, I would like to view the photo in its original size. 
- As a customer, I would like to view specific photo details including price, description and rating.
- As a customer, I would like to quickly identify deals in order to take advantage of special savings and also see the latest photo additions.
- As a customer, I would like to view the total of my purchases at any time in order to avoid spending more than what I intend to do.

### Sorting and Searching
- As a customer, I would like to sort the list of available photos using criterias such as high or low rating, high to low or low to high price, specific category/topic.
- As a customer, I would like to sort a specific category/topic of photos and find within the best rated or best priced items.
- As a customer, I would like to sort multiple categories/topics of photos and find within the best rated or best priced items.

### Purchasing and Checkout
- As a customer, I would like to easily adjust the quantity of a photo when purchasing it.
- As a customer, I would like to view the photos in my photobag to be purchased and identify the total cost and also granulary cost per photo.
- As a customer, I would like to experience an easy to use and clear payment system that will give me assurance regarding online security. 
- As a customer, I would like to check out quickly and with no difficulties in understanding the required payment form paramters.
- As a customer, I need to feel that my personal data and payment information is safe in order to confidently provide the needed parameters to make a purchase. 
- As a customer, I would like to view the order confirmation after checkout to verify there are no mistakes introduced in the process.
- As a customer, I would like to receive after checkout an email confirmation in order to keep the confirmation of what I have purchased for my records.

### Registration and User Accounts

- As a user, I would like to easily register for a personal account where I should be able to see my profile data.
- As a user, I would like to easily login to access my personal account information or logout.
- As a user, I would like to easily recover my password in case I forget it.
- As a user, I would like to receive an email confirmation after I register in order to verify that my account registration was successful.
- As a user, I would like to have a personalized user profile where I can view my order history and order confirmations and also save my payment information for the ease of future purchases.

### Administration and Picturesque Store Management

- As a superuser/admin, I would like to have the ability to add a new photo.
- As a superuser/admin, I would like to have the ability to edit or update photo characteristics like price, description etc.
- As a superuser/admin, I would like to have the ability to delete a photo.



