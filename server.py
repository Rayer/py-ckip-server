from flask import Flask, jsonify, request
from CkipWrapper import CkipWrapper

app = Flask(__name__)
ckip = CkipWrapper("/tmp")


@app.route('/', methods=["GET", "POST"])
def parse():
    if request.method == 'GET':
        return jsonify({'response': 'ok!(GET)'})
    payload = request.json
    if 'sentences' not in payload and 'sentences_with_keys':
        return jsonify({'response': 'No sentences nor sentence_with_keys attribute are found!'})

    ws_list = ckip.handle_sentences(payload['sentences'])

    return jsonify({'response': ws_list})

@app.route('/health')
def healthCheck():
    return 'healthy!'

if __name__ == '__main__':
    app.run(port=9000)
