from flask import Blueprint,render_template,request,redirect,url_for,session,jsonify
from database.database import db

midias_route = Blueprint('midia',__name__)

@midias_route.route('/')
def midiaCarousel(tipo, genero):
    base_query = """
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
        LEFT JOIN tblista l ON m.id = l.idmidia AND l.idperfil = %s
        LEFT JOIN tblike lk ON m.id = lk.idmidia AND lk.idperfil = %s
    """
    idperfil = session['idperfil']
    params = [idperfil,idperfil] 

  
    if tipo == "0" and genero == "0":
        query = base_query + " LIMIT 40"
    elif tipo == "0":
        query = base_query + " WHERE m.genero LIKE %s LIMIT 40"
        params.append('%' + genero + '%')
    elif genero == "0":
        query = base_query + " WHERE m.tipo = %s LIMIT 40"
        params.append(tipo)
    else:
        query = base_query + " WHERE m.tipo = %s AND m.genero LIKE %s LIMIT 40"
        params.extend([tipo, '%' + genero + '%'])

    # Executa a query
    query_result = db.execute_sql(query, params)

    resultado = query_result.fetchall()
    print(resultado)
    return resultado

@midias_route.route('/')
def carousel(nome,tipo,genero):
    midias =midiaCarousel(tipo,genero)

    return render_template('carousel.html',midias=midias,nome=nome)


@midias_route.route('/processar', methods=['POST'])
def processar():
    data = request.json
    texto = data.get('texto', '')

    # Prevenir erro ao pesquisar string vazia
    if not texto.strip():
        return jsonify({"resposta": []})  
    idperfil = session['idperfil']
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
        LEFT JOIN tblista l ON m.id = l.idmidia AND l.idperfil = %s
        LEFT JOIN tblike lk ON m.id = lk.idmidia AND lk.idperfil = %s
        WHERE m.titulo LIKE %s
        
    """

    params = [idperfil, idperfil, '%' + texto + '%']

    query_result = db.execute_sql(query, params)
    resultado = query_result.fetchall()

    resposta = []
    
    for row in resultado:
       
        resposta.append({
            
            "id": row[0],
            "nome": row[1],
            "descricao": row[2],
            "genero": row[3].strip("[]").replace("'", "").split(", "),  # Transformar string em lista
            "tipo": row[4],
            "lancamento": row[5],
            "poster": row[6],
            "imgfundo": row[7],
            "trailer": row[8],
            "tamanho": row[9],
            "naLista": row[11],  
            "curtido": row[12]   
        })
   
    return jsonify({"resposta": resposta})
