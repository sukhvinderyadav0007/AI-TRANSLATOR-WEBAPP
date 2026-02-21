from flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__, template_folder='templates', static_folder='static')

# Dictionary to store models and tokenizers for different language pairs
models = {}
tokenizers = {}

# Model configurations for different language pairs
LANGUAGE_MODELS = {
    # Original languages
    'chinese': 'Helsinki-NLP/opus-mt-en-zh',
    'zh': 'Helsinki-NLP/opus-mt-en-zh',
    'german': 'Helsinki-NLP/opus-mt-en-de',
    'de': 'Helsinki-NLP/opus-mt-en-de',
    'hindi': 'Helsinki-NLP/opus-mt-en-hi',
    'hi': 'Helsinki-NLP/opus-mt-en-hi',
    'korean': 'Helsinki-NLP/opus-mt-en-ko',
    'ko': 'Helsinki-NLP/opus-mt-en-ko',
    'spanish': 'Helsinki-NLP/opus-mt-en-es',
    'es': 'Helsinki-NLP/opus-mt-en-es',
    'french': 'Helsinki-NLP/opus-mt-en-fr',
    'fr': 'Helsinki-NLP/opus-mt-en-fr',
    'japanese': 'Helsinki-NLP/opus-mt-en-ja',
    'ja': 'Helsinki-NLP/opus-mt-en-ja',
    'russian': 'Helsinki-NLP/opus-mt-en-ru',
    'ru': 'Helsinki-NLP/opus-mt-en-ru',
    'arabic': 'Helsinki-NLP/opus-mt-en-ar',
    'ar': 'Helsinki-NLP/opus-mt-en-ar',
    'portuguese': 'Helsinki-NLP/opus-mt-en-pt',
    'pt': 'Helsinki-NLP/opus-mt-en-pt',
    # Additional 10 languages
    'italian': 'Helsinki-NLP/opus-mt-en-it',
    'it': 'Helsinki-NLP/opus-mt-en-it',
    'turkish': 'Helsinki-NLP/opus-mt-en-tr',
    'tr': 'Helsinki-NLP/opus-mt-en-tr',
    'thai': 'Helsinki-NLP/opus-mt-en-th',
    'th': 'Helsinki-NLP/opus-mt-en-th',
    'vietnamese': 'Helsinki-NLP/opus-mt-en-vi',
    'vi': 'Helsinki-NLP/opus-mt-en-vi',
    'indonesian': 'Helsinki-NLP/opus-mt-en-id',
    'id': 'Helsinki-NLP/opus-mt-en-id',
    'polish': 'Helsinki-NLP/opus-mt-en-pl',
    'pl': 'Helsinki-NLP/opus-mt-en-pl',
    'dutch': 'Helsinki-NLP/opus-mt-en-nl',
    'nl': 'Helsinki-NLP/opus-mt-en-nl',
    'swedish': 'Helsinki-NLP/opus-mt-en-sv',
    'sv': 'Helsinki-NLP/opus-mt-en-sv',
    'greek': 'Helsinki-NLP/opus-mt-en-el',
    'el': 'Helsinki-NLP/opus-mt-en-el',
    'hungarian': 'Helsinki-NLP/opus-mt-en-hu',
    'hu': 'Helsinki-NLP/opus-mt-en-hu'
}

def load_model(language_code):
    """Load model and tokenizer for the specified language"""
    if language_code not in models:
        model_name = LANGUAGE_MODELS[language_code]
        tokenizers[language_code] = MarianTokenizer.from_pretrained(model_name)
        models[language_code] = MarianMTModel.from_pretrained(model_name)
    return models[language_code], tokenizers[language_code]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    selected_language = "hi"  # Default language (Hindi)
    
    if request.method == 'POST':
        text = request.form.get('data', '')
        selected_language = request.form.get('language', 'hi')
        
        if text and selected_language in LANGUAGE_MODELS:
            try:
                # Load appropriate model and tokenizer
                model, tokenizer = load_model(selected_language)
                
                # Tokenize and translate
                input_ids = tokenizer.encode(text, return_tensors="pt")
                outputs = model.generate(input_ids, max_length=512)
                result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            except Exception as e:
                result = f"Error: {str(e)}"
    
    return render_template('index.html', result=result, selected_language=selected_language)

if __name__ == '__main__':
    app.run()
