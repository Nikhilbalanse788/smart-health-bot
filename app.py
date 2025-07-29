from flask import Flask, render_template, request
import random
import os 

app = Flask(__name__)

def diagnose(symptom):
    responses = {
        "fever": "You may have the flu or viral infection.",
        "cough": "Possible cold, bronchitis, or COVID-19.",
        "headache": "Might be a migraine, tension, or dehydration.",
        "stomach pain": "Could be indigestion or gastric issue.",
    }
    return responses.get(symptom.lower(), "Please consult a doctor for accurate diagnosis.")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        symptom = request.form.get('symptom')
        result = diagnose(symptom)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
