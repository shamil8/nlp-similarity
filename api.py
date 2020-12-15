from flask import Flask, request, jsonify
from nlp_py.similarity import get_similarity
from nlp_py.main import get_similarity_stat
app = Flask(__name__)


arr_trust = ['true', '1', 't', 'y', 'yes']

@app.route('/')
def index():
    return 'Welcome to Python :O)'


@app.route('/nlp-words')
def nlp_words():
    args = request.args
    if args and args.get('text'):
        append = args.get('is-append')
        is_append = False

        if append and append in arr_trust: is_append = True

        return jsonify(get_similarity(args.get('text'), is_append))

    return 'You need to add `text` param'

@app.route('/nlp-computing')
def nlp_computing():
    args = request.args
    if args and args.get('text'):
        append = args.get('is-append')
        is_append = False

        if append and append in arr_trust: is_append = True

        return jsonify(get_similarity_stat(args.get('text'), is_append))

    return 'You need to add `text` param'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')