import torch
import numpy as np
from transformers import BertTokenizer, BertForNextSentencePrediction

class ContextEvaluator:
    def __init__(self, nsp_limit):
        self.nsp_limit = nsp_limit
        self.tokenizer = BertTokenizer.from_pretrained('klue/bert-base')
        self.model = BertForNextSentencePrediction.from_pretrained('klue/bert-base')

    def evaluate_context(self, text1, text2):
        #0: IsNSP, 1: NotNSP

        def cal_softmax(x):
            #get_softmax value
            softmax_x = np.exp(x - np.max(x))
            return softmax_x / softmax_x.sum()

        input_tensor = self.tokenizer(text1, text2, return_tensors='pt')
        predict = self.model(**input_tensor)
        predict = predict.logits.detach().numpy()[0]   #tensor2numpy

        softmax = cal_softmax(predict)
        return softmax[0]   #softmax[0] == IsNSP probability
