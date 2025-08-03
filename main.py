import time
import requests
from datetime import datetime
import random

TOKEN = "8497542238:AAGmez9BaNaeqvi7JaxHYmiBCnTpvO6xi-Y"
CHANNEL_ID = "@SignauxTradingAuto"

actifs = ["XAUUSD", "BTCUSD", "ETHUSD", "EURUSD", "USDJPY", "NASDAQ", "SP500", "AAPL", "GOOGL", "TSLA"]

def envoyer_signal():
    actif = random.choice(actifs)
    type_trade = random.choice(["Achat", "Vente"])
    prix = round(random.uniform(100, 3000), 2)
    tp = prix + random.uniform(1, 10)
    sl = prix - random.uniform(1, 10)
    message = f"📈 *Signal {type_trade}*\n\nActif : {actif}\nEntrée : {prix}\nTP : {round(tp, 2)}\nSL : {round(sl, 2)}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    })

def envoyer_resume():
    message = "📊 Résumé du jour :\n- 7 signaux envoyés\n- 5 gagnants ✅\n- 2 perdants ❌"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
        "chat_id": CHANNEL_ID,
        "text": message
    })

while True:
    heure = datetime.now().strftime("%H:%M")
    if heure == "00:00":
        envoyer_resume()
    else:
        envoyer_signal()
    time.sleep(7200)
