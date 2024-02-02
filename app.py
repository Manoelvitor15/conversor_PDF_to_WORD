from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pdf2docx import Converter
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    if 'pdfFile' not in request.files:
        return "Nenhum arquivo enviado."

    pdf_file = request.files['pdfFile']

    if pdf_file.filename == '':
        return "Nome do arquivo não encontrado."

    if pdf_file:
        # Salva o arquivo PDF no diretório de uploads
        upload_dir = 'uploads'
        os.makedirs(upload_dir, exist_ok=True)

        pdf_filename = os.path.join(upload_dir, pdf_file.filename)
        pdf_file.save(pdf_filename)

        # Lógica de conversão usando a biblioteca pdf2docx
        word_filename = os.path.splitext(pdf_filename)[0] + '.docx'
        convert_pdf_to_word(pdf_filename, word_filename)

        return redirect(url_for('download', filename=os.path.basename(word_filename)))

def convert_pdf_to_word(pdf_filename, word_filename):
    # Usa a biblioteca pdf2docx para converter PDF para Word
    cv = Converter(pdf_filename)
    cv.convert(word_filename, start=0, end=None)
    cv.close()

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
