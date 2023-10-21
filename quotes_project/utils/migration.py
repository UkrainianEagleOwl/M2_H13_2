import os
import django

from pymongo import MongoClient
from pymongo.server_api import ServerApi

os.environ.setdefault("DJANGO_SETTINGS_MODULE","quotes_project.settings")
django.setup()

from quotes.models import Quote,Tag,Author


uri = "mongodb+srv://dmytrofilin:SV3s7TTyNsljL5Zp@ukrainianeagleowl.bvkh16q.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
    
db = client.M2_H08

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author.get('fullname'),
        born_date =  author.get('born_date'),
        born_location = author.get('born_location'),
        description = author.get('description'),
    )
    
quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
    
    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author.get('fullname'))
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)