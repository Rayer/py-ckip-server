import os, json, sys
from ckiptagger import data_utils, NER, WS, POS, construct_dictionary


class CkipWrapper:
    def __init__(self, dict_path):
        # If data not found, download file
        if not os.path.exists(dict_path + "/data.zip") and not os.path.exists("/data"):
            print("no dictionary data detected, downloading....")
            data_utils.download_data(dict_path)
        self.ws = WS(dict_path + "/data")
        # self.pos = POS(dict_path + "/data")
        # self.ner = NER(dict_path + "/data")

    def handle_sentences(self, sentences):
        word_sentence_list = self.ws(sentences)
        return word_sentence_list
        # pos_sentence_list = self.pos(sentences)
        # entity_sentence_list = self.ner(word_sentence_list, pos_sentence_list)

        # for i, sentence in enumerate(sentences):
        #     print()
        #     print(f"'{sentence}'")
        #     self.print_word_pos_sentence(word_sentence_list[i], pos_sentence_list[i])
        #     for entity in sorted(entity_sentence_list[i]):
        #         print(entity)
        # return

        # Show results
    @staticmethod
    def print_word_pos_sentence(word_sentence, pos_sentence):
        assert len(word_sentence) == len(pos_sentence)
        for word, pos in zip(word_sentence, pos_sentence):
            print(f"{word}({pos})", end="\u3000")
        print()
        return



