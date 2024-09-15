from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25318919"))
    API_HASH = getenv("API_HASH", "c1be7e25b00d9431c8575ef5d8058bcb")
    BOT_TOKEN = getenv("BOT_TOKEN", "7390995239:AAETy6yB2uorMTCT9Zw1RnQfhWpXOJCGQRw")
    FSUB = getenv("FSUB", "Aditya_ranjan_MathsComplete")
    CHID = int(getenv("CHID", "-1001945845419"))
    SUDO = list(map(int, getenv("SUDO", "1280494242").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sumansamtiya83:Suman321@cluster0.p7l7y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    SESSION = getenv("SESSION", "BQGCVgcAxAviJQXUqk92KZvVjWyTvA5hU_2cAmL3azzmwR3Eu0bo4EFpka9XJojAxoTSZUV8b-Dmi4tt72EL280g1r3YUdwYitJI0cPc05CZvuXQdwhXG0N8zZEyKKtZUqc2Ci_LYx01vfqVpEKh4rp8CotbYaUF64hf5g4fIx-PLmNlB50cknJUi2ZRr7r6hVev8LVJfAZx99-83B4x44M1bIELhaxz0Q-V-bJi5yVmSQqMBe95bs3w-m95qISimMyckNpxnrMnN4yo8gj6wILrBTC3LWiHh0bNCFKUsSLvKPN1iyiPJfUUCOklDyUQpO5prvS8pJJmvmILlmj9HXuXHfiQOgAAAABMUsqiAA")
    SESSION_USERNAME = getenv("SESSION_USERNAME, "Mr_Mahiji")
 
cfg = Config()
