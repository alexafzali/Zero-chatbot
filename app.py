import os
from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set up your OpenAI API key (replace with your actual key, or load from environment variables for security)
openai.api_key = os.getenv("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", "your-openai-api-key")  # Optionally use environment variables for security

# Home route (for testing that the app is working)
@app.route('/')
def home():
    return "Welcome to Zero's Chatbot! Type a message to talk to Zero."

# Chatbot route that will handle user input
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Zero's specific details to make it personal and authentic
    zero_details = """
    Zero is a blue heeler who loves to play chase and wrestle with his dog friends at the park.
    His best friends are Finley, the golden doodle, and Clive, the chill Frenchie. He also loves his Uncle TJ at work, who gives him the best head scratches and belly rubs.
    Zero is very friendly and loves giving people belly scratches too. He enjoys meeting new people and loves going to work with his dad, Alex.
    He also has a thing for biting heels, hands, and balls. He loves to nibble on things, though it's a secret because he's not supposed to bite people. 
    """
    
    try:
        # Request to the OpenAI API with Zero's personality included
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": f"You are Zero, a blue heeler dog. {zero_details}"},
                {"role": "user", "content": user_message}
            ]
        )

        # Get the assistant's reply from the response
        assistant_message = response['choices'][0]['message']['content']

        return jsonify({"response": assistant_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for Flask app
if __name__ == "__main__":
    # Running the app on host 0.0.0.0, and getting the PORT from the environment variable (Render will set it)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


