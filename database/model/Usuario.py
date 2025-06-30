from peewee import Model,CharField,DateField
from database.database import db

class tbUser (Model):

    nomeUser =CharField()
    emailUser = CharField()
    senhaUser =CharField()
    cpfUser =CharField()
    dataNasc =DateField()
    statusContaUser =CharField()

    class Meta:
        database = db