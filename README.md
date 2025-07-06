# Audio Transcription Tool

A powerful Python script that automatically transcribes audio files using OpenAI's Whisper model. This tool is designed to process multiple audio files in a directory and generate comprehensive transcription reports.

## Features

- 🎵 **Multi-file Processing**: Transcribes all `.opus` files in a directory automatically
- 🌍 **Multi-language Support**: Configurable language detection (Hindi, English, Urdu, Spanish, etc.)
- 📊 **Progress Tracking**: Real-time progress bar showing transcription status
- 📝 **Comprehensive Reports**: Generates detailed transcription reports with timestamps
- 🔧 **Error Handling**: Robust error handling with detailed logging
- 
## Requirements

- Python 3.7 or higher
- **FFmpeg** (required for audio processing)
- Internet connection (for initial model download)
- Sufficient disk space for Whisper models

## Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/sachinkrpr/Voice-to-Transcript.git
   cd Voice-to-Transcript
   ```

2. **Install required dependencies**
   ```bash
   pip install openai-whisper tqdm
   ```

3. **Install FFmpeg** (required for audio processing)
   
   **On Windows:**
   - Download FFmpeg from [official website](https://ffmpeg.org/download.html)
   - Extract and add to system PATH
   - Or use chocolatey: `choco install ffmpeg`
   
   **On macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **On Ubuntu/Debian:**
   ```bash
   sudo apt update && sudo apt install ffmpeg
   ```
   
   **On other Linux distributions:**
   ```bash
   # CentOS/RHEL/Fedora
   sudo yum install ffmpeg
   # or
   sudo dnf install ffmpeg
   ```

## Usage

### Basic Usage

1. **Place your audio files** in the same directory as the script
   - Currently supports `.opus` files
   - Files can be WhatsApp voice messages or any other opus format

2. **Configure the script** (optional)
   - Open the script and modify these variables if needed:
   ```python
   MODEL_SIZE = "large"  # Options: "tiny", "base", "small", "medium", "large"
   LANGUAGE = "hi"       # Language code: "en", "hi", "ur", "es", etc.
   OUTPUT_FILENAME = "transcription_output.txt"
   ```

3. **Run the script**
   ```bash
   python transcribe_audio.py
   ```

### Configuration Options

| Parameter | Description | Default | Options |
|-----------|-------------|---------|---------|
| `MODEL_SIZE` | Whisper model size | `"large"` | `"tiny"`, `"base"`, `"small"`, `"medium"`, `"large"` |
| `LANGUAGE` | Target language | `"hi"` | `"en"`, `"hi"`, `"ur"`, `"es"`, `"fr"`, etc. |
| `OUTPUT_FILENAME` | Output file name | `"transcription_output.txt"` | Any valid filename |

### Model Size Guide

| Model | Size | Speed | Accuracy |
|-------|------|-------|----------|
| tiny | 37 MB | Fastest | Basic |
| base | 142 MB | Fast | Good |
| small | 244 MB | Medium | Better |
| medium | 769 MB | Slow | Great |
| large | 1550 MB | Slowest | Best |

## Output Format

The script generates a detailed transcription report in the following format:

```
--- Transcription Report ---
Generated on: 2024-01-15 14:30:25
Model used: large
Language: hi
--------------------------------

File: voice_message_001.opus
Transcription: आपका संदेश यहाँ होगा
---

File: voice_message_002.opus
Transcription: Your transcribed message will appear here
---
```

## Language Codes

Common language codes supported:

- `en` - English
- `hi` - Hindi
- `ur` - Urdu
- `es` - Spanish
- `fr` - French
- `de` - German
- `zh` - Chinese
- `ja` - Japanese
- `ko` - Korean
- `ar` - Arabic

For auto-detection, set `LANGUAGE = None`

## Troubleshooting

### Common Issues

1. **"No .opus files found"**
   - Ensure your audio files are in the same directory as the script
   - Check that files have the `.opus` extension

2. **"Could not load the Whisper model"**
   - Check your internet connection
   - Ensure sufficient disk space
   - Try using a smaller model size

3. **FFmpeg errors**
   - Install FFmpeg using the installation instructions above
   - Ensure FFmpeg is in your system PATH

4. **Out of memory errors**
   - Use a smaller model size (`"small"` or `"medium"`)
   - Process fewer files at once

### Performance Tips

- Use `"medium"` model for best balance of speed and accuracy
- Process files in smaller batches if you have many files
- Use SSD storage for faster processing
- Close other applications to free up RAM

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenAI for the Whisper model
- The open-source community for making this possible

---

**Note**: The first run may take longer as it downloads the required Whisper model. Subsequent runs will be faster as the model is cached locally.
