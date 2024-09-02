from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titulo='Jogos')


@app.route('/crismandos')
def crismandos():
    return render_template('crismandos.html')


@app.route('/chamada')
def chamada():
    return render_template('chamada.html')


if __name__ == ('__main__'):
    app.run(host='0.0.0.0', debug=True)
