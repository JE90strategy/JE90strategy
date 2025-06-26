import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ✅ Define 'port' before using it
    app.run(host='0.0.0.0', port=port)
