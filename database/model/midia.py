from peewee import Model,CharField
from database.database import db

class Perfil (Model):


    tipoMidia = CharField()
    imgMidia = CharField()
    trailerMidia = CharField()
    nomeMidia = CharField()
    anoMidia = CharField()
    tamanhoMidia = CharField()
    classificacaoMidia = CharField()
    descricacaoMidia = CharField()

    class Meta:
        database = db