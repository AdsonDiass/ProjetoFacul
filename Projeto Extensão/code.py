from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Simulação de um banco de dados de usuários
users = {'Adson': {'senha': generate_password_hash('123456')}, 
         'Gustavo': {'senha': generate_password_hash('123456')}}

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user

# Armazenar as tarefas de estudo (simulando um banco de dados)
tarefas = []

# Rota para a tela de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['senha'], password):
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

# Rota para a página inicial (lista de tarefas)
@app.route('/')
@login_required
def index():
    # Cópia da lista de tarefas original
    tarefas_original = list(tarefas)
    
    # Ordenar as tarefas com base no parâmetro 'sort_by' (disciplina, descricao, data)
    sort_by = request.args.get('sort_by')
    if sort_by in ['disciplina', 'descricao', 'data']:
        tarefas_original.sort(key=lambda x: x.get(sort_by))

    # Filtrar as tarefas com base no parâmetro 'filter_by' (disciplina, data)
    filter_by = request.args.get('filter_by')
    filter_value = request.args.get('filter_value')
    if filter_by and filter_value:
        if filter_by == 'disciplina':
            tarefas_original = [tarefa for tarefa in tarefas_original if tarefa['disciplina'] == filter_value]
        elif filter_by == 'data':
            tarefas_original = [tarefa for tarefa in tarefas_original if tarefa['data'] == filter_value]

    return render_template('index.html', tarefas_enum=enumerate(tarefas_original))

# Rota para adicionar uma nova tarefa de estudo
@app.route('/adicionar', methods=['POST'])
@login_required
def adicionar_tarefa():
    disciplina = request.form['disciplina']
    descricao = request.form['descricao']
    data = request.form['data']
    tarefas.append({'disciplina': disciplina, 'descricao': descricao, 'data': data})
    return redirect('/')

# Rota para atualizar uma tarefa de estudo
@app.route('/atualizar/<int:id>', methods=['POST'])
@login_required
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
@login_required
def excluir_tarefa(id):
    del tarefas[id]
    return redirect('/')

# Rota para logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
