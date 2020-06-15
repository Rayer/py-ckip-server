import logging


class Engine:

    @staticmethod
    def get_filter_pos_symbols():
        return ["COMMACATEGORY", "DASHCATEGORY", "ETCCATEGORY", "EXCLAMATIONCATEGORY", "PARENTHESISCATEGORY",
                "PAUSECATEGORY", "PERIODCATEGORY", "QUESTIONCATEGORY", "SEMICOLONCATEGORY", "SPCHANGECATEGORY",
                "DE", "SHI", "COLONCATEGORY", "Cbb", "Caa", "Cab", "Cba", "Nh", "Nf"]

    def handle_sentences(self, sentences: [], filter_pos_symbols: bool = True, export_with_pos: bool = True):
        ret = []
        for s in sentences:
            ret += self.handle_single_sentence(s, filter_pos_symbols, export_with_pos)
        return ret

    def handle_sentences_with_keys(self, payload, filter_pos_symbols=True, export_with_pos=True):
        ret = []
        for rec in payload:
            ret.append({'key': rec['key'],
                        'result': self.handle_single_sentence(rec['sentence'], filter_pos_symbols, export_with_pos)})
        return ret

    def handle_single_sentence(self, s, filter_pos_symbols, export_with_pos):
        logging.info("Processing : " + s)
        section = monpa.pseg(s)
        analyzed = []
        for (w, p) in section:
            if not filter_pos_symbols or p not in self.get_filter_pos_symbols():
                if export_with_pos:
                    analyzed.append((w, p))
                else:
                    analyzed.append(w)
        return analyzed
