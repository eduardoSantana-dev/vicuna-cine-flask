# from peewee import MySQLDatabase

# # Configuração do banco no Railway
# DB_NAME = "railway"
# DB_USER = "root"
# DB_PASSWORD = "lWcGvxEWhMJcwwldmtYVyItSPPQwvmUq"
# DB_HOST = "viaduct.proxy.rlwy.net"
# DB_PORT = 24334  # Porta do seu banco no Railway

# # Criando a conexão com Peewee
# db = MySQLDatabase(
#     DB_NAME,
#     user=DB_USER,
#     password=DB_PASSWORD,
#     host=DB_HOST,
#     port=DB_PORT
# )
from peewee import MySQLDatabase

db = MySQLDatabase('dbvicunacine', host='localhost', port=3306, user='root', password='')