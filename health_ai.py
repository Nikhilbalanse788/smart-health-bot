import openai

def diagnose_symptom(symptom, api_key):
    openai.api_key = api_key

    prompt = f"""
You are a medical assistant. A user reports the symptom: "{symptom}".
Return a short diagnosis, likely causes, possible treatment, and health advice.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if you have access
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=300
    )

    result = response.choices[0].message.content.strip()
    return result
