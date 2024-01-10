from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    users = [
    {
    "id": 110,
    "name": "Leanne Graham jones",
    "last_name" : "graham",
    "username": "Bre'&t",
    "email": "Sincere@april.biz",
    "Date": datetime.now(), 
    "age": "",
    "family_members":  [{'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31}],
    "data_size": 811496,
    "works": [1,2,99,545,11],
    "html": "<b>This</b> is <em>a</em> <button>Button</button>"
    },

    ]
    return render (request,"index.html",{"users": users})
