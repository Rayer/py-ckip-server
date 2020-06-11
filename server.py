from flask import Flask, jsonify, request
from CkipWrapper import CkipWrapper
from MonpaWrapper import MonpaWrapper

app = Flask(__name__)
# ckip = CkipWrapper("/tmp")
monpa = MonpaWrapper()

@app.route('/', methods=["GET", "POST"])
def parse():
    if request.method == 'GET':
        return jsonify({'response': 'ok!(GET)'})
    payload = request.json
    if 'sentences' not in payload and 'sentence_with_keys' not in payload:
        return jsonify({'response': 'No sentences nor sentence_with_keys attribute are found!'})

    ws_list_1 = None
    ws_list_2 = None
    if 'sentences' in payload:
        ws_list_1 = monpa.handle_sentences(payload['sentences'])

    if 'sentence_with_keys' in payload:
        ws_list_2 = monpa.handle_sentences_with_keys(payload['sentence_with_keys'])

    # Sentences with keys have higher property
    return jsonify({'response': ws_list_2 if ws_list_1 is None else ws_list_1})

@app.route('/health')
def healthCheck():
    return 'healthy!'

if __name__ == '__main__':
    app.run(port=9000)
