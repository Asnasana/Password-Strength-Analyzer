from flask import Flask, render_template, request, jsonify
from password_analyzer import PasswordAnalyzer, WordlistGenerator

app = Flask(__name__)
analyzer = PasswordAnalyzer()
generator = WordlistGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.form.get('password', '')
    if not password:
        return jsonify({'error': 'Password is required'}), 400

    analysis = analyzer.analyze_strength(password)
    return jsonify(analysis)

@app.route('/generate', methods=['POST'])
def generate():
    base_words = request.form.get('base_words', '').split(',')
    base_words = [word.strip() for word in base_words if word.strip()]
    rules = request.form.getlist('rules')

    if not base_words:
        return jsonify({'error': 'At least one base word is required'}), 400

    wordlist = generator.generate_wordlist(base_words, rules)
    return jsonify({'wordlist': wordlist[:100], 'total': len(wordlist)})  # Limit to 100 for display

if __name__ == '__main__':
    app.run(debug=True)
