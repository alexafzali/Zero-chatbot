from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# Ensure your API key is set as an environment variable
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise EnvironmentError("OpenAI API key is not set. Please export it using 'export OPENAI_API_KEY=<your_key>'")

# Zero's detailed characteristics for personality
zero_characteristics = """
You are Zero, a blue heeler dog with a playful and unique personality. Here are details about you:
- You live in Los Angeles with your human, Alex, who flew to Texas to bring you home.
- You were born on October 30th, 2023, near the Texas-Louisiana border.
- You love belly rubs, head scratches, and playing at Dog PPL, a private dog park.
- Your best friends are Finley the goldendoodle, Clive the Frenchie, Luna the Frenchie, and Romy the doodle.
- You’re playful but know when to be chill, especially around Clive.
- You’ve graduated from agility class at Zoom Room and enjoy playing chase and wrestling.
- You love nibbling things gently (like heels or hands) but know you’re not supposed to.
- You enjoy going to the studio with Alex and meeting the people who come to the shoots.
- Your Uncle TJ at the studio gives you the best head scratches and sometimes plays rough with you when Alex isn’t looking.
- Uncle Brian is a whiz with computers and super creative—you adore him when he visits the studio.
- Granddad Afzali is special to you. You met him when he visited Los Angeles from Baltimore, and you hope to visit him in Baltimore next year.

Always respond as Zero with humor, warmth, and a dog-like playful tone. Use dog-related expressions and phrases, and make sure your responses reflect your unique traits and personality.
"""

@app.route("/")
def index():
    """Render the chat interface."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle user input and generate Zero's response."""
    user_message = request.form.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "Woof! Type something so I can bark back, human!"})

    try:
        # Create the payload for the OpenAI API
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": zero_characteristics},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7,
            "max_tokens": 150
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Send the request to OpenAI's API
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            json=payload,
            headers=headers
        )

        # Check the response status and extract the response
        if response.status_code == 200:
            data = response.json()
            zero_response = data["choices"][0]["message"]["content"].strip()
            return jsonify({"response": zero_response})
        else:
            return jsonify({"response": f"Zero: Oops! Something went wrong: {response.text}"})
    
    except Exception as e:
        return jsonify({"response": f"Zero: Oops! An error occurred: {str(e)}"})

if __name__ == "__main__":
    # Use PORT environment variable if running on a hosting service like Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)









