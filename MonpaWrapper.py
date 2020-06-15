import monpa
import logging
from Engine import Engine


class MonpaWrapper(Engine):
    def __init__(self):
        pass

    def handle_sentences_impl(self, sentences, filter_pos_symbols, export_with_pos):
        ret = []
        for s in sentences:
            logging.info("Processing : " + s)
            section = monpa.pseg(s)
            analyzed = []
            for (w, p) in section:
                if not filter_pos_symbols or p not in self.get_filter_pos_symbols():
                    if export_with_pos:
                        analyzed.append((w, p))
                    else:
                        analyzed.append(w)
            ret.append(analyzed)

        return ret

