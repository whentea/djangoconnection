#from django.db import models

# Create your models here.
from mongoengine import *
connect('datakoe', host='localhost')

class StatusModel(EmbeddedDocument):
    status_text = StringField(max_length=200)
    votes = IntField(default=0)

class userModel(Document):
    nama = STringField(max_length=200)
    tgl = DateTimeField(help_text='date published')
    status = ListField(EmbeddedDocumentField(StatusModel))
