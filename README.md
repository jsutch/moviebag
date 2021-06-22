# demo of flask RESTful api 

### signup:

POST  
/api/auth/signup  
```
{
    "email":"aaa@test.com",
    "password":"mypassword"
}
```

### login
POST  
/api/auth/login  
```
{
    "email":"aaa@test.com",
    "password":"mypassword"
}
```

### get all movies
GET  
/api/movies   

### add a movie

POST  
/api/movies  
```
{
    "name": "Shawshank Redemption",
    "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    "genres": ["Drama"]
}
```

### update a movie

PUT  
/api/movies/<id>  
```
{
    "name": "Shawshank Redemption On Mars Part 2",
    "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    "genres": ["Drama"]
}
```

### delete a movie

DELETE  
/api/movies/<id>  


### 


# Setup

Needs a "creds.py" file at root in the following format.

````
mongouser = 'myUsername'
mongopassword = 'myPassword'
JWT_SECRET_KEY = "JWTSecretKeyString"
MAIL_SERVER = "myMailServerAddress"
MAIL_PORT = "25"
MAIL_PORT_TEST = "1025"
MAIL_USERNAME = "support@mydomain.com"
MAIL_PASSWORD = ""
```

then

```
python3 run.py
```
