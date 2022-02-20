from concurrent.futures import thread
import socket
import threading


ip_host = '127.0.0.1'
port = 9008

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

# 서버 메시지


def announce():
    while True:
        message = f'server : {input(">")}'
        broadcast(message.encode('utf-8'))
        print(message)
        if message == f'server : /quit':
            broadcast('server 종료'.encode('utf-8'))
            print('server 종료 개시')
            close_server()
            break


def close_server():
    # broadcast('server 종료'.encode('utf-8'))
    server_socket.shutdown(socket.SHUT_RDWR)
    for client in clients_list:
        client.close()
    clients_list.clear()
    clients_nicknames.clear()
    # print(f'잔여 클라 {len(clients_list)}')
    server_socket.close()
    # print(server_socket.fileno())
    print('server closed - 서버 종료')

# 클라이언트 메시지 및 클라이언트 관리


def handle(client):
    while True:
        try:
            message = client.recv(1024)  # 1024byte 내의 정보를 받는다
            print('a')  # 없으면 나갈 시 나감 메시지가 다음 차례에 나온다. 이유 모름.
            broadcast(message)
        except:  # error and terminate 클라이언트 지움
            index = clients_list.index(client)
            clients_list.remove(client)
            client.close()
            nickname = clients_nicknames[index]
            broadcast(f'{nickname} 나감!'.encode('utf-8'))
            print(f'{nickname} 나감!')
            clients_nicknames.remove(nickname)
            break

# 새 클라이언트 받기


def receive():
    while True:
        try:
            client, address = server_socket.accept()
            print(f"conncted with {str(address)}")

            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            clients_nicknames.append(nickname)
            clients_list.append(client)

            print(f'Nick name for this client is {nickname}!')
            broadcast(f'{nickname}이 대화에 참여합니다~ '.encode('utf-8'))
            client.send('Connected to practice_server'.encode('utf-8'))
            handle_thread = threading.Thread(target=handle, args=(client,))
            handle_thread.daemon = True
            handle_thread.start()

            announce_thread = threading.Thread(target=announce)
            announce_thread.daemon = True
            announce_thread.start()

        except Exception as e:
            print(f'전체 통신 종료 {e}')
            break


print('server starts..')
receive()


# 연결 요청을 수락함. 그러면 아이피주소, 포트등 데이터를 return data = client_socket.recv(65535) # 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨) print("받은 데이터:", data.decode())
# client_socket, addr = server_socket.accept()

# 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨)
# data = client_socket.recv(65535)
# print("받은 데이터:", data.decode())
