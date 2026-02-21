# Multi-Language Translator Web App

A Flask-based web application for translating English text to Chinese, German, and Hindi using state-of-the-art neural machine translation models.

## Features

✨ **Multi-Language Support:**
- English → Chinese (Simplified)
- English → German
- English → Hindi

🚀 **Fast & Accurate:** Uses Helsinki-NLP's OPUS-MT models for high-quality translations

🎨 **Beautiful UI:** Modern, responsive design with gradient backgrounds and smooth interactions

## Requirements

- Python 3.7+
- Flask
- Transformers library (Hugging Face)
- PyTorch

## Installation

1. **Clone or navigate to the project folder:**
   ```bash
   cd AI-TRANSLATOR-WEBAPP
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Access the web interface:**
   - Open your browser and navigate to `http://localhost:5000`

## Usage

1. Select your target language from the dropdown menu
2. Enter the English text you want to translate
3. Click the "Translate" button
4. View the translated result

## Models Used

The app uses the following pre-trained models from Hugging Face:
- **Chinese:** `Helsinki-NLP/opus-mt-en-zh` - English to Chinese Simplified
- **German:** `Helsinki-NLP/opus-mt-en-de` - English to German  
- **Hindi:** `Helsinki-NLP/opus-mt-en-hi` - English to Hindi

## Performance Notes

- **First Translation:** The first translation in each language may take longer (20-30 seconds) as the model is loaded from the Hugging Face server
- **Subsequent Translations:** Much faster as models are cached in memory
- **Maximum Length:** Up to 512 tokens per translation

## Project Structure

```
AI-TRANSLATOR-WEBAPP/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── static/
│   └── css/
│       └── style.css     # Styling
└── templates/
    └── index.html        # Web interface
```

## License

Open source - feel free to use and modify!

## Troubleshooting

**Issue:** Slow model loading on first run
- **Solution:** This is normal. The model files (~1-2GB) are downloaded from Hugging Face on first use.

**Issue:** CUDA out of memory error
- **Solution:** The app will automatically use CPU if GPU memory is insufficient.

**Issue:** Translation quality is poor
- **Solution:** These models work best with clear, grammatically correct English text.

## Future Enhancements

- Add more language pairs
- Support for batch translations
- API endpoint for programmatic access
- Dark mode theme
