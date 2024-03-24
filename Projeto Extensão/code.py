from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Armazenar as tarefas de estudo (simulando um banco de dados)
tarefas = []

# Rota para a página inicial (lista de tarefas)
@app.route('/')
def index():
    return render_template('index.html', tarefas_enum=enumerate(tarefas))

# Rota para adicionar uma nova tarefa de estudo
@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    disciplina = request.form['disciplina']
    descricao = request.form['descricao']
    data = request.form['data']
    tarefas.append({'disciplina': disciplina, 'descricao': descricao, 'data': data})
    return redirect('/')

# Rota para atualizar uma tarefa de estudo
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar_tarefa(id):
    nova_disciplina = request.form['nova_disciplina']
    nova_descricao = request.form['nova_descricao']
    nova_data = request.form['nova_data']
    tarefas[id]['disciplina'] = nova_disciplina
    tarefas[id]['descricao'] = nova_descricao
    tarefas[id]['data'] = nova_data
    return redirect('/')

# Rota para excluir uma tarefa de estudo
@app.route('/excluir/<int:id>')
def excluir_tarefa(id):
    del tarefas[id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
