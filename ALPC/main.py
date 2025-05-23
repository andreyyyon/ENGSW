from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simulado (em memória)
produtos = [
    {"id": 1, "nome": "Smartphone", "preco": 1500.00, "estoque": 10},
    {"id": 2, "nome": "Notebook", "preco": 3500.00, "estoque": 5},
    {"id": 3, "nome": "Tablet", "preco": 1200.00, "estoque": 8}
]

# Rota GET para listar produtos (com filtros opcionais)
@app.route('/produtos', methods=['GET'])
def get_produtos():
    # Filtros via query parameters (ex: /produtos?nome=Notebook&estoque_minimo=5)
    nome_filtro = request.args.get('nome', type=str)
    estoque_minimo = request.args.get('estoque_minimo', type=int)
    
    resultado = produtos
    
    # Aplicar filtros se existirem
    if nome_filtro:
        resultado = [p for p in resultado if nome_filtro.lower() in p['nome'].lower()]
    if estoque_minimo:
        resultado = [p for p in resultado if p['estoque'] >= estoque_minimo]
    
    return jsonify({"produtos": resultado, "total": len(resultado)}), 200

# Rota GET para buscar um produto específico por ID (ex: /produtos/1)
@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto), 200
    else:
        return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)