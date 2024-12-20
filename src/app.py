import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configuração da chave de API
genai.configure(api_key=os.getenv("AIzaSyA6vSd2sKB7zoxZfKJ4NgvZ_W5ToFh0MA0"))

# Inicialização do modelo Gemini 1.5 Flash
model = genai.GenerativeModel('gemini-1.5-flash')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     if not user_input:
#         return jsonify({'error': 'Mensagem não fornecida'}), 400

#     # Envio da mensagem ao modelo
#     response = model.generate_content(user_input)
#     return jsonify({'response': response.text})



# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get('message')
#     if not user_input:
#         return jsonify({'error': 'Mensagem não fornecida'}), 400

#     # Prompt personalizado para o domínio de atendimento ao cliente
#     prompt = f"""
#     Você é um chatbot de atendimento aos pessoas .
#     Responda as dúvidas dos clientes de forma educada e precisa.
#     Pergunta: {user_input}
#     """

#     # Envio do prompt ao modelo
#     response = model.generate_content(prompt)
#     return jsonify({'response': response.text})

import requests

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'Cidade não fornecida'}), 400

    # Substitua 'sua_chave_api' pela sua chave da OpenWeatherMap
    api_key = "1be274b1d645468666c15db062fe833d"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br"

    # Realizar a requisição para a API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return jsonify({
            'city': city,
            'weather': weather,
            'temperature': f"{temp} °C"
        })
    else:
        return jsonify({'error': 'Não foi possível obter o clima'}), 400

if __name__ == '__main__':
    app.run(debug=True)