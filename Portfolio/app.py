from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
    nome = "Adson Dias Santos de Jesus"
    descricao = "Desenvolvedor Web Iniciante"
    status = "Melhorando as habilidades cada vez mais"
    curso = "Análise e Desenvolvimento de Sistemas"
    faculdade = "Anhanguera Unopar"
    
    return render_template('portfolio.html', nome=nome, descricao=descricao, status=status, curso=curso, faculdade=faculdade, projects=projects)

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
