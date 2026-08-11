import sys
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Aquí va la lógica de tu bot
    return "OK", 200

# Este es el punto de entrada para el handler
if __name__ == "__main__":
    app.run()
