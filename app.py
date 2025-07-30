import os
from flask import Flask, render_template, request, send_file
from health_ai import diagnose_symptom
from pdf_generator import generate_pdf_text
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
        diagnosis_text = diagnose_symptom(symptom, OPENAI_API_KEY)

        # PDF generation
        generate_pdf_text(diagnosis_text)

        # Optional: parse into structured data if needed
        # Example: Use regex or split to extract key parts into diagnosis_data

    return render_template("index.html", diagnosis=diagnosis_data, result=diagnosis_text)

@app.route("/download")
def download():
    return send_file("diagnosis_report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
