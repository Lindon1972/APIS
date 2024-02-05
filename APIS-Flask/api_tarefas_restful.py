from flask import Flask, request
from flask_restful import Api, Resource
import json
from tarefas import TipoTarefas, ListaTipoTarefas


app = Flask(__name__)
api = Api(app)

tarefas = [
    {'id':0, 'responsável':'Antonio', 'tarefa':'Desenvolver API', 'status':'pendente'},
    {'id':1, 'responsável':'Maria', 'tarefa':'Testar API', 'status':'pendente'},
    {'id':2, 'responsável':'Fernando', 'tarefa':'Desenvolver página WEB', 'status':'pendente'}
]


class Tarefa(Resource):
    
    def get(self, id):
        if id >= len(tarefas):
            response = {"Status":"Erro", "Mensagem":f"Registro com o ID = {id} não existe."}
        else:
            response = tarefas[id]
        return response
    
    def put(self, id):
        if id >= len(tarefas):
            response = {"Status":"Erro", "Mensagem":f"Registro com o ID = {id} não existe."}
        else:
            dados = json.loads(request.data)
            tarefas[id] = dados
            response = dados
        return response

    def delete(self, id):
        if id >= len(tarefas):
            response = {"Status":"Erro", "Mensagem":f"Registro com o ID = {id} não existe."}
        else:
            tarefas.pop(id)
            response = {"Status:":"Sucesso", "Mensagem":"Registro excluído!"}
        return response
    

class ListaTarefas(Resource):
    
    def get(self):
        return tarefas
    
    def post(self):
        posicao = len(tarefas)
        dados = json.loads(request.data)
        dados['id'] = posicao
        tarefas.append(dados)
        return tarefas[posicao]


api.add_resource(Tarefa, '/tarefas/<int:id>/')
api.add_resource(ListaTarefas, '/tarefas/lista/')
api.add_resource(ListaTipoTarefas, '/tarefas/tipo/')
api.add_resource(TipoTarefas, '/tarefas/tipo/<int:id>')
    

if __name__ == '__main__':
    app.run(debug=True)