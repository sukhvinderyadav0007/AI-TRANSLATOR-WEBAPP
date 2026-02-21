from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Simple translation dictionary for common phrases
TRANSLATIONS = {
    "hello": {"hi": "नमस्ते", "ko": "안녕하세요", "de": "Hallo", "es": "Hola", "fr": "Bonjour", "ja": "こんにちは", "ru": "Привет", "ar": "مرحبا", "pt-BR": "Olá", "zh-CN": "你好"},
    "welcome": {"hi": "स्वागत है", "ko": "환영합니다", "de": "Willkommen", "es": "Bienvenido", "fr": "Bienvenue", "ja": "ようこそ", "ru": "Добро пожаловать", "ar": "أهلا وسهلا", "pt-BR": "Bem-vindo", "zh-CN": "欢迎"},
    "thank you": {"hi": "धन्यवाद", "ko": "감사합니다", "de": "Danke", "es": "Gracias", "fr": "Merci", "ja": "ありがとう", "ru": "Спасибо", "ar": "شكراً", "pt-BR": "Obrigado", "zh-CN": "谢谢"},
    "good morning": {"hi": "सुप्रभात", "ko": "좋은 아침", "de": "Guten Morgen", "es": "Buenos días", "fr": "Bonjour", "ja": "おはよう", "ru": "Доброе утро", "ar": "صباح الخير", "pt-BR": "Bom dia", "zh-CN": "早上好"},
    "how are you": {"hi": "आप कैसे हैं", "ko": "어떻게 지내세요", "de": "Wie geht es dir", "es": "¿Cómo estás?", "fr": "Comment allez-vous", "ja": "お元気ですか", "ru": "Как ты", "ar": "كيف حالك", "pt-BR": "Como você está", "zh-CN": "你好吗"},
}

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text", "").lower().strip()
        target_lang = request.form.get("language", "hi")

        # Check if we have a translation in our dictionary
        if text in TRANSLATIONS:
            translated_text = TRANSLATIONS[text].get(target_lang, f"Translation not available for '{text}'")
        else:
            translated_text = f"Try: hello, welcome, thank you, good morning, how are you"

    return render_template("index.html", result=translated_text)

if __name__ == "__main__":
    app.run()

