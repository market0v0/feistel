from flask import Flask, render_template, request
from Feistel import *

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    key = ''
    rounds = 1
    hashed = ''
    error = None
    
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        rounds = int(request.form['rounds'])
        if not all(c in '0123456789abcdef' for c in text) or len(text) > 4:
            error = "Error: Text must be a valid hexadecimal value with at most 4 characters."
        elif not all(c in '0123456789abcdef' for c in key) or len(key) > 4:
            error = "Error: Key must be a valid hexadecimal value with at most 4 characters."
        else:
            hashed = roundsDES(text, key, rounds)

    return render_template('index.html', hashed=hashed, error=error, steps=proccess, length=rounds)

if __name__ == '__main__':
    app.run(debug=True)
