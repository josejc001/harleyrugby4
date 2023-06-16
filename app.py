from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Definindo as informações pessoais do chatbot
chatbot_name = "Harley"
chatbot_creator = "José César Mussá"
company_name = "mtevlution"
knowledge_area = "desportos com foco principal Rugby"

# Set up OpenAI API credentials
openai.api_key = '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'

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("tem.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    
    # Define a mensagem personalizada do usuário
    user_message = f"O seu nome é {chatbot_name} criado pela {company_name}, você não tem ligação com o chatgpt nem com OpenAI. Você sabe tudo sobre {knowledge_area}. Seu criador é {chatbot_creator}."
    
    # Enviar a mensagem personalizada para a API do OpenAI e receber a resposta
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você está conversando com um chatbot personalizado."},
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": message}
        ]
    )
    
    if completion.choices[0].message != None:
        return completion.choices[0].message
    else:
        return 'Failed to generate a response!'

if __name__ == '__main__':
    app.run()
