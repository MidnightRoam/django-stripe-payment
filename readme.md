# A few words about Pixel Playground
### Ecommerce video game store with Stripe payment system connected, written in Python, Django as backend and CSS, JavaScript as frontend part
### <a href="http://uladzislau.pythonanywhere.com/">OPEN SITE IN BROWSER</a>
#### What has been implemented so far:
#### Apps:
<ul>
    <li>Products</li>
    <li>Accounts</li>
    <li>Cart</li>
    <li>News</li>
    <li>Reviews</li>
    <li>Publishers and developers</li>
</ul>

#### Some of the features:
<ul>
    <li>Purchase of products through Stripe API, using sessions</li>
    <li>Search for products in the database</li>
    <li>Extensive filtering of products by many criteria</li>
    <li>User authorization and registration, including registration and login through GitHub</li>
    <li>News that is added to the database through parsing of news websites</li>
    <li>Display of screenshots, trailers, and all full information on the product page</li>
    <li>Product reviews</li>
    <li>Calculation and display of the average product rating</li>
    <li>Option to add products to favorites or cart and display the number of people who added the product to their favorites</li>
    <li>Discount functionality</li>
    <li>Information about the localization of the product, its system requirements</li>
    And much more!
</ul>

#### Additional
<ul>
    <li>Design</li>
    <li>Layout</li>
</ul>

#### Tools of development
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
    <li>Docker</li>
    <li>Celery</li>
    <li>Redis</li>
    <li>Stripe API</li>
    <li>Django MPTT</li>
    And others...
</ul>

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

#### That's all you need to getting started


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

#### That's all you need to getting started without Docker
