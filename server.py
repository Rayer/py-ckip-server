from flask import Flask, jsonify, request
from MonpaWrapper import MonpaWrapper
import logging

app = Flask(__name__)
monpa = MonpaWrapper()

LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y%m%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)

logging.debug('Hello debug!')
logging.info('Hello info!')
logging.warning('Hello warning!')
logging.error('Hello error!')
logging.critical('Hello critical!')

@app.route('/', methods=["GET", "POST"])
def parse():
    if request.method == 'GET':
        return jsonify({'response': 'ok!(GET)'})
    payload = request.json
    if 'sentences' not in payload and 'sentence_with_keys' not in payload:
        return jsonify({'response': 'No sentences nor sentence_with_keys attribute are found!'})

    ws_list_1 = None
    ws_list_2 = None
    export_with_pos = True

    if 'export_with_pos' in payload:
        export_with_pos = payload['export_with_pos']

    if 'sentences' in payload:
        ws_list_1 = monpa.handle_sentences(payload['sentences'], export_with_pos=export_with_pos)

    if 'sentence_with_keys' in payload:
        ws_list_2 = monpa.handle_sentences_with_keys(payload['sentence_with_keys'], export_with_pos=export_with_pos)

    # Sentences with keys have higher property
    return jsonify({'response': ws_list_2 if ws_list_1 is None else ws_list_1})


@app.route('/health')
def healthCheck():
    return 'healthy!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
