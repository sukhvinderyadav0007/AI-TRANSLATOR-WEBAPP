from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__, template_folder='../templates', static_folder='../static')
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    selected_language = "hi"
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        selected_language = request.form.get('language', 'hi')
        
        if text:
            try:
                translated = translator.translate(text, dest=selected_language)
                translated_text = translated.text
            except Exception as e:
                translated_text = f"Error: {str(e)}"
    
    return render_template('index.html', result=translated_text, selected_language=selected_language)

# IMPORTANT for Vercel
app = app

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

