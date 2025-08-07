import whisper

def transcribe_audio(file_path='meeting_sample.mp3', output_file='transcript.txt'):
    print("Loading Whisper model...")
    model = whisper.load_model("base")  # using 'base' model for faster demo; can switch to 'small' or 'medium' for better accuracy
    print("Transcribing audio...")
    
    # To transcribe the audio file
    result = model.transcribe(file_path)
    
    # To save transcript to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f" Transcription complete. Saved to {output_file}")
    return result["text"]

# Run directly (for testing)
if __name__ == "__main__":
    transcribe_audio()
