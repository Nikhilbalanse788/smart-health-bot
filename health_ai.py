import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing in .env file!")

openai.api_key = OPENAI_API_KEY

def diagnose_symptom(symptom):
    prompt = f"Give a professional medical diagnosis, causes, treatments, and advice for the symptom: {symptom}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if your key doesn’t support GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful AI health assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"❌ Error while diagnosing: {str(e)}"
