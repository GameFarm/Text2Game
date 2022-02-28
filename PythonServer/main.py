import re
import os
import sys
import time
import socket
import select
import logging
sys.path.append("/home/koj3767/scenarioBasedModel")
from conversationEvaluator import ConversationEvaluator

# from model_test import SentimentEvaluatoir


# [ 테스트 항목 ]
# 1. 클라이언트가 정상적으로 종료되는가?
# 2. 클라이언트가 서버와 재 연결 시도시 정상적으로 연결되는가?
# 3. 클라이언트가 32byte를 초과하는 데이터 송수신시 발생하는 오류 확인
# 4. 모델 정상 작동 여부 확인
# 5. 클라이언트가 보낸 데이터가 String이 아닐때 서버에서 정상작동 여부
#   5.1  예외처리
#   5.2  if 문으로 string 값인지 확인후, 아니면 return, 129줄 이후 else 를 추가하여 처리하면 좋을 듯 합니다.

# [잠재적버그] 
# time.sleep 사용시 비동기화 방식으로 확장했을 때 시퀀스가 꼬이는 상황이 발생할 수 있다.




# 데이터 전처리 함수
def preprocess_sentence(sentence):
    # list의 []는 공백처리
    sentence = re.sub(r'[" "]+', " ", sentence)
    # 문장 부호 이외 다른 특수문자 제거
    sentence = re.sub(r"([?.!,])", r" \1 ", sentence)   
    # 영문자, 한글, 숫자, 주요 특수문자 이외 모든 문자는 공백처리
    sentence = re.sub(r"[^a-zA-Zㄱ-ㅎ가-힣0-9?.!,]+", " ", sentence)   
    # 단어 좌우 공백 제거
    sentence = sentence.strip()

    return sentence



def server_print_test(client_socket):
    message = "[Server] 연결 확인용 "
    client_socket.send(message.encode('utf-8'))
    time.sleep(5)


def sentiment_model(client_socket, model_evaluator, text):
    print('[server][sentiment model] 클라이언트 메세지 : ', text)
    predict = model_evaluator.predict_sentiment(text)
    print('[server][sentiment] 결과 : ', predict)
    
    message = "[sentiment]@" + str(list(predict))
    client_socket.send(message.encode('utf-8'))
    time.sleep(1)


def emotion_model(client_socket, model_evaluator, text):
    print('[server][emotion model] 클라이언트 메세지 : ', text)
    predict = model_evaluator.predict_emotion(text)
    print('[emotion] 결과 : ', predict)
    
    message = "[emotion]@" + str(list(predict))
    client_socket.send(message.encode('utf-8'))
    time.sleep(1)


def context_model(client_socket, model_evaluator, text):
    print('[server][context model] 클라이언트 메세지 : ', text)
    result = preprocess_sentence(str(text)).split(',')
    print('[server][test] 분할 결과 : ',result)
        
    predict = model_evaluator.predict_context(result[0], result[1])
    print('[context] 결과 : ', predict)
    
    message = "[context]@" + str(predict)
    client_socket.send(message.encode('utf-8'))
    time.sleep(1)


def question_model(client_socket, model_evaluator, text):
    predict = model_evaluator.predict_sts(text)
    print('[sentiment] 결과 : ', predict)
    
    message = "[sentiment]@" + str(list(predict))
    client_socket.send(message.encode('utf-8'))
    time.sleep(1)


def server_start():
    host = '10.128.0.4'   #curl ifconfig.me 를 이용하여 외부ip를 알 수 있다고한다.
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    client_socket = None
    model_evaluator = ConversationEvaluator()# model create

    while True:
        if client_socket is None:
            client_socket, client_address = server_socket.accept()
            print('[연결] ', client_address)
            msg = str(client_address) + " 접속"
            client_socket.sendall(msg.encode())
        elif client_socket is not None:
            # Client 에서 메세지 발신 했을때 활성화
            try:
                message = client_socket.recv(128).decode('utf-8')
                client_socket.send("서버 인지".encode('utf-8'))
            except:
                print('[Except] client_abnormal_close')
                client_socket.close()
                client_socket = None
                client_address = None

            # 받은 데이터가 없으면 loop진행
            if not message:
                continue

            pre_msg = message.split(',')
            print("[Client msg] ", message)

            if pre_msg[0] == "sentiment":
                sentiment_model(client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "emotion":
                emotion_model(client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "context":
                context_model(client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "question":
                question_model(client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "client_close":
                msg = '[Client connect exit][OK] client_close'
                client_socket.send(msg.encode('utf-8'))
                print('[Server System] ', msg)
                time.sleep(0.5)
                client_socket.close()
                client_socket = None
                client_address = None

            time.sleep(1)

            # server_print_test(client_socket)

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    server_start()
