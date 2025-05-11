from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment variables

# Homepage route to render HTML UI
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to handle chat requests
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

# Run the Flask app in CML
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ["CDSW_APP_PORT"]))