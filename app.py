from flask import Flask, render_template, request, send_file
from health_ai import diagnose_symptom
from pdf_generator import generate_pdf_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis_text = ""
    if request.method == "POST":
        symptom = request.form["symptom"]
        diagnosis_text = diagnose_symptom(symptom)
        generate_pdf_text(diagnosis_text)
    return render_template("index.html", diagnosis={"condition": "See below", "causes": "", "treatment": "", "advice": ""}, result=diagnosis_text)

@app.route("/download")
def download():
    return send_file("diagnosis_report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
