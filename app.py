from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    valor = round(float(request.form.get('valor')),3)
    moeda_origem = request.form.get('moeda_origem')
    moeda_destino = request.form.get('moeda_destino')    
    api_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={apikey}&base_currency={moeda_origem}&currencies={moeda_destino}"
    response = requests.get(api_url)
    data = response.json()
    taxa_cambio = round(data['data'][f'{moeda_destino}'],3)    
    valor_convertido = round(float(valor),3) * round(float(taxa_cambio),3)
    
    return render_template('result.html', valor_convertido=valor_convertido, moeda_destino=moeda_destino, taxa_cambio=taxa_cambio, valor=valor, moeda_origem=moeda_origem)

if __name__ == '__main__':
    app.run(debug=True)
