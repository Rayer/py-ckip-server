import monpa


class MonpaWrapper:
    def __init__(self):
        pass

    def handle_sentences(self, sentences):
        ret = []
        for s in sentences:
            ret += monpa.cut(s)
        return ret
