from flask_restful import Resource, reqparse
from models.rota import RotaModel
from sqlalchemy import func
import sqlite3
import datetime

# filtros de consulta via path
path_params = reqparse.RequestParser()
path_params.add_argument('carregado', type=str)
path_params.add_argument('periodo', type=str)
path_params.add_argument("limit", type=float)
path_params.add_argument("offset", type=float)

class Rotas(Resource):
    def get(self):

        dados = path_params.parse_args()
        
        hoje = datetime.date.today()
        umDia = datetime.timedelta(days=1)
        seteDias = datetime.timedelta(days=7)
        trintaDias = datetime.timedelta(days=30)
        ontem = hoje - umDia
        ultimaSemana = hoje - seteDias
        ultimoMes = hoje - trintaDias
        periodo = ""
        
        if dados['periodo'] == "dia":
            periodo = 'AND data_partida >=' + ontem.strftime('%Y-%m-%d')
        elif dados['periodo'] == "semana":
            periodo =  'AND data_partida >=' +  ultimaSemana.strftime('%Y-%m-%d')
        elif dados['periodo'] == "mes":
            periodo =   'AND data_partida >=' + ultimoMes.strftime('%Y-%m-%d')


        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT count(1) FROM rotas WHERE rotas.carregado="sim"' + periodo)
        total_carregados = list(cursor)[0]
        cursor.close()
        
        if dados['carregado']:
            return { 'Total de caminhões carregados' : total_carregados }
        else:
            return {'Rotas' : [rota.json() for rota in RotaModel.query.order_by(RotaModel.tipo_veiculo).all()]}

class Rota(Resource):
    # a biblioteca reqparce recebe os dados da requisição para gravar na lista
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('caminhoneiro_id')
    argumentos.add_argument('origem')
    argumentos.add_argument('destino')
    argumentos.add_argument('data_partida')
    argumentos.add_argument('carregado')
    argumentos.add_argument('tipo_veiculo')
    
    def get(self, rota_id):
        rota = RotaModel.find_rota(rota_id)
        if rota:
            return rota.json(), 200
        return {'message' : 'Rota não encontrada.'}, 404

    def put(self, rota_id):
        dados = Rota.argumentos.parse_args()
        rota_encontrado = RotaModel.find_rota(rota_id)
        if rota_encontrado:
            rota_encontrado.update_rota(**dados)
            try:
                rota_encontrado.save_rota()
            except:
                return {'message' : 'Erro interno de servidor.'}, 500
            return rota_encontrado.json(), 200
        rota = RotaModel(**dados)
        try:
            rota.save_rota()
        except:
            return {'message' : 'Erro interno de servidor.'}, 500
        return rota.json(), 201

    def delete(self, rota_id):
        rota = RotaModel.find_rota(rota_id)
        if rota:
            try:
                rota.delete_rota()
            except:
                return {'Erro interno de servidor.'}, 500
            return {'message': 'Rota excluida com sucesso!'}, 200
        return {'message' : 'Rota não encontrada.'}, 404

class CadastraRota(Resource):
    def post(self):
        dados = Rota.argumentos.parse_args()
        rota = RotaModel(**dados)
        try:
            rota.save_rota()
        except:
            return {'message' : 'Erro interno de servidor.'}, 500
        return rota.json()
    