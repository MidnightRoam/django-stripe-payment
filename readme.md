# A few words about the web application
### Online video game store with Stripe payment system connected, written in Python, Django as backend and CSS, JavaScript as frontend
#### Functionality implemented so far:
<ul>
    <li>Search for products from the database</li>
    <li>Sort products by tags</li>
    <li>Buying goods through API Stripe using sessions</li>
    <li>Adding an item to the cart</li>
    <li>Adding a product to favorites</li>
    <li>Display screenshots of the product and its tags on the product page</li>
    <li>Display the number of users who added a particular product to favorites</li>
    <li>Display of the average product rating based on user reviews</li>
    <li>Adding a User Review to a Product</li>
    <li>Registration of new users</li>
</ul>

# Deployed application address
### http://midnightuser.pythonanywhere.com
# Getting started
## Using Docker:
#### 1. Select a hard drive location where the project will be located

#### 2. Paste this command into the terminal

    git clone https://github.com/MidnightRoam/django-stripe-payment

#### 3. Paste this commands into the terminal
To deploy a project

    docker-compose build
To start a project

    docker-compose up

### That's all you need to getting started


## Start without Docker:
#### 1. Select a hard drive location where the project will be located

#### 2. Paste this command into the terminal

    git clone https://github.com/MidnightRoam/django-stripe-payment

#### 3. From the root of the project, paste this command into the terminal:

    pip install -r requirements.txt

#### 4. After installing all dependencies paste this commands into the terminal:
    
    cd service 
    python manage.py migrate
    python manage.py runserver

### That's all you need to getting started without Docker
