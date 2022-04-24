import re
import numpy as np
from transformers import BertTokenizer, TFBertForSequenceClassification


class ConversationEvaluator:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('../scenarioBasedModel/model/tokenizer')
        
        self.context = TFBertForSequenceClassification.from_pretrained('../scenarioBasedModel/model/context model')
        self.sentiment = TFBertForSequenceClassification.from_pretrained('../scenarioBasedModel/model/sentiment model')
        self.emotion = TFBertForSequenceClassification.from_pretrained('../scenarioBasedModel/model/emotion model')
        self.sts = TFBertForSequenceClassification.from_pretrained('../scenarioBasedModel/model/sts model')
    
    def filt_str(self, text: str):
        #processing sentence
        text = text.lower()
        text = re.sub(r"[ㅇ]+", "응", text)
        text = re.sub(r"[ㄴ]+", "노", text)
        text = re.sub(r"[^가-힣a-z.,!?<>;\']", " ", text)
        text = re.sub(r'[" "]+', " ", text)
        return text
    
    def sentence2token(self, text1: str, text2: str=None):
        #convert sentence to token
        token = self.tokenizer(
            *tuple((text1, text2)),
            return_tensors='tf',
            pad_to_max_length=True,
            max_length=128
        )
        return token
    
    def cal_softmax(self, x):
        #get_softmax value
        softmax_x = np.exp(x - np.max(x))
        return (softmax_x / softmax_x.sum()).round(3)
    
    def predict_context(self, script: str, user_input: str):
        script = self.filt_str(script)
        user_input = self.filt_str(user_input)
        
        input_tensor = self.sentence2token(script, user_input)
        
        predict = self.context(input_tensor)
        predict = predict.logits.numpy()
        predict = list(self.cal_softmax(predict))
        #  predict = self.cal_softmax(predict).tolist()
        predict = predict[0][1]
        return predict
    
    def predict_sentiment(self, user_input: str):
        user_input = self.filt_str(user_input)
        
        input_tensor = self.sentence2token(user_input, None)
        
        predict = self.sentiment(input_tensor)
        predict = predict.logits.numpy()
        predict = list(self.cal_softmax(predict))
        # predict = self.cal_softmax(predict).tolist()
        predict = predict[0]
        return predict
    
    def predict_emotion(self, user_input: str):
        user_input = self.filt_str(user_input)
        
        input_tensor = self.sentence2token(user_input, None)
        
        predict = self.emotion(input_tensor)
        predict = predict.logits.numpy()
        predict = list(self.cal_softmax(predict))
        # predict = self.cal_softmax(predict).tolist()
        predict = predict[0]
        return predict
    
    def predict_sts(self, script: str, user_input: str):
        script = self.filt_str(script)
        user_input = self.filt_str(user_input)

        input_tensor = self.sentence2token(script, user_input)

        predict = self.sts(input_tensor)
        predict = predict.logits.numpy()
        predict = self.cal_softmax(predict).tolist()
        predict = predict[0][1]
        return predict
