import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def diagnose_symptom(symptom):
    prompt = f"Give a professional medical diagnosis, causes, treatments, and advice for the symptom: {symptom}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI health assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        result = response['choices'][0]['message']['content']
        return result.strip()

    except Exception as e:
        return f"Error: {str(e)}"
