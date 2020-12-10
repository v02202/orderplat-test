# urmart-test

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
