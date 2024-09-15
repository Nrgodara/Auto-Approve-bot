from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25318919"))
    API_HASH = getenv("API_HASH", "c1be7e25b00d9431c8575ef5d8058bcb")
    BOT_TOKEN = getenv("BOT_TOKEN", "7390995239:AAETy6yB2uorMTCT9Zw1RnQfhWpXOJCGQRw")
    FSUB = getenv("FSUB", "Aditya_ranjan_MathsComplete")
    CHID = int(getenv("CHID", "-1001945845419"))
    SUDO = list(map(int, getenv("SUDO", "1280494242").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sumansamtiya83:Suman321@cluster0.p7l7y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    SESSION = getenv("SESSION", "")
cfg = Config()
