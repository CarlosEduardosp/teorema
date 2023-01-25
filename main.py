from flask import Flask, render_template, url_for, make_response, request, redirect
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    #coletando os dados do formulario html
    if request.method == 'POST':
        valorx = request.form.get('valorx')
        valory = request.form.get('valory')

        #convertendo os textos em float.
        valorx = float(valorx)
        valory = float(valory)

        #valor da hipotenusa ao quadrado
        hipotenusa = (valorx * valorx) + (valory * valory)

        #achando a raiz quadrada da hipotenusa.
        hipotenusa = math.pow(hipotenusa, 1/2)

        #chamando o index.html, e passando o valor por parâmetro.
        return render_template('index.html', hipotenusa=hipotenusa)

if __name__ == '__main__':
    app.run(debug=True)

