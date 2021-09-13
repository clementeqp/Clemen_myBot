from telegram.ext import Updater, CommandHandler, ConversationHandler

import os
from dotenv import load_dotenv



load_dotenv()

INPUT_TEXT = 0

def start(update, context):
    update.message.reply_text('Hola, bienvenido.\nQue deseas hacer?\nUsa /qr para generar un codigo qr')
    
def qr_command_handler(update, context):
    
    update.message.reply_text('Enviame un texto para generarte un codigo qr')
    
    return INPUT_TEXT



if __name__ == '__main__':
    updater = Updater(token=os.getenv('token'), use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler)
        ],
        
        states={},
        
        fallbacks=[]
    ))
    
    
    # add handler
    updater.start_polling()
    updater.idle()
    