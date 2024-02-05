from flask import Flask, jsonify
from bayeta import frotar
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>!Hola mundo!</p>"

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def frases(n_frases):
    frases_generadas = frotar(n_frases)
    return jsonify({"frases": frases_generadas})

app.run(host="0.0.0.0")