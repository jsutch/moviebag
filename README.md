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
