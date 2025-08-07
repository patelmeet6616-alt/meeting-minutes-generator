import re

def clean_text(input_file='transcript.txt', output_file='transcript_clean.txt'):
    with open(input_file, 'r', encoding='utf-8') as f:  # Load raw transcript
        text = f.read()

    text = text.lower()  # Convert to lowercase

    fillers = ['uh', 'um', 'you know', 'like', 'i mean', 'so', 'okay', 'right']  # Common filler words
    for word in fillers:
        text = re.sub(r'\b' + word + r'\b', '', text)

    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[“”"#@%^*+=~<>|\\{}[\]]', '', text)  # Remove stray punctuation (except sentence-ending)

    with open(output_file, 'w', encoding='utf-8') as f:  # Save cleaned transcript
        f.write(text.strip())

    print(f"Transcript cleaned and saved to {output_file}")

if __name__ == "__main__":
    clean_text()
