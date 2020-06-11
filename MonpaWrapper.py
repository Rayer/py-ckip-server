import monpa


class MonpaWrapper:
    def __init__(self):
        pass

    def handle_sentences(self, sentences):
        ret = []
        for s in sentences:
            ret.append(monpa.cut(s))
        return ret

    def handle_sentences_with_keys(self, payload):
        ret = []
        for rec in payload:
            ret.append({'key': rec['key'], 'result': monpa.cut(rec['sentence'])})
        return ret
