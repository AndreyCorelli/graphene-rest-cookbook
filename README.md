# 1 How to run the project from command line
Create a virtual environment:
```shell
python3 -m venv venv
source venv/bin/activate
```
Install packages:
```shell
pip install -r requirements.txt
```

Apply migrations to the database, create superuser and import fixtures:
```shell
./manage.py migrate
./manage.py loaddata ingredients
./manage.py loaddata dishes 
./manage.py createsuperuser
```

Run
```shell
./manage.py runserver
```

# 2 How to test the project

Check the API in the command line ...
```shell
curl -H 'Accept: application/json; indent=4' -u Administrator:Administrator http://127.0.0.1:8000/categories/
```
... or navigate to the Django administrator website:
http://localhost:8000/admin/

... or navigate to the GraphQL debug webpage:
http://localhost:8000/graphql/

# 3 Example queries
## 3.1 Read operations
Read all dishes w/o filtering, include id, recipe and ingredients fields.
Select name of each of the ingredients.
```graphql
query {
  allDishes {
    id
    recipe
    ingredients {
      name
    }
  }
}
```