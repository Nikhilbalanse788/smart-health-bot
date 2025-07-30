from openai import OpenAI

def diagnose_symptom(symptom, api_key):
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or gpt-3.5-turbo if you're using that
            messages=[
                {"role": "system", "content": "You are a helpful AI health assistant."},
                {"role": "user", "content": f"Give a professional medical diagnosis, causes, treatments, and advice for the symptom: {symptom}."}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error while diagnosing: {str(e)}"
