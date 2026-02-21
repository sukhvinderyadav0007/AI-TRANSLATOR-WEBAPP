from flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__, template_folder='templates', static_folder='static')

# Dictionary to store models and tokenizers for different language pairs
models = {}
tokenizers = {}

# Model configurations for Hindi, Korean, and French
LANGUAGE_MODELS = {
    'hi': 'Helsinki-NLP/opus-mt-en-hi',    # Hindi
    'ko': 'Helsinki-NLP/opus-mt-en-ko',    # Korean
    'fr': 'Helsinki-NLP/opus-mt-en-fr',    # French
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
        text = request.form.get('text', '')
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
    print("🚀 Starting Flask Application...")
    print("📝 Models supported: Hindi, Korean, French")
    app.run(debug=True, host='127.0.0.1', port=5000)
