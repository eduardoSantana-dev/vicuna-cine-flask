from peewee import *
import requests
from database.database import db
import time

# Conectar ao banco de dados MySQL

# Modelo de Filme/Série no banco de dados



class tbmidia(Model):
    titulo = CharField()  # Título do filme ou série
    descricao = TextField()  # Descrição do filme ou série
    genero = CharField()  # Gênero(s) do filme/série
    tipo = CharField()  # 'movie' para filmes, 'tv' para séries
    data_lancamento = DateField()  # Data de lançamento
    faixaEtaria = CharField()  # Faixa etária do filme/série (ex: '18+', 'Livre')
    poster = CharField()  # URL do poster do filme/série
    imgfundo = CharField()  # Nova coluna adicionada
    trailer = CharField()
    tamanho = IntegerField()
   
    id_tmdb = IntegerField(unique=True)  # ID único do filme/série na TMDb

    class Meta:
        database = db  # O banco de dados que estamos usando

# Conectar ao banco de dados
db.connect()
db.create_tables([tbmidia])  # Criar a tabela no banco




def obter_filmes_serie(tipo,page):  # 'movie' para filmes, 'tv' para séries
    api_key = '094bacfd11763f9c0f9b9f27db1557cf'  # Sua chave de API do TMDb
    url = f'https://api.themoviedb.org/3/discover/{tipo}?api_key={api_key}&language=pt-BR&page={page}'
    response = requests.get(url)  # Fazendo a requisição GET
    dados = response.json()  # Convertendo a resposta em JSON
    return dados['results']  # Retorna os resultados da API (lista de filmes ou séries)



def obter_trailer(movie_id,tipo):
   
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=094bacfd11763f9c0f9b9f27db1557cf&language=pt-BR"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Verifica se há vídeos e se o tipo é "Trailer"
        for video in data['results']:
            
                trailer_url = f"https://www.youtube.com/embed/{video['key']}"
                return trailer_url
    return None





def obter_duracao(movie_id,tipo):
    if tipo =="movie":
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=094bacfd11763f9c0f9b9f27db1557cf&language=pt-BR"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Duração do filme em minutos
            duracao = data.get('runtime', None)
            
            return duracao
        
    else:
        url = f"https://api.themoviedb.org/3/tv/{movie_id}?api_key=094bacfd11763f9c0f9b9f27db1557cf&language=pt-BR"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Número de temporadas
            num_temporadas = data.get('number_of_seasons', None)
            
            return num_temporadas
       

def obter_genero(movie_id,tipo):
    if tipo =='movie':
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=094bacfd11763f9c0f9b9f27db1557cf&language=pt-BR"
    else: 
        url = f"https://api.themoviedb.org/3/tv/{movie_id}?api_key=094bacfd11763f9c0f9b9f27db1557cf&language=pt-BR"
    response = requests.get(url)
    if response.status_code == 200:
            data = response.json()
            
            # Duração do filme em minutos
            generos = data.get('genres', None)
            nomes_generos = [genero['name'] for genero in generos]
            return nomes_generos

def salvar_filmes_serie(tipo,page):
    filmes_serie = obter_filmes_serie(tipo,page)  # Obtendo os dados dos filmes ou séries da API

    for item in filmes_serie:
        # Verifica se o filme/série já está no banco
        if not tbmidia.select().where(tbmidia.id_tmdb == item['id']).exists():
            # Coletando os dados relevantes de cada item retornado pela API
            if tipo =='movie':titulo = item['title']
            else :titulo =item['name']
            descricao = item.get('overview', 'Descrição não disponível')
        
            data_lancamento = item.get('release_date', item.get('first_air_date'))
            faixa_etaria = item.get('certification', 'Não disponível')
            poster_url = f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get('poster_path') else None
           
            backdrop_path = item['backdrop_path']
            if backdrop_path:
                backdrop_url = f"https://image.tmdb.org/t/p/original{backdrop_path}"  # URL completa da imagem
            else: backdrop_url = "imgfundonone.png"

            # Inserir o filme/série no banco de dados
            tbmidia.create(
                titulo=titulo,
                descricao=descricao,
                tipo=tipo,
                data_lancamento=data_lancamento,
                poster=poster_url,
                imgfundo=backdrop_url,
                genero=obter_genero(item['id'],tipo),
                trailer = obter_trailer(item['id'],tipo),
                tamanho = obter_duracao(item['id'],tipo),
                id_tmdb=item['id']
            )
# i=111
# tipo  ='movie'
# while i<200:
#     salvar_filmes_serie(tipo,i) 
#     i= i+1
#     time.sleep(0.5)
#     print (i,tipo) 

