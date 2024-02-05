from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rd
from pandas_ods_reader import read_ods


app = Flask(__name__)

#run_with_ngrok(app)

arquivo = read_ods("arquivos/Cadastro.ods")

cadastro = {}
lista = {}

i = 0

while i < 5:

    for linha in arquivo.items():
        cadastro[linha[0]] = linha[1][i]
    
    lista[cadastro['id']] = {'nome': cadastro['nome'], 'idade': cadastro['idade'], 
                         'cidade': cadastro['cidade'], 'país': cadastro['país']}
    i += 1


@app.route("/")
def home():
    return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL. <h3><marquee>"


@app.route("/input")
def input():
    return jsonify(lista)


@app.route("/output", methods=['GET','POST'])
def predJson():
    pred = rd.choice(['positive', 'negative'])
    nd = lista.get(1)
    nd['prediction'] = pred
    return jsonify(nd)


#run_with_ngrok(app)
app.run()

