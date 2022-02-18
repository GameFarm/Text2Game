import socket
import threading

from sqlalchemy import null

nickname = input("대화방에서 이용 할 별명을 입력해주세요: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_host = '127.0.0.1'  # change it to server ip
port = 9008

client_socket.connect((ip_host, port))


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICK':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            if client_socket is null:
                print('error!! shutting off 꺼집니다.')
            else:
                print("client 정상 종료됩니다.")
                client_socket.close()
            break


def write():
    while True:
        message = f'{nickname}: {input(">")}'
        client_socket.send(message.encode('utf-8'))
        if message == f'{nickname}: /quit':
            close_client()
            break


def close_client():
    print('클라이언트 종료')
    client_socket.shutdown(socket.SHUT_RDWR)
    client_socket.close()


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
