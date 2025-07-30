from fpdf import FPDF

def generate_pdf_text(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output("diagnosis_report.pdf")
