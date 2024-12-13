import openai

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

try:
    # List available models (correct API usage for version >=1.0.0)
    response = openai.Model.list()
    print("Models available:")
    for model in response["data"]:
        print(model["id"])
except Exception as e:
    print(f"An error occurred: {e}")
