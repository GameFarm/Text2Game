import socket
import threading

nickname = input("대화방에서 이용 할 별명을 입력해주세요: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_host = '172.30.151.139'
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
            print("error!! shutting off")
            client_socket.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client_socket.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


client_socket.send('Hello'.encode())
