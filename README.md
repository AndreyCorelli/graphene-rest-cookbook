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

(Optionally) apply migrations to the database, create superuser and import fixtures:
```shell
./manage.py migrate
./manage.py loaddata ingredients
./manage.py loaddata dishes 
./manage.py createsuperuser
```
The repository already includes SqLite database (file db.sqlite3) with sample data.

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

Paging example. See schema_queries.py, class Query, all_dishes / resolve_all_dishes:
```graphql
query {
  allDishes(skip: 0, first: 1) {
    id
    recipe
    ingredients {
      name
    }
  }
}
```

## 3.2 Create / delete an object
See schema_mutations.py, class CreateDish:
```graphql
mutation {
  createDish(dishData: {
    name: "Fried Chicken"
    recipe: "Fry it"
    complexity: 3
    ingredients: [ 2 ]
  }) {
    	dish { id }
  }
}
```

Deleting an object (see schema_mutations.py, DeleteDish):
```graphql
mutation {
  deleteDish(id: 3) {
    ok
  }
}
```

Modifying an object (see schema_mutations.py, ModifyDish):
```graphql
mutation {
  updateDish(dishData: {
    id: 5
    name: "Fried Chicken"
    ingredients: [ 3 ]
  }) {
    	dish { id }
  }
}
```

## 4 Build and run Docker image
Build image: just run 
```shell
sudo docker build -t graphene-cookbook .
```
command. When the image is built run

```shell
docker run -it -p 8020:8020 \
     -e DJANGO_SUPERUSER_USERNAME=Administrator \
     -e DJANGO_SUPERUSER_PASSWORD=Administrator \
     -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
     graphene-cookbook
```