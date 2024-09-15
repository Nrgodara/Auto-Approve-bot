from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25318919"))
    API_HASH = getenv("API_HASH", "c1be7e25b00d9431c8575ef5d8058bcb")
    BOT_TOKEN = getenv("BOT_TOKEN", "7390995239:AAETy6yB2uorMTCT9Zw1RnQfhWpXOJCGQRw")
    FSUB = getenv("FSUB", "Aditya_ranjan_MathsComplete")
    CHID = int(getenv("CHID", "-1001945845419"))
    SUDO = list(map(int, getenv("SUDO", "1280494242").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sumansamtiya83:Suman321@cluster0.p7l7y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    SESSION = getenv("SESSION", "1BVtsOIwBu2X7acNGcO6QY9jeoTCIhU4LLgmLcLx2uXWXltiem0eOE8o1lhAJJ-Sk2Eh_zt76IPIGb7vIaSR2AoE7lapXOmOtN67Izka_WDqsKbcMXrkQIa0bUBI5C_fjHC1CI7RCGCHjH0wkjCl8MG4hycDtb-ZUQmeY39laZWp_I7XE2Sfuta3hG7DshLEQ5DwF9JNsU5oS6swNOioPBm-dtcJqQhse5m7JknapdsBKgUq-cNYIEN71xJOmY1gtENI3umEtwd7bOnWbpfmrExdQ_GtTKmBd76kAR3roYIY36r5Qkz3oF0OvfuJDX1oEpOvxub9oQ5wmA71ZeyOOpKgd2-vJ1w8=")
    SESSION_USERNAME = getenv("SESSION_USERNAME", "Mr_Mahiji")
 
cfg = Config()
