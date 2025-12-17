#Chat com Telegram Bot API
import os
from langchain_groq import ChatGroq
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"
TELEGRAM_BOT_TOKEN = "TELEGRAM_BOT_TOKEN"

#CRIAR O MODELO DE IA Llama 3
chat = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    ) 

#FUNCAO PARA INTERAGIR COM O CHATBOT
def conversar_com_chatbot(pergunta:str)-> str:
    resposta = chat.invoke([
        {"role": "user", "content": pergunta}]) #usa o metodo predict_messages para obter a resposta do chatbot
    return resposta.content #retorna o conteudo da resposta

#Função para lidar com mensagens recebidas
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Olá! Eu sou um chatbot. Estou processando sua mensagem...")

async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pergunta = update.message.text
    resposta = conversar_com_chatbot(pergunta)
    await update.message.reply_text(resposta)

def main() -> None: 
    # Criar a aplicação do bot
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Adicionar handlers para comandos e mensagens
    app.add_handler(CommandHandler("start", handle_message))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    app.run_polling()

    # Iniciar o bot
    app.run_polling()
    
if __name__ == "__main__":
    main()