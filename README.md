# REST_API_flask
This is Alibi Zhenis's personal REST API project. Tech stack: Flask, Marshmallow, SQLAlchemy, SQLite.

# Setup
```
#Installing dependencies
$ pip install requirements.txt

# Launch
python3 main.py
```

# Description
Database stores only one object - product:
```
{
  id: int,
  name: string,
  description: string,
  price: int,
  qty: int
}
```
Client can create, update, query(all or by id), and delete any instance of an object.

# Endpoints
```
GET /product
GET /product/:id
POST /product
PUT /product/:id
DELETE /product/:id
```
