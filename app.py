from flask import Flask, render_template, request, send_file
from health_ai import diagnose_symptom
from pdf_generator import generate_pdf_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        symptom = request.form["symptom"]
        result = diagnose_symptom(symptom)
        generate_pdf_text(result)
    return render_template("index.html", result=result)

@app.route("/download")
def download():
    return send_file("diagnosis_report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
