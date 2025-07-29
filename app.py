from flask import Flask, render_template, request
import random
import os 

app = Flask(__name__)

def diagnose(symptom):
    responses = {
        "fever": {
            "condition": "Flu or Viral Infection",
            "causes": "Infection by virus or bacteria, seasonal flu",
            "treatment": "Rest, hydration, paracetamol for fever, consult doctor if persistent",
            "advice": "Monitor temperature regularly. Seek medical help if fever lasts more than 3 days."
        },
        "cough": {
            "condition": "Cold, Bronchitis, or COVID-19",
            "causes": "Viral infection, dust, pollution, or allergies",
            "treatment": "Cough syrup, steam inhalation, stay hydrated",
            "advice": "If cough lasts >7 days or accompanied by fever, consult a doctor."
        },
        "headache": {
            "condition": "Migraine or Dehydration",
            "causes": "Stress, dehydration, eye strain, or lack of sleep",
            "treatment": "Drink water, rest in a dark room, take a pain reliever",
            "advice": "Avoid screens, get good sleep. Visit doctor if headaches are frequent."
        },
        "stomach pain": {
            "condition": "Indigestion or Gastric issue",
            "causes": "Overeating, food poisoning, acidity",
            "treatment": "Antacids, drink warm water, avoid oily/spicy food",
            "advice": "If pain is severe or you have vomiting/diarrhea, consult a physician." 
         "sore throat": {
    "condition": "Throat Infection",
    "causes": "Viral or bacterial infection, cold",
    "treatment": "Warm salt water gargle, throat lozenges",
    "advice": "Avoid cold foods, visit doctor if pain persists."
},
"cold": {
    "condition": "Common Cold",
    "causes": "Rhinovirus infection",
    "treatment": "Rest, fluids, nasal drops, paracetamol",
    "advice": "Avoid cold drinks, keep warm."
},
"fatigue": {
    "condition": "Tiredness or Nutritional Deficiency",
    "causes": "Lack of sleep, poor diet, stress",
    "treatment": "Eat balanced food, rest, stay hydrated",
    "advice": "If persistent, get a blood test."
},
"chest pain": {
    "condition": "Could be muscular or cardiac",
    "causes": "Muscle strain, acidity, or heart issues",
    "treatment": "Rest, avoid exertion, antacids",
    "advice": "If pain is sharp or with breathlessness, rush to hospital."
}
   
        }
    }

    return responses.get(symptom.lower(), {
        "condition": "Unknown",
        "causes": "Unrecognized symptom",
        "treatment": "Consult a medical professional.",
        "advice": "Please see a doctor for accurate diagnosis."
    })

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = {}
    if request.method == 'POST':
        symptom = request.form.get('symptom')
        diagnosis = diagnose(symptom)
    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


