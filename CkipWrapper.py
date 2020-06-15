import os

from ckiptagger import data_utils, WS, POS, NER
from Engine import Engine


class CkipEngine(Engine):

    def __init__(self, dict_path):
        # If data not found, download file
        if not os.path.exists(dict_path + "/data.zip") and not os.path.exists("/data"):
            print("no dictionary data detected, downloading....")
            data_utils.download_data(dict_path)
        self.ws = WS(dict_path + "/data")
        self.pos = POS(dict_path + "/data")
        self.ner = NER(dict_path + "/data")

    def handle_sentences_impl(self, sentences: [], filter_pos_symbols: bool = True, export_with_pos: bool = True):
        word_sentence_list = self.ws(sentences)
        pos_sentence_list = None
        ret = []
        if filter_pos_symbols or export_with_pos:
            pos_sentence_list = self.pos(sentences)


        # Process per sentence
        for sentence_index in range(0, len(word_sentence_list)):
            filtered_word_list = []
            filtered_pos_list = []
            if pos_sentence_list[sentence_index] is not None:
                pos_list = pos_sentence_list[sentence_index]
                word_list = word_sentence_list[sentence_index]
                for word, pos in zip(word_list, pos_list):
                    if pos not in self.get_filter_pos_symbols():
                        filtered_word_list.append(word)
                        filtered_pos_list.append(pos)
            word_sentence_list[sentence_index] = filtered_word_list
            pos_sentence_list[sentence_index] = filtered_pos_list
            if export_with_pos:
                for index in range(0, len(filtered_word_list)):
                    ret.append([filtered_word_list[index], filtered_pos_list[index]])
            else:
                ret.append(filtered_word_list)

        return ret
