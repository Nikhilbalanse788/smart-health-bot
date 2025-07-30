import os
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
from health_ai import diagnose_symptom
from pdf_generator import generate_pdf_text

# Load environment variables from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing from .env file!")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis_text = ""
    diagnosis_data = {
        "condition": "See below",
        "causes": "",
        "treatment": "",
        "advice": ""
    }

    if request.method == "POST":
        symptom = request.form["symptom"]
        
        # ✅ Fix: Pass the API key to the diagnose function
        diagnosis_text = diagnose_symptom(symptom, OPENAI_API_KEY)

        # ✅ Optional: Save to PDF
        generate_pdf_text(diagnosis_text)

        # Optional: Extract structured data from response (future enhancement)
        # Example: use regex to parse condition/causes/treatment/advice

    return render_template("index.html", diagnosis=diagnosis_data, result=diagnosis_text)

@app.route("/download")
def download():
    return send_file("diagnosis_report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
