from flask import Flask, request, jsonify
from flask_cors import CORS
from connector.tasks_to_csv import upgrade_tasks
from nlp_py.similarity import get_similarity
from nlp_py.main import get_similarity_date

app = Flask(__name__)
cors = CORS(app)

text_param_error = 'Bad request! (you need to add `text` param)'
param_error_code = 400


@app.route('/')
def index():
    return 'Welcome to Python :O)'


@app.route('/upgrade-tasks')
def update_tasks():
    upgrade_tasks()
    return 'Updated tasks!'


@app.route('/nlp-words')
def nlp_words():
    args = request.args
    if args and args.get('text'):
        append = args.get('is-append')
        is_append = False

        if append and append in ['true', '1', 't', 'y', 'yes']:
            is_append = True

        response = jsonify(get_similarity(args.get('text'), is_append))
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    return text_param_error, param_error_code


@app.route('/nlp-computing')
def nlp_date_computing():
    args = request.args

    return jsonify(get_similarity_date(args.get('text'), args.get('owner_id'))) if args and args.get('text') \
        else (text_param_error, param_error_code)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
# if you work with this docker-compose file you need to set port=5001 !!!
