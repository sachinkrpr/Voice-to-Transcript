Whisper Audio Transcription Script
A powerful and easy-to-use Python script to batch transcribe audio files (.opus or other formats) into text using OpenAI's Whisper model.

This script automatically finds all audio files in its directory, processes them through your chosen Whisper model, and saves the complete transcription into a single, well-organized text file.

Features
Batch Processing: Transcribe multiple audio files at once.

High-Quality Transcription: Leverages the power of OpenAI's Whisper models (from tiny to large).

Language Specific: Easily set the audio language for improved accuracy.

Simple to Use: Just place your audio files in the folder and run the script.

Organized Output: Generates a detailed report with timestamps, model details, and clear transcription for each file.

Progress Tracking: Uses tqdm to show a live progress bar.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7+: You can download it from python.org.

FFmpeg: Whisper requires FFmpeg to process audio files.

On Windows (using Chocolatey):

choco install ffmpeg

On macOS (using Homebrew):

brew install ffmpeg

On Linux (using apt):

sudo apt update && sudo apt install ffmpeg

Installation
Clone the repository or download the script:
Save the Python script (e.g., transcribe.py) to a new folder on your computer.

Install the required Python libraries:
Open your terminal or command prompt, navigate to the script's directory, and run the following command:

pip install openai-whisper tqdm

How to Use
Place Your Audio Files:
Copy all the .opus (or other audio format) files you want to transcribe into the same folder where you saved the transcribe.py script.

Customize the Script (Optional):
Open the script in a text editor and modify the configuration variables at the top of the file to suit your needs:

MODEL_SIZE: Change the Whisper model. Options are tiny, base, small, medium, and large. Larger models are more accurate but require more resources and time.

LANGUAGE: Set the two-letter code for the language spoken in the audio files (e.g., 'en' for English, 'es' for Spanish, 'hi' for Hindi). Set to None to let Whisper auto-detect the language.

# --- CONFIGURATION ---
MODEL_SIZE = "large"  # Or "base", "small", "medium", etc.
LANGUAGE = "hi"       # e.g., 'en', 'es', 'fr'. Set to None for auto-detect.
# ---------------------

Run the Script:
Navigate to the script's directory in your terminal or command prompt and execute it:

python transcribe.py

The script will now scan for audio files, load the Whisper model, and begin the transcription process. You will see a progress bar tracking the files.

Output
Once the script is finished, it will generate a file named transcription_output.txt in the same directory.

This file contains:

A header with the report generation time, model used, and language.

A separate entry for each audio file, showing its name and the corresponding transcription.

Error messages for any files that could not be processed.

Example transcription_output.txt:

--- Transcription Report ---
Generated on: 2023-10-27 14:30:00
Model used: large
Language: hi
--------------------------------

File: PTT-20231026-WA0001.opus
Transcription: नमस्ते, यह एक परीक्षण ऑडियो है।
---

File: PTT-20231027-WA0002.opus
Transcription: [ERROR] - Could not process 'PTT-20231027-WA0002.opus'.
---


License
This project is licensed under the MIT License. See the LICENSE file for details.
