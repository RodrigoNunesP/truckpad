from sql_alchemy import banco
from datetime import datetime

class RotaModel(banco.Model):
    __tablename__ = 'rotas'
    
    rota_id = banco.Column(banco.Integer, primary_key=True)
    caminhoneiro_id = banco.Column(banco.Integer)
    origem = banco.Column(banco.String(80))
    destino = banco.Column(banco.String(80))
    data_partida = banco.Column(banco.String(80))
    tipo_veiculo = banco.Column(banco.Integer, banco.ForeignKey('veiculos.codigo'))
    carregado = banco.Column(banco.String(3))
    
    def __init__(self, caminhoneiro_id, origem, destino, data_partida, tipo_veiculo, carregado):
        self.caminhoneiro_id = caminhoneiro_id
        self.origem = origem
        self.destino = destino
        self.data_partida = data_partida
        self.tipo_veiculo = tipo_veiculo
        self.carregado = carregado
        
    def json(self):
        return {
            'rota_id' : self.rota_id,
            'caminhoneiro_id' : self.caminhoneiro_id,
            'origem' : self.origem,
            'destino' : self.destino,
            'data_partida' : self.data_partida,
            'tipo_veiculo' : self.tipo_veiculo,
            'carregado' : self.carregado
        }

    @classmethod
    def find_rota(cls, rota_id):
        rota = cls.query.filter_by(rota_id=rota_id).first() 
        if rota:
            return rota
        return None

    def save_rota(self):
        banco.session.add(self)
        banco.session.commit()

    def update_rota(self, caminhoneiro_id, origem, destino, data_partida, tipo_veiculo, carregado):
        self.caminhoneiro_id = caminhoneiro_id
        self.origem = origem
        self.destino = destino
        self.data_partida = datetime.strptime(data_partida, '%Y-%m-%d %H:%M')
        self.tipo_veiculo = tipo_veiculo
        self.carregado = carregado

    def delete_rota(self):
        banco.session.delete(self)
        banco.session.commit()
