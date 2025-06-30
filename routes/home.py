from flask import Blueprint,render_template,request,redirect,url_for,session
from database.database import db
from routes.midias import carousel
home_route = Blueprint('home',__name__)
@home_route.route('/')
def index():


    return redirect (url_for('home.home'))
@home_route.route('/inicio')
def home(): 
    if 'id' not in session:
        return redirect (url_for('login.login'))
    elif 'idperfil' not in session :
        return redirect (url_for('perfis.perfis'))

    query = db.execute_sql("SELECT m.imgfundo, t.idmidia, COUNT(t.idLista) AS total_likes FROM tblista t INNER JOIN tbmidia m ON t.idmidia = m.id  GROUP BY t.idmidia, m.imgfundo ORDER BY total_likes DESC LIMIT 1;")
    imghome = query.fetchone()
    
    return render_template('index.html',carousel=carousel,pagina='inicio',imagem_url=imghome[0])

@home_route.route('/filmes')
def filmes():
    if 'id' not in session:
        return redirect (url_for('login.login'))
    elif 'idperfil' not in session :
        return redirect (url_for('perfis.perfis'))
    
    query = db.execute_sql("SELECT m.imgfundo, t.idmidia, COUNT(t.idlike) AS total_likes FROM tblike t INNER JOIN tbmidia m ON t.idmidia = m.id WHERE m.tipo = 'movie'  GROUP BY t.idmidia, m.imgfundo ORDER BY total_likes DESC LIMIT 1;")
    imghome = query.fetchone()
    return render_template ('index.html',carousel=carousel,pagina='filmes',imagem_url=imghome[0])

@home_route.route('/series')
def series():
    if 'id' not in session:
        return redirect (url_for('login.login'))
    elif 'idperfil' not in session :
        return redirect (url_for('perfis.perfis'))
    
    query = db.execute_sql("SELECT m.imgfundo, t.idmidia, COUNT(t.idlike) AS total_likes FROM tblike t INNER JOIN tbmidia m ON t.idmidia = m.id WHERE m.tipo = 'tv'  GROUP BY t.idmidia, m.imgfundo ORDER BY total_likes DESC LIMIT 1;")
    imghome = query.fetchone()
    return render_template ('index.html',carousel=carousel,pagina='series',imagem_url=imghome[0])


def perfil_nav():
   query= db.execute_sql("SELECT idPerfil,nomePerfil,imgPerfil FROM tbPerfil WHERE idUser = %s",(session['idperfil'],))
   resultado = query.fetchall()
   print(resultado)
   return resultado