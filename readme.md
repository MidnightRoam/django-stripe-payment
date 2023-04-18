# A few words about
### Online video game store with Stripe payment system connected, written in Python, Django as backend and CSS, JavaScript as frontend part
### <a href="http://midnightdeveloper.pythonanywhere.com/">OPEN SITE IN BROWSER</a> (may not be available for a while)
#### Что было реализовано на данный момент:
#### Приложения:
<ul>
    <li>Продукты</li>
    <li>Пользователи</li>
    <li>Корзина</li>
    <li>Новости</li>
    <li>Отзывы</li>
    <li>Издатели и разработчики</li>
</ul>

#### Функционал:
<ul>
    <li>Покупка товаров через Stripe API, используя сессии</li>
    <li>Поиск товаров по базе данных</li>
    <li>Фильтрация по тэгам и платформам активации продукта</li>
    <li>Авторизация и регистрация пользователя, включая регистрацию и вход через GitHub</li>
    <li>Новости, которые добавляются в базу данных через парсинг новостных сайтов</li>
    <li>Вывод скриншотов, трейлеров и всей полной информации на странице товара</li>
    <li>Отзывы об товаре</li>
    <li>Расчет и вывод среднего рейтинга продукта</li>
    <li>Возможность добавления товара в избранное или корзину и вывод количества людей, добавившие товар в избранное</li>
    <li>Скидочный функционал</li>
    <li>Информация об локализации товара, его системные требования</li>
    И многое другое...
</ul>

#### Другое
<ul>
    <li>Дизайн</li>
    <li>Верстка</li>
</ul>

#### Инструменты разработки
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
    И другие...
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
