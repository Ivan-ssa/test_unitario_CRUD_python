from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para armazenar reservas
reservas = []

# Rota para criar reserva
@app.route('/reservas', methods=['POST'])
def criar_reserva():
    dados = request.get_json()
    reserva = {
        'id': len(reservas) + 1,
        'nome': dados.get('nome'),
        'data': dados.get('data')
    }
    reservas.append(reserva)
    return jsonify(reserva), 201

# Rota para listar reservas
@app.route('/reservas', methods=['GET'])
def listar_reservas():
    return jsonify(reservas)

# Rota para atualizar reserva
@app.route('/reservas/<int:id>', methods=['PUT'])
def atualizar_reserva(id):
    dados = request.get_json()
    reserva = next((r for r in reservas if r['id'] == id), None)
    if reserva is not None:
        reserva['nome'] = dados.get('nome', reserva['nome'])
        reserva['data'] = dados.get('data', reserva['data'])
        return jsonify(reserva)
    return jsonify({'message': 'Reserva não encontrada'}), 404

# Rota para cancelar reserva
@app.route('/reservas/<int:id>', methods=['DELETE'])
def cancelar_reserva(id):
    global reservas
    reservas = [r for r in reservas if r['id'] != id]
    return jsonify({'message': 'Reserva cancelada'}), 204

if __name__ == '__main__':
    app.run(debug=True)
