import re
import os
import sys
import time
import socket
import select
import logging
sys.path.append("/home/koj3767/scenarioBasedModel")
from conversationEvaluator import ConversationEvaluator


# 데이터 전처리 함수
def preprocess_sentence(logger, sentence):
    logger.info("[ preprocess_sentence() ] 함수 진입")
    try:
        # list의 []는 공백처리
        sentence = re.sub(r'[" "]+', " ", sentence)
        # 문장 부호 이외 다른 특수문자 제거
        sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
        # 영문자, 한글, 숫자, 주요 특수문자 이외 모든 문자는 공백처리
        sentence = re.sub(r"[^a-zA-Zㄱ-ㅎ가-힣0-9?.!,]+", " ", sentence)
        # 단어 좌우 공백 제거
        sentence = sentence.strip()
    except Exception as e:
        logger.error("[ preprocess_sentence() ] "+str(e))

    return sentence



def server_print_test(client_socket):
    message = "[Server] 연결 확인용 "
    client_socket.send(message.encode('utf-8'))


def sentiment_model(logger, client_socket, model_evaluator, text):
    logger.info(str("[sentiment model] 함수 진입"))
    logger.debug("[sentiment model] 클라이언트 메세지 : "+ str(text))
    result = preprocess_sentence(logger, str(text)).split(',')
       
    predict = model_evaluator.predict_sentiment(result[0])
    logger.debug("[sentiment model] 모델 예측 결과 : "+ str(predict))
    
    message = "[sentiment]@" + str(list(predict))
    client_socket.send(message.encode('utf-8'))


def emotion_model(logger, client_socket, model_evaluator, text):
    logger.info("[emotion model] 함수 진입")
    logger.debug("[emotion model] 클라이언트 메세지 : "+ str(text))
    result = preprocess_sentence(logger, str(text)).split(',')
    
    predict = model_evaluator.predict_emotion(result[0])
    logger.debug("[emotion model] 모델 예측 결과 : "+ str(predict))
    
    message = "[emotion]@" + str(list(predict))
    client_socket.send(message.encode('utf-8'))


def context_model(logger, client_socket, model_evaluator, text):
    logger.info("[context model] 함수 진입")
    logger.debug("[context model] 클라이언트 메세지 : "+ str(text))
    result = preprocess_sentence(logger, str(text)).split(',')
    logger.debug("[context model] 데이터 전처리 결과 : "+ str(result))
        
    predict = model_evaluator.predict_context(result[0], result[1])
    logger.debug("[context model] 모델 예측 결과 : "+ str(predict))
    
    message = "[context]@" + str(predict)
    client_socket.send(message.encode('utf-8'))


def sts_model(logger, client_socket, model_evaluator, text):
    logger.info("[sts model] 함수 진입")
    logger.debug("[sts model] 클라이언트 메세지 : "+ str(text))
    result = preprocess_sentence(logger, str(text)).split(',')
    logger.debug("[sts model] 데이터 전처리 결과 : "+ str(result)) 
    
    predict = model_evaluator.predict_sts(result[0], result[1])
    logger.debug("[sts model] 모델 예측 결과 : "+ str(predict)) 
    
    message = "[sts]@" + str(predict)
    client_socket.send(message.encode('utf-8'))
    
    
def record_to_log(content):   #디버깅용 로그파일에 기록하기 위한 함수
    log_file_addr = "log.txt"
    content_log = [content, '\n']
    content_log = "".join(content_log)
    with open(log_file_addr, 'a') as log_data:
        log_data.write(content_log)


def server_start():
    host = 'ip-172-31-23-109.us-east-3.compute.internal'   #curl ifconfig.me 를 이용하여 외부ip를 알 수 있다고한다.
    port = 8000
    
    logger = logging.getLogger("Zil_M")
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler('GameFarm Server.log')
    logger.addHandler(file_handler)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    client_socket = None
    model_evaluator = ConversationEvaluator()
    logger.info("[System] Server Run")

    while True:
        if client_socket is None:
            logger.info("[System] Client socket 객체가 없는 분기점 호출")
            client_socket, client_address = server_socket.accept()
            logger.info("[System] Client connected")
            logger.debug("[System] Client socket object : " + str(client_socket))
            logger.debug("[System] Client socket address : " + str(client_address))
            msg = str(client_address) + " 접속"
            client_socket.sendall(msg.encode())
        elif client_socket is not None:
            # Client 에서 메세지 발신 했을때 활성화
            try:
                message = client_socket.recv(1024).decode('utf-8')
            except Exception as e:
                logger.error("[System][non client scoket] : "+str(e))
                logger.info("[System] Client socket과 연결 해제")
                client_socket.close()
                logger.info("[System] Client socket 메모리 값 초기화")
                client_socket = None
                client_address = None

            # 받은 데이터가 없으면 loop 다시 진행
            if not message:
                continue

            pre_msg = message.split(',')
            logger.debug("[System] Client Message : " + str(message))

            if pre_msg[0] == "sentiment":
                logger.info("[System] Sentiment model 함수 호출")               
                sentiment_model(logger, client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "emotion":
                logger.info("[System] Emotion model 함수 호출") 
                emotion_model(logger, client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "context":
                logger.info("[System] Context model 함수 호출") 
                context_model(logger ,client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "question":
                logger.info("[System] Sts model 함수 호출") 
                sts_model(logger, client_socket, model_evaluator, pre_msg[1:])
            elif pre_msg[0] == "client_close":
                msg = '[Client connect exit][OK] client_close'
                client_socket.send(msg.encode('utf-8'))
                logger.info("[System] Disconnect the client")
                client_socket.close()
                client_socket = None
                client_address = None
                #time.sleep(0.5)
            
            logger.info("[System] Server Pause 0.5 sec")
            time.sleep(0.5)
                
    logger.info("[System] Server Exit")
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    server_start()
