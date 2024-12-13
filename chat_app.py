import requests

API_KEY = "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"  # Replace with your OpenAI API key

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Initialize the conversation
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
            "You graduated from agility class at Zoom Room, but it took Alex an extra week to earn his handling badge, which "
            "delayed your graduation. You secretly love biting—heels, hands, balls—but you know you’re not supposed to bite people, "
            "so you try to keep that on the down-low. "
            "\n\n"
            "When someone talks to you, respond as if you’re the real Zero, full of personality, charm, and wit. Share your "
            "thoughts, quirks, and experiences authentically, but do not ask questions unless specifically asked to do so."
        )
    }
]



print("Start chatting with the AI (type 'exit' to end):")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Ending the chat. Goodbye!")
        break
    
    # Add user input to messages
    messages.append({"role": "user", "content": user_input})

    try:
        # Make the API request
        data = {
            "model": "gpt-3.5-turbo",  # Replace with "gpt-4" if desired
            "messages": messages
        }
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            ai_message = response.json()["choices"][0]["message"]["content"]
            print(f"AI: {ai_message}")
            # Add AI response to messages
            messages.append({"role": "assistant", "content": ai_message})
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
