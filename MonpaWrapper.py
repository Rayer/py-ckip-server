import monpa


class MonpaWrapper:
    def __init__(self):
        pass

    def get_filter_pos_symbols(self):
        return ["COMMACATEGORY", "DASHCATEGORY", "ETCCATEGORY", "EXCLAMATIONCATEGORY", "PARENTHESISCATEGORY",
                "PAUSECATEGORY", "PERIODCATEGORY", "QUESTIONCATEGORY", "SEMICOLONCATEGORY", "SPCHANGECATEGORY",
                "DE", "SHI", "COLONCATEGORY", "Cbb", "Caa", "Cab", "Cba", "Nh", "Nf"]

    def handle_sentences(self, sentences, filter_pos_symbols=True):
        ret = []
        for s in sentences:
            ret += self.handle_single_sentence(filter_pos_symbols, s)
        return ret

    def handle_sentences_with_keys(self, payload, filter_pos_symbols=True):
        ret = []
        for rec in payload:
            ret.append({'key': rec['key'], 'result': self.handle_single_sentence(filter_pos_symbols, rec['sentence'])})
        return ret
    
    def handle_single_sentence(self, filter_pos_symbols, s):
        section = monpa.pseg(s)
        analyzed = []
        for (w, p) in section:
            if not filter_pos_symbols or p not in self.get_filter_pos_symbols():
                analyzed.append((w, p))
        return analyzed
