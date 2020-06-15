import logging
import abc
from collections import OrderedDict


class Engine(metaclass=abc.ABCMeta):

    @staticmethod
    def get_filter_pos_symbols():
        return ["COMMACATEGORY", "DASHCATEGORY", "ETCCATEGORY", "EXCLAMATIONCATEGORY", "PARENTHESISCATEGORY",
                "PAUSECATEGORY", "PERIODCATEGORY", "QUESTIONCATEGORY", "SEMICOLONCATEGORY", "SPCHANGECATEGORY",
                "DE", "SHI", "COLONCATEGORY", "Cbb", "Caa", "Cab", "Cba", "Nh", "Nf"]

    def handle_sentences(self, sentences: [], filter_pos_symbols: bool = True, export_with_pos: bool = True):
        return self.handle_sentences_impl(sentences, filter_pos_symbols, export_with_pos)

    @abc.abstractmethod
    def handle_sentences_impl(self, sentences: [], filter_pos_symbols: bool = True, export_with_pos: bool = True):
        return NotImplemented

    def handle_sentences_with_keys(self, payload, filter_pos_symbols=True, export_with_pos=True):
        ret = []
        input_sentences = []
        for p in payload:
            input_sentences.append(p["sentence"])

        result = self.handle_sentences(input_sentences, filter_pos_symbols, export_with_pos)
        for index in range(0, len(payload)):
            ret.append({'key': payload[index]['key'], 'result': result[index]})

        return ret
