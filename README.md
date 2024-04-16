# dash24-demo


Bootstrap the project

1. Create a virtual environment `python -mvenv venv`
2. Use the virtual environment `source venv/bin/activate`
3. Install all dependencies `pip install -r requirements.txt`
4. Init the database `rm -f db.sqlite ;  sqlite3 db.sqlite < init.sql`

Start the project:

```shell
flask --app service run
```



## Use the API


### List all products

```shell
curl http://127.0.0.1:5000/api/product/list
```

### Add a product

```shell
curl -H "Content-Type: application/json" -X POST --data '{"name": "<product-name>"}' http://localhost:5000/api/product/add
```
