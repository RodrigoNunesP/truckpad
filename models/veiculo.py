from sql_alchemy import banco

class VeiculoModel(banco.Model):
    __tablename__ = 'veiculos'
    codigo = banco.Column(banco.Integer, primary_key=True)
    tipo_veiculo = banco.Column(banco.String(80))
    rotas = banco.relationship('RotaModel')
    
    def __init__(self, codigo, tipo_veiculo):
        self.codigo = codigo
        self.tipo_veiculo = tipo_veiculo

    def json(self):
        return {
            'codigo' : self.codigo,
            'tipo_veiculo' : self.tipo_veiculo,
            'rotas': [rota.json() for rota in self.rotas]
        }

    @classmethod
    def find_veiculo(cls, codigo):
        veiculo = cls.query.filter_by(codigo=codigo).first() 
        if veiculo:
            return veiculo
        return None

    def save_veiculo(self):
        banco.session.add(self)
        banco.session.commit()

    def update_veiculo(self, codigo, tipo_veiculo):
        self.codigo = codigo
        self.tipo_veiculo = tipo_veiculo

    def delete_veiculo(self):
        banco.session.delete(self)
        banco.session.commit()
