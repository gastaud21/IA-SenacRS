# Chatbot com Gemini 1.5 Flash

Este projeto implementa um chatbot interativo utilizando o modelo Gemini 1.5 Flash do Google. Este guia passo a passo apresenta como configurar o ambiente, obter a chave de API e rodar o chatbot localmente.

## Passo 1: Configuração do Ambiente

1. **Instale o Python 3.10 ou superior**:

   - Baixe e instale o Python a partir do [site oficial do Python](https://www.python.org/).
   - Código testado com o python 3.10

2. **Crie um ambiente virtual**:

   ```bash
   python -m venv venv
   ```

   - Isso evita que os requisitos deste projeto se misturem com os demais da máquina

3. **Ative o ambiente virtual**:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - Execute o seguinte comando para garantir que o Python que está sendo usado é o do ambiente virtual. Windows: where python ou macOS/Linux: which python
   - O caminho deve apontar para o diretório do ambiente virtual, algo com venv: 'c:\caminho\do\projeto\venv\Scripts\python.exe'

4. **Instale as bibliotecas necessárias**:
   ```bash
   pip install -q -U google-generativeai Flask
   ```

## Passo 2: Obtenção da Chave de API do Gemini

1. **Crie uma conta no Google AI Studio**:

   - Acesse o [Google AI Studio](https://ai.google.dev/).

2. **Obtenha a chave de API**:

   - Siga o guia detalhado disponível neste link: [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br&lang=python).

3. **Configure a chave de API no terminal**:
   - **Windows**:
     ```bash
     set GEMINI_API_KEY=sua_chave_api_aqui
     ```
   - **macOS/Linux**:
     ```bash
     export GEMINI_API_KEY=sua_chave_api_aqui
     ```

## Passo 3: Desenvolvimento do Chatbot

1. **Crie o arquivo `app.py`**:

   - No diretório `src`, crie um arquivo chamado `app.py` com o código fornecido neste repositório. Ou se preferir apenas clone todo projeto para sua máquina com git clone

2. **Execute o servidor Flask**:

   - No terminal, execute o seguinte comando para iniciar o servidor:
     ```bash
     python src/app.py
     ```

3. **Interaja com o chatbot**:
   - Use o comando `curl` para testar o chatbot:
     ```bash
     curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{"message": "Olá, como você está?"}"
     ```
     curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{"message": "Olá, como você está?"}"

# Exemplos de Uso

1. **Personalização para um Domínio (Atendimento ao Cliente)**

- Adicione uma camada de personalização ao prompt para o domínio de atendimento ao cliente. Modifique o endpoint /chat para incluir um "sistema" que guie o modelo.

```bash
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'Mensagem não fornecida'}), 400

    # Prompt personalizado para o domínio de atendimento ao cliente
    prompt = f"""
    Você é um chatbot de atendimento ao cliente para uma loja de eletrônicos.
    Responda as dúvidas dos clientes de forma educada e precisa.
    Pergunta: {user_input}
    """

    # Envio do prompt ao modelo
    response = model.generate_text(prompt)
    return jsonify({'response': response.text})
```

- Como testar: Envie uma requisição com o nome de uma cidade:

```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{"message": "Vocês trabalham com troca de fonte de Computador?"}"
```

2. **Integração com API de Terceiros (Consulta de Clima)**

- Adicione um endpoint adicional para integrar o chatbot com uma API pública, como a [OpenWeatherMap](https://openweathermap.org/) API. Suponha que você já tenha uma chave da API.

```bash
import requests

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'Cidade não fornecida'}), 400

    # Substitua 'sua_chave_api' pela sua chave da OpenWeatherMap
    api_key = "sua_chave_api"
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
```

- Como testar: Envie uma requisição com o nome de uma cidade:

```bash
curl -X POST http://127.0.0.1:5000/weather -H "Content-Type: application/json" -d "{"city": "Porto Alegre"}"
```
