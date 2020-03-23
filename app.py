from flask import Flask
from flask_restful import Api
from resourses.caminhoneiro import Caminhoneiros, Caminhoneiro, CadastraCaminhoneiro
from resourses.rota import Rotas, Rota, CadastraRota
from resourses.veiculo import Veiculos, Veiculo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

# endpoint para Caminhoneiros
api.add_resource(Caminhoneiros, '/caminhoneiros')
api.add_resource(Caminhoneiro, '/caminhoneiro/<int:caminhoneiro_id>')
api.add_resource(CadastraCaminhoneiro, '/caminhoneiro/cadastra')

# endpoint para Rotas 
api.add_resource(Rotas, '/rotas')
api.add_resource(Rota, '/rota/<int:rota_id>')
api.add_resource(CadastraRota, '/rota/cadastra')

# endpoint para Veiculos
api.add_resource(Veiculos, '/veiculos')
api.add_resource(Veiculo, '/veiculo/<int:codigo>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)

