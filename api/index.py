from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__, template_folder='../templates', static_folder='../static')
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        target_lang = request.form["language"]

        translated = translator.translate(text, src="en", dest=target_lang)
        translated_text = translated.text

    return render_template("index.html", result=translated_text)

if __name__ == "__main__":
    app.run()

