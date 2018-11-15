#from django.db import models

# Create your models here.
from mongoengine import *
connect('datakoe', host='localhost')

class StatusModel(EmbeddedDocument):
    mk = StringField(max_length=200)
    votes = IntField(default=0)

class UserModel(Document):
    nama = StringField(max_length=200)
nilais = ListField(EmbeddedDocumentField(StatusModel))
