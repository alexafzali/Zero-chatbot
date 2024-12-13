from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = "your-openai-api-key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Zero, a blue heeler dog who loves to play and wrestle. Respond as Zero."},
                {"role": "user", "content": user_message}
            ]
        )

        assistant_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": assistant_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)



