from flask_restful import Resource, reqparse
from models.caminhoneiro import CaminhoneiroModel
import sqlite3

# filtros de consulta via path
path_params = reqparse.RequestParser()
path_params.add_argument('carregado', type=str)
path_params.add_argument('possui_veiculo', type=str)
path_params.add_argument("limit", type=float)
path_params.add_argument("offset", type=float)

class Caminhoneiros(Resource):
    def get(self):
        dados = path_params.parse_args()

        if dados['carregado']:
            return {'Caminhoneiros' : [caminhoneiro.json() for caminhoneiro in CaminhoneiroModel.query.filter_by(carregado=dados['carregado']).limit(50).offset(0)]}
        elif dados['possui_veiculo']:
            return {'Caminhoneiros' : [caminhoneiro.json() for caminhoneiro in CaminhoneiroModel.query.filter_by(possui_veiculo=dados['possui_veiculo']).limit(50).offset(0)]}
        else:
            return {'Caminhoneiros' : [caminhoneiro.json() for caminhoneiro in CaminhoneiroModel.query.all()]}

class Caminhoneiro(Resource):
    # a biblioteca reqparce recebe os dados da requisição para gravar na lista
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('idade')
    argumentos.add_argument('sexo')
    argumentos.add_argument('possui_veiculo')
    argumentos.add_argument('tipo_CNH')
    argumentos.add_argument('carregado')
    argumentos.add_argument('tipo_veiculo')
    
    def get(self, caminhoneiro_id):
        caminhoneiro = CaminhoneiroModel.find_caminhoneiro(caminhoneiro_id)
        if caminhoneiro:
            return caminhoneiro.json(), 200
        return {'message' : 'Caminhoneiro não encontrado.'}, 404
    
    def put(self, caminhoneiro_id):
        dados = Caminhoneiro.argumentos.parse_args()
        caminhoneiro_encontrado = CaminhoneiroModel.find_caminhoneiro(caminhoneiro_id)
        if caminhoneiro_encontrado:
            caminhoneiro_encontrado.update_caminhoneiro(**dados)
            try:
                caminhoneiro_encontrado.save_caminhoneiro()
            except:
                return {'message' : 'Erro interno de servidor.'}, 500
            return caminhoneiro_encontrado.json(), 200
        caminhoneiro = CaminhoneiroModel(**dados)
        try:
            caminhoneiro.save_caminhoneiro()
        except:
            return {'message' : 'Erro interno de servidor.'}, 500
        return caminhoneiro.json(), 201

    def delete(self, caminhoneiro_id):
        caminhoneiro = CaminhoneiroModel.find_caminhoneiro(caminhoneiro_id)
        if caminhoneiro:
            try:
                caminhoneiro.delete_caminhoneiro()
            except:
                return {'erro interno de servidor.'}, 500
            return {'message': 'Caminhoneiro excluido com sucesso!'}, 200
        return {'message' : 'Caminhoneiro não encontrado.'}, 404

class CadastraCaminhoneiro(Resource):
    def post(self):
        dados = Caminhoneiro.argumentos.parse_args()
        caminhoneiro = CaminhoneiroModel(**dados)
        try:
            caminhoneiro.save_caminhoneiro()
        except:
            return {'message' : 'Erro interno de servidor.'}, 500
        return caminhoneiro.json()