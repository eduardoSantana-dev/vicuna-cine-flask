from flask import Flask,session,redirect,url_for
from routes.home import home_route
from routes.login import login_route
from routes.perfis import perfis_route
from routes.cadastro import cadastro_route
from database.database import db
from database.model.Usuario import tbUser
from routes.midias import midias_route
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # Corrige CORS

@app.context_processor
def perfil_nav():
    if 'idperfil' in session:
        # Executa a consulta no banco de dados
        query = db.execute_sql("SELECT idPerfil, nomePerfil, imgPerfil FROM tbperfil WHERE idPerfil = %s", (session['idperfil'],))
        resultado = query.fetchall()
        
        # Converte os resultados para uma estrutura de dicionário legível
        perfis = [{"idPerfil": row[0], "nomePerfil": row[1], "imgPerfil": row[2]} for row in resultado]
        
        # Retorna os perfis como parte do contexto
        return {"perfis_nav": perfis}
    else:
        # Retorna um valor vazio se não houver 'idperfil' na sessão
        return {"perfis_nav": []}


app.secret_key = '12346'
app.register_blueprint(home_route)
app.register_blueprint(login_route,url_prefix='/login')
app.register_blueprint(cadastro_route)
app.register_blueprint(perfis_route)
app.register_blueprint(midias_route)


db.connect()
db.create_tables([tbUser])

app.run(debug=True)

# caso queira rodar direto em seu ip
# app.run(host='0.0.0.0', port=8000, debug=True)
