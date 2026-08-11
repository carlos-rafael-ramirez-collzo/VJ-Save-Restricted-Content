# netlify/functions/bot.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa tu bot desde el archivo principal
from app import app  # Asumiendo que tu bot se llama 'app'

def handler(event, context):
    # Si usas webhook, este es el punto de entrada
    return app(event, context)
