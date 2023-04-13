from flask import Flask, render_template, request
import translate
app = Flask(__name__)
translator = translate.Translator(to_lang='en', from_lang='fr')
@app.route('/', methods=['GET', 'POST'])
def uppercase():
    if request.method == 'POST':
        text = request.form['text']
        translation = translator.translate(text)
        return translation
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
