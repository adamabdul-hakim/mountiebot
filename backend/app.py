from flask import Flask, request, jsonify
from flask_cors import CORS
from mountiebot.chatbot import bot_response

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")
        response = bot_response(message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
