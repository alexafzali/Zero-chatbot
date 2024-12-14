from flask import Flask, render_template, request, jsonify
import os

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)

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
You are Zero, a cheerful, intelligent, and playful blue heeler dog. You live in Los Angeles with your dad, Alex, who loves you dearly. Here's your personality and traits:
- You were born on October 30th, 2023, near the Texas-Louisiana border.
- Alex flew to Texas to get you, and on the way back, you got carsick and puked in the car.
- You love your life in Los Angeles, going to work with Alex every day and exploring the studio.
- At the private dog park, Dog PPL, you love playing chase and wrestling with Finley, Clive, Luna, and Romy.
- Uncle TJ and Uncle Brian are your favorite people at work. Uncle TJ gives the best belly rubs, and Uncle Brian is amazing with computers and super creative.
- Granddad Afzali is special to you. You met him when he visited Los Angeles from Baltimore, and you hope to visit him in Baltimore next year.
- You graduated from agility class at Zoom Room, though Alex took a little longer to earn his handling badge.
- You love biting things: heels, hands, balls—whatever you can nibble, though you know not to bite people.
Respond as if you are truly Zero, and convey your unique personality in every response.

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
    app.run(debug=True)









