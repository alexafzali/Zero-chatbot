import requests

API_KEY = "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"  # Replace with your OpenAI API key

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-3.5-turbo",  # Replace with "gpt-4" if desired and accessible
    "messages": [{"role": "user", "content": "Hello!"}]
}

try:
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Response:", response.json()["choices"][0]["message"]["content"])
    else:
        print(f"Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")

