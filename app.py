import openai

def diagnose_symptom(symptom, api_key):
    prompt = f"Give a professional medical diagnosis, causes, treatments, and advice for the symptom: {symptom}."

    try:
        openai.api_key = api_key

        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or gpt-3.5-turbo if needed
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
