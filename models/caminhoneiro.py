from sql_alchemy import banco

class CaminhoneiroModel(banco.Model):
    __tablename__ = 'caminhoneiros'
    
    caminhoneiro_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    idade = banco.Column(banco.String(3))
    sexo = banco.Column(banco.String(10))
    possui_veiculo = banco.Column(banco.String(3))
    tipo_CNH = banco.Column(banco.String(80))
    carregado = banco.Column(banco.String(3))
    tipo_veiculo = banco.Column(banco.String(80))

    def __init__(self, nome, idade, sexo, possui_veiculo, tipo_CNH, carregado, tipo_veiculo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.possui_veiculo = possui_veiculo
        self.tipo_CNH = tipo_CNH
        self.carregado = carregado
        self.tipo_veiculo = tipo_veiculo

    def json(self):
        return {
            'caminhoneiro_id' : self.caminhoneiro_id,
            'nome' : self.nome,
            'idade' : self.idade,
            'sexo' : self.sexo,
            'possui_veiculo' : self.possui_veiculo,
            'tipo_CNH' : self.tipo_CNH,
            'carregado' : self.carregado,
            'tipo_veiculo' : self.tipo_veiculo
        }

    @classmethod
    def find_caminhoneiro(cls, caminhoneiro_id):
        caminhoneiro = cls.query.filter_by(caminhoneiro_id=caminhoneiro_id).first() 
        if caminhoneiro:
            return caminhoneiro
        return None

    def save_caminhoneiro(self):
        banco.session.add(self)
        banco.session.commit()

    def update_caminhoneiro(self, nome, idade, sexo, possui_veiculo, tipo_CNH, carregado, tipo_veiculo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.possui_veiculo = possui_veiculo
        self.tipo_CNH = tipo_CNH
        self.carregado = carregado
        self.tipo_veiculo = tipo_veiculo

    def delete_caminhoneiro(self):
        banco.session.delete(self)
        banco.session.commit()
