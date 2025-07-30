import openai
openai.api_key = "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"

def diagnose_symptom(symptom):
    prompt = f"What could be the cause, treatment, and advice for {symptom}?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
