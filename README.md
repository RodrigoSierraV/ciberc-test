# ciberc-test

This project was developed with Python 3.7.5 in a Ubuntu 18.04 machine with MySQL 8.

The app is deployed in an AWS EC2 instance, you can go directly to: http://18.231.89.50/upload/

it will receive only ```.xlsb``` files and process the first sheet and the first 3 columns,
which need to have:
  - first column - serial number: with 5 alpha numeric characters
  - second column - quantity: positive integer
  - third column - price: integer or float with two decimal positions

## Local Start

0. Setting MySQL on your machine:
  - ```$ sudo apt-get install libmysqlclient-dev```
  - ```$ sudo mysql -u root -p```
  - ```mysql> create database ciberc;```
  - ```mysql> create user 'django'@'localhost' identified by 'djangodev';```
  - ```mysql> grant usage on *.* to 'django'@'localhost';```
  - ```mysql> grant all privileges on ciberc.* to 'django'@'localhost';```

2. Clone the repo
  ```
  $ git clone https://github.com/RodrigoSierraV/ciberc-test.git
  $ cd ciberc-test/
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv venv
  $ source venv/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

4. Migrate:
  ```
  (venv) $ python manage.py migrate
  ```

5. Run the app:
  ```
  (venv) $ python manage.py runserver
  ```

6. In your browser go to:
  ```
  http://127.0.0.1:8000/upload
  ```
