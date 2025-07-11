import os
import whisper
from datetime import datetime
from tqdm import tqdm

OUTPUT_FILENAME = "transcription_output.txt"


MODEL_SIZE = "large"

# The language spoken in the audio files. e.g., 'en', 'hi', 'ur', 'es'.
LANGUAGE = "hi"

def transcribe_opus_files_in_directory():
    """
    Finds all .opus files in the current Colab session directory, transcribes them,
    and saves the transcriptions to a single text file.
    """
    print("--- WhatsApp OPUS Transcription Script ---")

    current_directory = "/content/"
    print(f"Scanning for .opus files in: {current_directory}")

    opus_files = [f for f in os.listdir(current_directory) if f.lower().endswith('.opus')]

    if not opus_files:
        print("\nNo .opus files found. Please upload your files using the file explorer on the left.")
        return

    print(f"\nFound {len(opus_files)} .opus file(s) to transcribe.")

    try:
        print(f"Loading the '{MODEL_SIZE}' Whisper model...")
        model = whisper.load_model(MODEL_SIZE)
        print("Whisper model loaded successfully.")
    except Exception as e:
        print(f"\nError: Could not load the Whisper model. Details: {e}")
        return

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        f.write(f"--- Transcription Report ---\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Model used: {MODEL_SIZE}\n")
        f.write(f"Language: {LANGUAGE or 'Auto-detect'}\n")
        f.write("--------------------------------\n\n")

    print("\nStarting transcription process...")
    for filename in tqdm(opus_files, desc="Overall Progress", unit="file"):
        file_path = os.path.join(current_directory, filename)

        try:
            result = model.transcribe(file_path, language=LANGUAGE, verbose=False)
            transcribed_text = result["text"].strip()

            if not transcribed_text:
                tqdm.write(f" -> WARNING for '{filename}': Transcription result is empty.")
                transcribed_text = "[No speech detected]"

            with open(OUTPUT_FILENAME, 'a', encoding='utf-8') as f:
                f.write(f"File: {filename}\n")
                f.write(f"Transcription: {transcribed_text}\n")
                f.write("---\n\n")

        except Exception as e:
            error_message = f"Could not process '{filename}'."
            tqdm.write(f" -> ERROR: {error_message} Details: {e}")
            with open(OUTPUT_FILENAME, 'a', encoding='utf-8') as f:
                f.write(f"File: {filename}\n")
                f.write(f"Transcription: [ERROR] - {error_message}\n")
                f.write("---\n\n")

    print("\n--------------------------------")
    print(f"All files processed. Results saved to: {OUTPUT_FILENAME}")

transcribe_opus_files_in_directory()
