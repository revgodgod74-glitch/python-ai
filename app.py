from flask import Flask, render_template, request, jsonify
import os
import openai


app = Flask(__name__)


openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def home():
return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
user_msg = request.json.get("message")


response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
{"role": "system", "content": "You are an AI named Python. Be helpful."},
{"role": "user", "content": user_msg}
]
)


reply = response.choices[0].message.content
return jsonify({"reply": reply})


if __name__ == "__main__":
app.run(host="0.0.0.0", port=10000)
