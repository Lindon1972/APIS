from flask import Flask, jsonify, request
import json


app = Flask(__name__)

tarefas = [
    {'id':1, 'responsável':'Antonio', 'tarefa':'Desenvolver uma api', 'status':'pendente'},
    {'id':2, 'responsável':'Maria', 'tarefa':'Testar uma api', 'status':'pendente'},
    {'id':3, 'responsável':'Fernando', 'tarefa':'Desenvolver uma página web', 'status':'pendente'}
]


@app.route('/tarefas/', methods=['GET','POST'])
def lista_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        tarefas.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido!'})


@app.route('/tarefas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    
    mensagem = f'Registro com ID={id} não existe!'
    response = {'status':'erro', 'mensagem':mensagem}
    
    i = 0
    ind = -1

    for tarefa in tarefas:

        if tarefa['id'] == id:
            response = tarefa
            ind = i
            break
        i += 1
    
    
    if ind < 0:
        return response
    
    if request.method == 'GET':
        return jsonify(response)
    elif request.method == 'PUT':
        response['status'] = 'resolvido'
        return jsonify({'status':'sucesso', 'Mensagem:':'Status alterado!'})
    elif request.method == 'DELETE':
        tarefas.pop(ind)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído!'})        


""" if __name__ == '__main__':
    app.run(debug=True) """