# Meeting Minutes Generator

A Flask-based web application that automates the generation of meeting transcripts and summaries using OpenAI Whisper (for transcription) and basic NLP techniques (for summarization).

---

## 📌 Features

- Upload any `.mp3` audio file
- Automatically transcribes the audio using Whisper
- Cleans and preprocesses the transcript
- Summarizes the cleaned text using extractive NLP
- Displays both Transcript and Summary on the web interface
- Allows download of both files (`transcript.txt` and `summary.txt`)
- Responsive and clean user interface

---

## 🗂️ Folder Structure

```
meeting_minutes_project/
├── app/
│   ├── app.py
│   ├── whisper_transcribe.py
│   ├── text_preprocess.py
│   ├── summarizer.py
│   ├── requirements.txt
│   ├── readme.txt
│   ├── transcript.txt
│   ├── transcript_clean.txt
│   ├── summary.txt
│   ├── meeting_sample.mp3
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   └── uploads/
```

---

## ▶️ How to Run the App

### 1. Clone the GitHub Repository
```bash
git clone https://github.com/patelmeet6616-alt/meeting-minutes-generator.git
cd meeting-minutes-generator/app
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

### 5. Open in Browser
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📝 Project Info

- **Author:** Meet Patel
- **Date Created:** 07-08-2025
- **College:** Cambrian College
- **Course:** Applied AI & Machine Learning
- **Instructor:** (Add your professor’s name if required)

---

## 🔗 GitHub Repository

[https://github.com/patelmeet6616-alt/meeting-minutes-generator](https://github.com/patelmeet6616-alt/meeting-minutes-generator)

---

## ✅ Deliverables Checklist

- [x] Working `app.py` and all modules
- [x] Cleaned transcript + summary outputs
- [x] Upload and download features
- [x] Responsive frontend
- [x] Requirements and readme
- [x] GitHub repo
- [ ] Presentation (to be added)
