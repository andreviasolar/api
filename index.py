from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe os dados enviados para o webhook
    data = request.json
    
    # Faça qualquer processamento necessário com os dados recebidos
    # Neste exemplo, simplesmente devolvemos os dados recebidos
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
