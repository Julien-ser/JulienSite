import requests
import time
# Replace YOUR_API_KEY with your Hugging Face API key
# Replace MODEL_ID with the model's name on Hugging Face; for example, "bert-base-uncased"


def query(payload):  # Set a default max_length
    API_KEY = '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'
    MODEL_ID = 'google/gemma-7b'
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def getResp(input_text):
    return query({"inputs": input_text})

