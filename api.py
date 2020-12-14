from flask import Flask, request, jsonify
from main import get_similarity
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Python :O)'


@app.route('/nlp-words')
def nlp_words():
    args = request.args
    if args and args.get('text'):
        return jsonify(get_similarity(args.get('text')))

    return 'false'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')