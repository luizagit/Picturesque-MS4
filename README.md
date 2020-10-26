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
### Project Target Audience

- People who love the art of photography and don't mind spending money for it.

### Business goals:

- Provide users with a secure professional e-commerce online shop
- Make profit from selling my personal photos

### Exploring Photos and Navigation

- As a customer, I expect to access the website from any device, so that I can use the website anytime and anywhere.
- As a customer, I expect to easily navigate the website, so that I can quickly find what I'm looking for.
- As a customer, I want to easily access social media links of the website owner, so that I can read more information about the business overall.
- As a customer, I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
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

- As a customer, I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.
- As a customer, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
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

- As a superuser/admin, I would like to have the ability to add a new photo in the front end or back end.
- As a superuser/admin, I would like to have the ability to edit or update photo characteristics like price, description etc. in the front end or back end.
- As a superuser/admin, I would like to have the ability to delete a photo in the front end or back end.

## Utilised Technologies

- HTML, CSS and JavaScript.
- Bootstrap - to create responsive, mobile-first front-end web development components.
- Visual Studio Code - the IDE of choice.
- Django - full fledged web framework following the model-template-views architectural pattern.
- Django-crispy-forms - to help with managing Django forms and adjust various forms properties on the backend.
- Django-countries - which was used for the country field that provides all ISO 3166-1 countries as choice for the users.
- Django-allauth - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- Django-storages - a collection of custom storage backends for Django that was used with Amazon S3 integration in our website.
- Dj-database-url - used for integration with Heroku PostgreSQL.
- Stripe - payment processing software and application programming interface for e-commerce websites and mobile applications.
- Pillow - Python Imaging Library, it was used to add support for opening, manipulating, and saving images.
- Psycopg2 - PostgreSQL database adapter for the Python programming language
- Flake8 - for checking the code base against coding style (PEP8), programming errors.
- JQuery - JavaScript library.
- Gunicorn - Web Server Gateway Interface (WSGI) server implementation was used to run the Python application on Heroku.
- Heroku - an ecosystem of cloud services, which can be used to instantly extend applications with fully-managed services, it was used to deploy Picturesque application production version.
- Amazon AWS - to store application content such as media files, static assets, and photo uploads for use by Heroku deployment hence offloading the storage of static files from Heroku app's dynos ephemeral filesystem.

## Deployment
### Local Deployment

Picturesque project was developed using Visual Studio Code IDE and using Git & GitHub for version control. It is hosted on the Heroku platform with static, media files and photo uploads being hosted in AWS S3 Basket.
To be able to run this project, the following tools have to be installed:
- An IDE of your choice, I used [Visual Studio Code](https://code.visualstudio.com/) for creating this project
- [Git](https://git-scm.com/), [Python3](https://www.python.org/downloads/), [Pip3](https://pypi.org/project/pip/)
Apart from that, you also need to create accounts with the following services:
- [Stripe](https://stripe.com/)
- [Amazon AWS](https://signin.aws.amazon.com) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Gmail](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp) account

1. At the top of this repository, click the green button **Clone or download**.
2. In the Clone with HTTPs section, copy the clone URL for the repository.
3. Change the current working directory to the location where you want the cloned directory to be made.
4. Type git clone, and then paste the URL you copied in Step 2.
5. Press Enter. Your local clone will be created.
6. To create a virtual environment within project directory enter:<br/>
`python3 -m venv .venv`<br/>
7. Taking Visual Studio Code as example, type:<br/>
`code .`<br/>
8. Edit `~/.bashrc` by adding the following env vars:<br/>
`export DEVELOPMENT=True`<br/>
`export SECRET_KEY="<Your Secret key>"`<br/>
`export STRIPE_PUBLIC_KEY="<Your Stripe Public key>"` <br/>
`export STRIPE_SECRET_KEY="<Your Stripe Secret key>"` <br/>
9. Install all required modules from requirements.txt with the command<br/>
`python3 -m pip install -r requirements.txt`<br/>
10. In the terminal in your IDE migrate the models to crete a database using the following commands:<br/>
`python3 manage.py makemigrations --dry-run`<br/>
`python3 manage.py makemigrations`<br/>
`python3 manage.py migrate --plan`<br/>
`python3 manage.py migrate`<br/>
11. Load the data fixtures (**categories** and **photos**) in that order into the database using the following commands:<br/>
`python manage.py loaddata categories`<br/>
`python manage.py loaddata photos`<br/>
12. Create a superuser to have access to the admin panel (you need to follow the instructions and insert username, email and password):<br/>
`python3 manage.py createsuperuser`<br/>
13. You will now be able to run the application using the following command:<br/>
`python3 manage.py runserver 0.0.0.0:8000`<br/>
14. To access the admin panel, you can add the **/admin** path at the end of the url link and login using your superuser credentials.

### Heroku Deployment

To start Heroku Deployment process, you need to clone the project as described in the **Local deployment** section above.
To deploy the project to [Heroku](https://dashboard.heroku.com/apps) the following steps need to be completed:

The website was deployed on [Heroku](https://dashboard.heroku.com/apps) following these steps:

1. Create a **requirements.txt** file, which contains a list of the dependencies, using the following command in the terminal:<br/>
`python3 -m pip freeze --local > requirements.txt`<br/>
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:<br/>
`web: gunicorn picturesque_ms4.wsgi:application`<br/>
3. `git add -A`, `git commit -m "<message>`, `git push` the files to the Github repositoty of this project.
4. Other modules that are required for the Heroku deployment and have to be installed: **gunicorn** (WSGI HTTP Server), **dj-database-url** for database connection and **Psycopg** (PostgreSQL driver for Python). All of the mentioned above are already installed in this project and mirrored in the **requirements.txt** file.
5. Go to Heroku and create a new app. Set a name for this app and select the closest region.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Provision** button to add it to your project.
5. Choose Deployment method as GitHub in Heroku Dashboard and link the Github repository to the Heroku app.
6. Go to **Settings** then **Reveal Config Vars** in Heroku Dashboard and set the values as follows:

| config vars                   | values                                        | 
| ------------------------------|-----------------------------------------------|
| AWS_ACCESS_KEY_ID             | <your_aws_access_key>                         |
| AWS_SECRET_ACCESS_KEY         | <your_aws_secret_access_key>                  | 
| HEROKU_POSTGRESQL_RED_URL     | <your_postgres_database_url>                  |
| EMAIL_HOST_PASS               | <your_email_password_generated_by_gmail>      |
| EMAIL_HOST_USER               | <your_email_address>                          |
| IP                            | 0.0.0.0                                       |
| SECRET_KEY                    | <your_secret_key>                             |
| STRIPE_PUBLIC_KEY             | <your_stripe_public_key>                      |
| STRIPE_SECRET_KEY             | <your_stripe_secret_key>                      |
| STRIPE_WH_SECRET              | <your_stripe_webhook_key>                     |
| USE_AWS                       | True                                          |



