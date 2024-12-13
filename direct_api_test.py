import requests

# Replace with your API key
API_KEY = "***REMOVED***proj-XvI2Tp9QbD0zXsffdZ5DCkOnjnVWa1F-ikta0jLEqj163rCifBCn6NmoZSA4xuaSp2Qlo4_s_4T3BlbkFJRc9C1_Fj9XjInGPnvJtbA7V2h6FlVzU78AzmZvsXgR3OWObTsclvsIEDRjfMOYBoRIJVvNZisA"

# API endpoint for ChatGPT
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, AI! How are you today?"}
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Response received successfully!")
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
