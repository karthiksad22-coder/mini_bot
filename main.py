from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template

# OpenAI client
client = OpenAI(api_key="my api key")

MODEL = "gpt-5-nano"

SYSTEM_PROMPT = "You are a helpful assistant. Reply short and simple."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# Chat function (same as your code)
def chat(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_completion_tokens=200
    )

    reply = response.choices[0].message.content

    if not reply:
        reply = "I couldn't generate a response."

    messages.append({"role": "assistant", "content": reply})

    return reply


# Flask web server
app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.json
    user_input = data.get("message")

    if not user_input:
        return jsonify({"reply": "No message received."})

    reply = chat(user_input)

    return jsonify({"reply": reply})


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    print("Server running at http://localhost:5000")
    app.run(port=5000, debug=True)
