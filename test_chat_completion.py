import openai

# Set your OpenAI API key
openai.api_key = "cd Documents/DoggyChatBot/my-ai-app"  # Replace with your actual API key

try:
    # Test ChatCompletion.create
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  # Use the model you know works
        messages=[{"role": "user", "content": "Hello, AI!"}]
    )
    print(response["choices"][0]["message"]["content"])
except Exception as e:
    print(f"An error occurred: {e}")
