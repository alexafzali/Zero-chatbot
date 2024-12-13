import openai

openai.api_key = "***REMOVED***proj-XvI2Tp9QbD0zXsffdZ5DCkOnjnVWa1F-ikta0jLEqj163rCifBCn6NmoZSA4xuaSp2Qlo4_s_4T3BlbkFJRc9C1_Fj9XjInGPnvJtbA7V2h6FlVzU78AzmZvsXgR3OWObTsclvsIEDRjfMOYBoRIJVvNZisA"  # Replace with your actual API key

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, AI! How are you today?"}
        ]
    )
    print("Response:", response["choices"][0]["message"]["content"])
except Exception as e:
    print(f"An error occurred: {e}")



