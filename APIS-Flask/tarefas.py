from flask_restful import Resource, request
import json


tipo_tarefas = ["Testar API", "Desenvolver API", "Desenvolver página WEB", "Subir Git Hub"]


class ListaTipoTarefas(Resource):
    
    def get(self):
        return tipo_tarefas
    
    def post(self):
        dados = json.loads(request.data)
        tipo_tarefas.append(dados)
        return dados
    

class TipoTarefas(Resource):
    
    def get(self, id):
        if id >= len(tipo_tarefas):
            response = {"Status":"Erro", "Mensagem":f"Registro com ID = {id} não existe."}
        else:
            response = tipo_tarefas[id]
        return response
    
    def put(self, id):
        if id >= len(tipo_tarefas):
            response = {"Status":"Erro", "Mensagem":f"Registro com ID = {id} não existe."}
        else:
            dados = json.loads(request.data)
            tipo_tarefas[id] = dados
            response = dados
        return response
    
    def delete(self, id):
        if id >= len(tipo_tarefas):
            response = {"Status":"Erro", "Mensagem":f"Registro com ID = {id} não existe."}
        else:
            tipo_tarefas.pop(id)
            response = {"Status":"Sucesso","Mensagem":"Registro excluído!"}
        return response