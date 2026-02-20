from flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__, template_folder='templates', static_folder='static')

# Load Marian tokenizer and model
model_name = "helsinki-nlp/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form.get('data', '')
        if text:
            # Tokenize and translate
            input_ids = tokenizer.encode(text, return_tensors="pt")
            outputs = model.generate(input_ids, max_length=512)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
