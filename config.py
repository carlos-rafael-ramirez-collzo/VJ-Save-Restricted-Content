import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29860993"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b0e23e8daeac124e838dcb6f07eb4a2b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://braintimestudios:AMfboVS2c0viqspL@cluster0.ukz2v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
