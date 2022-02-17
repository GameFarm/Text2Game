from concurrent.futures import thread
import socket
import threading

ip_host = '172.30.151.139'
port = 9008

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip주소, 포트번호 지정 server_socket.listen(0) # 클라이언트의 연결요청을 기다리는 상태 client_socket, addr = server_socket.accept() # 연결 요청을 수락함. 그러면 아이피주소, 포트등 데이터를 return data = client_socket.recv(65535) # 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨) print("받은 데이터:", data.decode())
server_socket.bind((ip_host, port))
# 클라이언트의 연결요청을 기다리는 상태 client_socket, addr = server_socket.accept() # 연결 요청을 수락함. 그러면 아이피주소, 포트등 데이터를 return data = client_socket.recv(65535)
server_socket.listen()

clients_list = []
clients_nicknames = []

# 클라이언트 메시지 방송부분


def broadcast(message):
    for client in clients_list:
        client.send(message)

# 클라이언트 메시지 및 클라이언트 관리


def handle(client):
    while True:
        try:
            message = client.recv(1024)  # 1024byte 내의 정보를 받는다
            broadcast(message)
        except:
            index = clients_list.index(client)  # error and terminate 클라이언트 지움
            clients_list.remove(message)
            client.close()
            nickname = clients_nicknames[index]
            broadcast(f'{nickname} 박멸됨!'.encode('utf-8'))
            nickname.remove(nickname)
            break

# 새 클라이언트 받기


def receive():
    while True:
        client, address = server_socket.accept()
        print(f"conncted with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients_nicknames.append(nickname)
        clients_list.append(client)

        print(f'Nick name for this client is {nickname}!')
        broadcast(f'{nickname}이 대화에 참여합니다~ '.encode('utf-8'))
        client.send('Connected to practice_server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print('server starts..')
receive()


# 연결 요청을 수락함. 그러면 아이피주소, 포트등 데이터를 return data = client_socket.recv(65535) # 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨) print("받은 데이터:", data.decode())
client_socket, addr = server_socket.accept()

# 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨)
data = client_socket.recv(65535)
print("받은 데이터:", data.decode())
