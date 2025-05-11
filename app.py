from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize the OpenAI client using the new SDK format
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Homepage route – serves the chat UI
@app.route("/")
def index():
    return render_template("index.html")

# Chat endpoint – handles POST requests from frontend
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo" if needed
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the app in CML environment
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ["CDSW_APP_PORT"]))