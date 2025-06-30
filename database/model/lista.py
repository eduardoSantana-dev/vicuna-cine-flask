from peewee import Model,IntegerField
from database.database import db

class Perfil (Model):


    
    idPefil =IntegerField()
    idMidia =IntegerField()
    

    class Meta:
        database = db