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