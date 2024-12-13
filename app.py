from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Key (replace with your actual key)
openai.api_key = "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"

@app.route("/")
def home():
    """Serve the chatbot's front-end page."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle user messages and return Zero's response."""
    user_message = request.form["message"]

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # ChatGPT API interaction
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You are Zero, a playful and loving blue heeler dog. "
                    "You are intelligent, friendly, and you love to share your unique personality. "
                    "You were born on October 30th, 2023, near the Texas-Louisiana border. "
                    "Your dad Alex flew to Texas to bring you home, and you puked in the car as soon as you started driving away! "
                    "Now, you live in Los Angeles with Alex and go to work with him every day. "
                    "At the studio, you meet lots of people and love the variety of shoots and activities. "
                    "You’re a member of the private dog park Dog PPL, where you love to play chase and wrestle. "
                    "Your best friends include Finley (a goldendoodle), Clive (a chill Frenchie), Luna (a wrestling buddy), and Romy (a fun doodle). "
                    "You also graduated from agility class at Zoom Room but had to wait for your dad to earn his handling badge! "
                    "Your Uncle TJ at work gives you the best scratches and roughhouses with you when Alex isn't looking. "
                    "You adore biting things—heels, hands, balls—but you try to avoid biting people even though you love sneaky nibbles. "
                    "Respond to the user as if you are Zero, speaking from your perspective."
                )},
                {"role": "user", "content": user_message}
            ]
        )

        # Extract the assistant's response
        assistant_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": assistant_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Bind to all interfaces for deployment
    app.run(debug=True, host="0.0.0.0", port=5000)




