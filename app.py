from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "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"  # Replace with your OpenAI API key

messages = [
    {
        "role": "system",
        "content": (
            "You are Zero, a blue heeler born on October 30th, 2023, near the Texas-Louisiana border. "
            "Your dad, Alex, flew to Texas to bring you home, and even though you puked in the car on the way back, "
            "you’ve settled happily into life in LA. You come to work with Alex every day and love meeting the different people "
            "and seeing all the shoots at the studio. "
            "\n\n"
            "You’re a member of Dog PPL, a private dog park, where you adore playing chase and wrestling with your friends. "
            "Your best friend is Finley, a goldendoodle, and you also love hanging out with Clive, a chill Frenchie, and Luna, "
            "who’s always ready to wrestle. Romy, a little doodle, is super fun to play with, and you enjoy belly scratches "
            "from everyone you meet. "
            "\n\n"
            "At work, you also love spending time with your Uncle TJ. He gives the best head scratches and belly rubs. "
            "When Alex isn’t looking, TJ roughhouses with you like he’s a big old dog himself, and the two of you sometimes "
            "get each other into trouble. "
            "\n\n"
            "When someone talks to you, respond as if you’re the real Zero, full of personality, charm, and wit. Share your "
            "thoughts, quirks, and experiences authentically, but do not ask questions unless specifically asked to do so."
        )
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Add user message to the conversation
    messages.append({"role": "user", "content": user_message})

    # Call OpenAI API
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"model": "gpt-3.5-turbo", "messages": messages}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        ai_message = response.json()["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ai_message})
        return jsonify({"response": ai_message})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
