from flask import Flask, render_template, request, send_from_directory
from whisper_transcribe import transcribe_audio
from text_preprocess import clean_text
from summarizer import generate_summary
import os
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    transcript = ''
    summary = ''

    if request.method == 'POST':
        file = request.files['file']
        if file:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{file.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Transcription
            transcribe_audio(filepath)

            # Text Cleaning
            clean_text()

            # Summarization
            generate_summary()

            # Load cleaned transcript and summary
            with open('transcript_clean.txt', 'r', encoding='utf-8') as f:
                transcript = f.read()

            with open('summary.txt', 'r', encoding='utf-8') as f:
                summary = f.read()

    return render_template('index.html', transcript=transcript, summary=summary)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('.', filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
