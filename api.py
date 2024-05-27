from flask import Flask, jsonify

app = Flask(__name__)

# Rota para raiz da API
@app.route('/')
def index():
    return 'Bem-vindo à API!'

# Rota para retornar dados
@app.route('/dados')
def get_data():
    dados = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
