from transformers import pipeline

def generate_summary(input_file='transcript_clean.txt', output_file='summary.txt'):

    with open(input_file, 'r', encoding='utf-8') as f:    # To load cleaned transcript
        text = f.read()

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")    # To initialize summarization pipeline


    max_chunk_size = 1024
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]    # To break text into chunks (BART has a max token limit ~1024 words)


    print(" Generating summary...")
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=60, min_length=20, do_sample=False)    # To generate summary for each chunk
        summary += result[0]['summary_text'] + "\n"


    with open(output_file, 'w', encoding='utf-8') as f:    # To save summary
        f.write(summary.strip())

    print(f"Summary generated and saved to {output_file}")
    return summary


if __name__ == "__main__":   # To run directly for testing
    generate_summary()
