from flask import Flask, request
import requests
import os  # needed for Render port binding

app = Flask(__name__)

# Replace these with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = "123456789:ABCdefYourBotTokenHere"
TELEGRAM_CHAT_ID = "-1001234567890"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data:
        message = data.get('message', 'No message received')
        send_telegram_alert(message)
        return 'Message sent to Telegram', 200
    return 'Invalid request', 400

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # get Render's assigned port
    app.run(host='0.0.0.0', port=port)
