from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment variables

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})


if __name__ == "__main__":
    # port = int(os.environ.get("PORT",8080))
    # app.run(host='127.0.0.1', port=int(os.environ['CDSW_APP_PORT']))
    app.run(debug=True, port=5001)