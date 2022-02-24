import socket
import time
from model_test import SentimentEvaluator


def server_print_test(client_socket):
    message = "[Server] 연결 확인용 "
    client_socket.send(message.encode('utf-8'))
    time.sleep(5)


def sentiment_model(client_socket, text):
    # sentiment_evaluator = SentimentEvaluator()
    # predict = sentiment_evaluator.evaluate_sentiment(text)
    # print('[sentiment] 결과 : ', predict)
    # message = "[sentiment]" + str(list(predict[0]))

    client_socket.send(text.encode('utf-8'))
    time.sleep(1)


def emotion_model(client_socket, text):
    # emotion_evaluator = SentimentEvaluator()
    # predict = emotion_evaluator.evaluate_sentiment(text)
    # print('[sentiment] 결과 : ', predict)
    # message = "[sentiment]" + str(list(predict[0]))

    client_socket.send(text.encode('utf-8'))
    time.sleep(1)


def context_model(client_socket, text):
    # emotion_evaluator = SentimentEvaluator()
    # predict = emotion_evaluator.evaluate_sentiment(text)
    # print('[sentiment] 결과 : ', predict)
    # message = "[sentiment]" + str(list(predict[0]))

    client_socket.send(text.encode('utf-8'))
    time.sleep(2)


def question_model(client_socket, text):
    # emotion_evaluator = SentimentEvaluator()
    # predict = emotion_evaluator.evaluate_sentiment(text)
    # print('[sentiment] 결과 : ', predict)
    # message = "[sentiment]" + str(list(predict[0]))

    client_socket.send(text.encode('utf-8'))
    time.sleep(2)


def server_start():
    host = '10.128.0.4'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    client_socket = None

    while True:

        if client_socket is None:
            client_socket, client_address = server_socket.accept()
            print('[연결] ', client_address)
            msg = str(client_address) + " 접속"
            client_socket.sendall(msg.encode())
        elif client_socket is not None:
            # Client 에서 메세지 발신 했을때 활성화
            try:
                message = client_socket.recv(32).decode('utf-8')
                client_socket.send("server received".encode('utf-8'))

            except Exception as e:
                print("scene changed")
                client_socket.close()
                client_socket = None
                client_address = None

            # 받은 데이터가 없으면 loop진행
            if not message:
                continue

            pre_msg = message.split(',')
            print("[Client msg] ", message)

            if pre_msg[0] == "sentiment":
                sentiment_model(client_socket, pre_msg[1])
            elif pre_msg[0] == "emotion":
                emotion_model(client_socket, pre_msg[1])
            elif pre_msg[0] == "context":
                context_model(client_socket, pre_msg[1])
            elif pre_msg[0] == "question":
                question_model(client_socket, pre_msg[1])

            time.sleep(1)

            # server_print_test(client_socket)

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    server_start()
