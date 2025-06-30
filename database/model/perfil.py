from peewee import Model,CharField,IntegerField
from database.database import db

class Perfil (Model):


    
    idUser =IntegerField()
    nomePefil =CharField()

    class Meta:
        database = db