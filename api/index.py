from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='../templates', static_folder='../static')

def translate_text(text, target_lang):
    """Translate text using MyMemory Translation API (free, no API key required)"""
    try:
        url = "https://api.mymemory.translated.net/get"
        params = {
            'q': text,
            'langpair': f'en|{target_lang}'
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'responseData' in data:
                return data['responseData']['translatedText']
        return "Translation failed"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    selected_language = "hi"
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        selected_language = request.form.get('language', 'hi')
        
        if text:
            translated_text = translate_text(text, selected_language)
    
    return render_template('index.html', result=translated_text, selected_language=selected_language)

# IMPORTANT for Vercel
app = app

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

