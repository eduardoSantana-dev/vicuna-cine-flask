from flask import Blueprint ,render_template,request,redirect,url_for,session,jsonify
from database.database import db

perfis_route = Blueprint('perfis',__name__)

@perfis_route.route('/perfis')
def perfis():
    if 'id' not in session:
        return redirect (url_for('login.login'))
  
    
    
    try:
        query = db.execute_sql("SELECT idperfil,nomePerfil,imgPerfil FROM tbperfil WHERE idUser = %s",(session['id'],))
        resultado = query.fetchall()
       
        return render_template('perfis.html',perfis=resultado)
    except:
        print("erro")

@perfis_route.route('/acao',methods=["POST"])
def acao():
    nome = request.form.get('nome')
    img = request.form.get('image')
    idperfil = request.form.get('idperfil')
    acao = request.form.get('acao')

    if acao == 'edit':
        edit_perfil(nome,img,idperfil)
    else:
        novo_perfil(nome,img)

    return redirect(url_for('perfis.perfis'))


def novo_perfil(nome,img):
    
  
    try:
        query = db.execute_sql("INSERT INTO tbperfil (idUser, nomePerfil, imgPerfil) VALUES (%s,%s,%s)",(session['id'],nome,img))
       
    except:
        print("erro")

def edit_perfil(nome,img,idperfil):
    
    try:
        query = db.execute_sql("UPDATE tbperfil SET nomePerfil= %s,imgPerfil= %s WHERE idPerfil = %s",(nome,img,idperfil))
        print(nome,img,idperfil)
    except:
        print("erro")


@perfis_route.route('/delete',methods=["POST"])
def delete():
    idperfil = request.form.get('idperfil')
    try:
        query = db.execute_sql("DELETE FROM tbperfil WHERE idperfil = %s",(idperfil,))
        return redirect(url_for('perfis.perfis'))

    except:
        print("erro")



@perfis_route.route('/entrarperfil',methods=["POST"])
def entrar_perfil():
    idPerfil =request.form.get ('idperfil')      
    session['idperfil']= idPerfil
    return redirect (url_for('home.home'))


@perfis_route.route('/adiciolista', methods=["POST"])
def add_lista():
    try:
        data = request.json
        idmidia = data.get('input_data')
        idperfil = session['idperfil']
        
        query = db.execute_sql("INSERT INTO tblista (idPerfil, idMidia) VALUES (%s, %s)", (idperfil, idmidia))
        
        return jsonify({"success": True})
        
    except:
        return jsonify({"success": False, "error": "Descrição do erro"}), 400


@perfis_route.route('/removerlista', methods=["POST"])
def remover_lista():
    try:
        data = request.json
        idmidia = data.get('input_data')
        idperfil = session['idperfil']

        query = db.execute_sql("DELETE FROM tblista WHERE idMidia = %s and idPerfil = %s",(idmidia,idperfil))
        return jsonify({"success": True})

    except:

        return jsonify({"success": False})

@perfis_route.route('/Minha-lista')
def minha_lista():
    if 'id' not in session:
        return redirect (url_for('login.login'))
    elif 'idperfil' not in session :
        return redirect (url_for('perfis.perfis'))
    
    idperfil = session['idperfil']
    try:
        query = """
        SELECT 
            m.*, 
            CASE 
                WHEN l.idmidia IS NOT NULL THEN 'sim'
                ELSE 'nao'
            END AS midia_na_lista,
            CASE 
                WHEN lk.idmidia IS NOT NULL THEN 'sim'
                ELSE 'nao'
            END AS midia_curtida
        FROM tbmidia m
        INNER JOIN tblista l ON m.id = l.idMidia
        LEFT JOIN tblike lk ON m.id = lk.idMidia AND lk.idPerfil = %s
        WHERE l.idPerfil = %s
        """

        params = [idperfil,idperfil] 

        
        query_result = db.execute_sql(query, params)

        resultado = query_result.fetchall()
        
        return render_template('lista.html',midias=resultado)
    except:
        print("erro")
    

@perfis_route.route('/curtir', methods=["POST"])
def curtir():
    data = request.json
    idmidia = data.get('input_data')  # Corrigido para pegar o valor de input_data
    idperfil = session['idperfil']
    
    try:
        query = db.execute_sql("INSERT INTO tblike (idMidia, idPerfil) VALUES (%s, %s)", (idmidia, idperfil))
        # Não é necessário usar 'fetchall' já que a inserção não retorna dados
        return jsonify({"success": True})

    except Exception as e:
        print(f"Erro: {e}")  # Imprime o erro no servidor para depuração
        return jsonify({"success": False})


@perfis_route.route('/descurtir', methods=["POST"])
def descurtir():
    data = request.json
    idmidia = data.get('input_data')
    idperfil = session['idperfil']
    
    try:
        query = db.execute_sql("DELETE FROM tblike WHERE idMidia = %s AND idPerfil = %s", (idmidia, idperfil))
        return jsonify({"success": True})

    except Exception as e:
        print(f"Erro: {e}")  # Imprime o erro no servidor para depuração
        return jsonify({"success": False})
