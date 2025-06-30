from flask import Blueprint ,render_template,request,redirect,url_for,session
from database.database import db

login_route = Blueprint('login',__name__)

@login_route.route ('/')
def login():

    return render_template('login.html')

@login_route.route('/logar',methods=["POST"])
def logar():
    email = request.form.get('email')
    senha = request.form.get('senha')
    try:
        query = db.execute_sql("SELECT idUser FROM tbuser WHERE emailUser = %s and senhaUser = %s and StatusContaUser ='ativo'",(email,senha))
        id = query.fetchone()
        if id:
            session['id']= id
            return redirect(url_for('perfis.perfis'))
        else:
            session.clear
            return render_template('login.html',erro=1)
    except:
        print("erro")
        return render_template('login.html',erro=2)


@login_route.route('/deslogar')
def deslogar():

    session.clear()
    
    return redirect(url_for('home.home'))


