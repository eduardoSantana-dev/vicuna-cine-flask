from flask import Blueprint ,render_template,request,redirect,url_for,session
from database.model.Usuario import tbUser
from database.database import db
cadastro_route = Blueprint('cadastro',__name__)

@cadastro_route.route ('/cadastro')
def cadastro():

    return render_template('cadastro.html')


@cadastro_route.route ('/cadastrar',methods=['POST'])
def cadastrar():
    email = request.form.get('email')
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    data = request.form.get('data')
    senha = request.form.get('senha')
    try:
        query =db.execute_sql ("SELECT iduser FROM tbuser WHERE emailUser = %s",(email,))
        resultado = query.fetchone()
        if resultado == None:
                cadastro = tbUser.create(
                nomeUser = nome,
                emailUser = email,
                senhaUser = senha,
                cpfUser = cpf,
                dataNasc =data,
                statusContaUser = "ativo"
                )
                return redirect(url_for('login.login'))
        else:
            return render_template('cadastro.html',erro=1)

    except:
         return render_template('cadastro.html',erro=2)
        




        
@cadastro_route.route('/atualizar-conta')
def atualizar():
    query = db.execute_sql("SELECT * FROM tbUser WHERE idUser =%s",(session['id']))
    resultado = query.fetchall()
    return  render_template('atualizarconta.html',conta=resultado)
@cadastro_route.route('/updateuser',methods=['POST'])
def atualizarconta():
    email = request.form.get('email')
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    data = request.form.get('data')
    oldsenha = request.form.get('oldsenha')
    newsenha = request.form.get('newsenha')
    iduser = request.form.get('iduser')
    try:
        query = db.execute_sql ("SELECT idUser FROM tbuser WHERE senhaUser = %s and idUser = %s",(oldsenha,iduser))
        resultado = query.fetchone()
        if resultado == None:
            print(resultado)
            return redirect ('/atualizar-conta')
        else:
            update = db.execute_sql("UPDATE tbuser SET nomeUser= %s ,emailUser= %s ,senhaUser= %s ,cpfUser= %s ,DataNasc= %s WHERE iduser = %s",(nome,email,newsenha,cpf,data,iduser))
            return redirect(url_for('home.home'))


    except:
        return "<h1>viado</h1>"