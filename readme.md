# A few words about the web application
### Online video game store with Stripe payment system connected, written in Python, Django as backend and CSS, JavaScript as frontend

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
