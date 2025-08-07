Project: AI-Powered Meeting Minutes Generator
Phase: 1 - Functional Prototype (Transcription Only)

This submission demonstrates the initial implementation of a meeting minutes generator using OpenAI Whisper. The goal is to automatically transcribe meeting audio and extract clear summaries and actionable items.

---

📂 Folder Contents:

- app/
  ├── whisper_transcribe.py : Python script that transcribes sample.mp3 using Whisper
  ├── app.py                : (Optional) Flask starter file for web-based interface
  ├── requirements.txt      : Libraries used in this phase
  ├── sample.mp3            : Test audio file for transcription
  └── transcript.txt        : Transcript generated from Whisper output

- Project_Update_Phase1_PPT.pptx : 4-slide Phase 1 project update presentation

---

▶ How to Run:

1. Install dependencies:
   pip install -r requirements.txt

2. Run transcription:
   python whisper_transcribe.py

3. Output will be saved in:
   transcript.txt

---

Next Steps:
- Build web interface using Flask
- Add real-time audio upload & dynamic transcription
- Implement summarization and action-item extraction (Phase 2)

