# Primeiros passos e o básico para a introdução em Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)