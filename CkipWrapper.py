import os

from ckiptagger import data_utils, WS


class CkipWrapper:
    def __init__(self, dict_path):
        # If data not found, download file
        if not os.path.exists(dict_path + "/data.zip") and not os.path.exists("/data"):
            print("no dictionary data detected, downloading....")
            data_utils.download_data(dict_path)
        self.ws = WS(dict_path + "/data")

    def handle_sentences(self, sentences):
        word_sentence_list = self.ws(sentences)
        return word_sentence_list

    @staticmethod
    def print_word_pos_sentence(word_sentence, pos_sentence):
        assert len(word_sentence) == len(pos_sentence)
        for word, pos in zip(word_sentence, pos_sentence):
            print(f"{word}({pos})", end="\u3000")
        print()
        return


