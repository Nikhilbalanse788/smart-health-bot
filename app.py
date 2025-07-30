from flask import Flask, request, render_template, send_file
import os
from health_ai import diagnose_symptom
from pdf_generator import generate_pdf_text

app = Flask(__name__)

# ✅ Get your OpenAI API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis_text = ""
    if request.method == "POST":
        symptom = request.form.get("symptom", "").strip()
        print("🧾 Received symptom:", symptom)

        if not symptom:
            diagnosis_text = "Please enter a symptom."
        elif not OPENAI_API_KEY:
            diagnosis_text = "OpenAI API key is not set. Please check your .env file or environment variable."
        else:
            try:
                diagnosis_text = diagnose_symptom(symptom, OPENAI_API_KEY)
                print("✅ Diagnosis text:", diagnosis_text)

                try:
                    generate_pdf_text(diagnosis_text)
                except Exception as pdf_error:
                    print("⚠️ PDF generation error:", pdf_error)
            except Exception as ai_error:
                print("❌ OpenAI error:", ai_error)
                diagnosis_text = f"Error while diagnosing: {str(ai_error)}"

    return render_template("index.html", result=diagnosis_text)

@app.route("/download")
def download():
    try:
        return send_file("diagnosis_report.pdf", as_attachment=True)
    except Exception as e:
        print("❌ PDF download error:", e)
        return "Failed to download PDF."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
