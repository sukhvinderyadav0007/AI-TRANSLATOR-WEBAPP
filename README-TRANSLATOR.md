# 🌍 English to Hindi, Korean & French Translator

A Flask-based web application that translates English text to Hindi, Korean, and French using advanced machine learning models.

## Features

- ✨ Translate English to:
  - 🇮🇳 Hindi
  - 🇰🇷 Korean
  - 🇫🇷 French
- 🚀 Fast and accurate translations using Helsinki-NLP models
- 🎨 Beautiful and responsive UI
- 📱 Mobile-friendly design

## Requirements

- Python 3.7+
- Flask
- Transformers
- PyTorch
- Sentencepiece

## Installation

1. **Clone the repository:**
   ```bash
   cd AI-TRANSLATOR-WEBAPP
   ```

2. **Create a virtual environment:**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask app:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Use the translator:**
   - Select your target language (Hindi, Korean, or French)
   - Enter English text
   - Click "Translate 🚀" button
   - View the translated result

## How It Works

The application uses the **Helsinki-NLP Opus-MT** pre-trained models for machine translation:

- **English → Hindi:** `Helsinki-NLP/opus-mt-en-hi`
- **English → Korean:** `Helsinki-NLP/opus-mt-en-ko`
- **English → French:** `Helsinki-NLP/opus-mt-en-fr`

These models are downloaded automatically on first use and cached for faster subsequent translations.

## Project Structure

```
AI-TRANSLATOR-WEBAPP/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web UI
├── static/
│   └── css/
│       └── style.css     # Styling
└── README.md             # Documentation
```

## Usage Examples

**English:** "Hello, how are you?"
**Hindi:** "नमस्ते, आप कैसे हैं?"

**English:** "Thank you very much"
**Korean:** "감사합니다"

**English:** "Good morning everyone"
**French:** "Bonjour à tous"

## Performance Notes

- First translation may take longer as models are downloaded and loaded
- Subsequent translations are faster due to model caching
- For large texts, processing may take a few seconds

## Troubleshooting

If you face issues with model downloads:
1. Check your internet connection
2. Ensure you have enough disk space (~2-3 GB)
3. Try clearing the cache: `rm -rf ~/.cache/huggingface/` (Linux/Mac) or `rmdir %USERPROFILE%\.cache\huggingface` (Windows)

## Deployment

To deploy on Vercel, Heroku, or other platforms:
1. Ensure `requirements.txt` contains all dependencies
2. Set appropriate environment variables
3. Note: Model loading may require sufficient memory (~2-4 GB)

## License

MIT License - Feel free to use this project for personal and commercial use.

## Support

For issues or improvements, please open a GitHub issue.

---

Made with ❤️ for language learners and multilingual communication.
