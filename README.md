# Truckpad
API controle de caminhoes


# Desafio

● Precisamos criar uma api para para cadastrar os motoristas que chegam nesse terminal e saber
mais informações sobre eles. Precisamos saber nome, idade, sexo, se possui veiculo, tipo da CNH,
se está carregado, tipo do veiculo que está dirigindo.
● Precisamos saber a origem e destino de cada caminhoneiro. Será necessário pegar a latitude e
longitude de cada origem e destino.
● Precisamos de um método para consultar todos os motoristas que não tem carga para voltar ao seu
destino de origem.
● Precisamos saber quantos caminhões passam carregados pelo terminal durante o dia, semana e
mês.
● Precisamos saber quantos caminhoneiros tem veiculo próprio.
● Mostrar uma lista de origem e destino agrupado por cada um dos tipos.
● Será necessário atualizar os registros dos caminhoneiros.
● Criar testes unitários para validar o funcionamento dos serviços criados. Utilize o framework de
testes de sua preferência.

# Linguagem + ferramentas
Python 3.7.6, SQLite3

# Rodando a aplicação
No Python 3, para criar um ambiente virtual executamos no terminal (prompt de comando):

python3 -m venv my_venv
Com este comando, um ambiente virtual com o nome my_venv será gerado na forma de uma pasta com a seguinte estrutura:
```
my_venv/
├── bin
│   ├── activate
│   ├── pip
│   ├── python
│   └── ...
│   ...
└── lib
       └── python3.7
           └── site-packages
            └── ...
```
A pasta bin contém o interpretador python, o gerenciador de pacotes pip e outros arquivos usados para interagir com o ambiente virtual, como o activate que serve para ativar o ambiente virtual. Na pasta lib temos o subpasta site-packages na qual são gravados todos pacotes de terceiros que são obtidos pelo gerenciador de pacotes pip. Todos estes arquivos trabalhando em conjunto, garantem o isolamento do ambiente virtual.

### Ativando o ambiente virtual
       
Para usar um ambiente virtual, é necessário ativá-lo usando o script activate conforme já adiantado na seção anterior. Para tal, basta executar:

```
source my_env/bin/activate
```

Após a execução, você notará que o prompt do seu terminal possui agora começa com (my_venv), isto quer dizer que você ativou seu ambiente virtual com sucesso e agora está trabalhando em um ambiente Python isolado daquele que está instalado em seu sistema operacional — e também de outros ambientes virtuais caso existam.


### Testando o ambiente virtual

Finalmente para vermos de fato o funcionamento do ambiente virtual que criamos, vamos instalar um pacote globalmente e testar se o mesmo ficará acessível em nosso ambiente virtual.

Com o ambiente virtual desativado, execute o comando abaixo para instalar o pacote requests — que possui funcionalidades que facilita a manipulação de requisições HTTP, mais informações sobre ele aqui.

```
pip -q install requests
```

Carregando a biblioteca de requerimentos para aplicação:

```
pip install -r requirements.txt 
```
no seu ambiente virtual novo, você conseguirá reinstalar todos pacotes necessários ao seu projeto


Nesta linha de comando, usamos o gerenciador de pacotes do Python chamado pip, você pode encontrar mais informações sobre ele em sua documentação.

Após a instalação, verifique que o pacote requests foi instalado usando o comando para listar os pacotes instalados pelo pip:

```
pip list
```

Agora, ative o ambiente virtual criado anteriormente, fazendo:

```
source my_env/bin/activate
```
Execute novamente o comando do pip para visualizar os pacotes instalados em seu ambiente virtual:

```
pip list
```
Veja que o pacote requests não consta na lista, ou seja, nosso ambiente virtual está isolado do ambiente global do sistema operacional.

# Testes da aplicação

Os testes da API foram feitos via Postman e tanto os testes quanto a documentação podem ser acessados via link abaixo:

https://documenter.getpostman.com/preview/2594455-cef7035b-abe4-409b-ae15-380e7453f5a7?versionTag=latest&apiName=CURRENT&version=latest&top-bar=ffffff&right-sidebar=303030&highlight=ef5b25#intro

