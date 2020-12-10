# urmart-test
Urmart-test is for developers testing the orderplatform. 

## Technologies
Project is created with:
* Python 3.8.6
* Django 3.1.4
* Django-environ 0.4.5
* Docker 19.03.13

## Setup
To run this project, install it locally using `git clone`

### Build the project in local, please follow the steps:
#### After cloning this project on 
#### Please add an .env file fist and specify the following
* SECRET_KEY: check setting.py 
* EMAIL_HOST: for the sending information purpose, please set a email host, ex:'smtp.gmail.com'
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD
For example:
```
ENV=dev
SECRET_KEY ='YOUR_SECRET_KEY'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,urmart-test.tw
EMAIL_HOST='YOUR_EMAIL_HOST'
EMAIL_HOST_USER='YOUR_EMAIL'
EMAIL_HOST_PASSWORD='YOUR_EMAIL_PASSWORD'
```
#### AND RUN ```docker-compose -f docker-compose-off.yml build```

#### THEN RUN ```docker-compose -f docker-compose-off.yml up```
