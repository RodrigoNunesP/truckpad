from flask_restful import Resource, reqparse
from models.veiculo import VeiculoModel

class Veiculos(Resource):
    def get(self):
        return {'Veiculos' : [veiculo.json() for veiculo in VeiculoModel.query.all()]}

class Veiculo(Resource):
    # a biblioteca reqparce recebe os dados da requisição para gravar na lista
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('codigo')
    argumentos.add_argument('tipo_veiculo')
    
    def get(self, codigo):
        veiculo = VeiculoModel.find_veiculo(codigo)
        if veiculo:
            return veiculo.json(), 200
        return {'message' : 'veiculo não encontrado.'}, 404
    
    def post(self, codigo):
        if VeiculoModel.find_veiculo(codigo):
            return {'message' : 'Codigo de veiculo "{}" já existe.' . format(codigo)}, 400

        dados = Veiculo.argumentos.parse_args()
        veiculo = VeiculoModel(**dados)
        try:
            veiculo.save_veiculo()
        except:
            return {'message' : 'Erro interno de servidor.'}, 500
        return veiculo.json()

    def put(self, codigo):
        dados = Veiculo.argumentos.parse_args()
        veiculo_encontrado = VeiculoModel.find_veiculo(codigo)
        if veiculo_encontrado:
            veiculo_encontrado.update_veiculo(**dados)
            try:
                veiculo_encontrado.save_veiculo()
            except:
                return {'message' : 'Erro interno de servidor.'}, 500
            return veiculo_encontrado.json(), 200
        veiculo = VeiculoModel(**dados)
        try:
            veiculo.save_veiculo()
        except:
            return {'message' : 'Erro interno de servidor.'}, 500
        return veiculo.json(), 201

    def delete(self, codigo):
        veiculo = VeiculoModel.find_veiculo(codigo)
        if veiculo:
            try:
                veiculo.delete_veiculo()
            except:
                return {'erro interno de servidor.'}, 500
            return {'message': 'veiculo excluido com sucesso!'}, 200
        return {'message' : 'veiculo não encontrado.'}, 404
