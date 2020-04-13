import socket
import pickle
import json
from book_management import get_books, issue_book


def receive(conn):
    return conn.recv(2048).decode()


def send(conn, data):
    conn.send(data.encode())


def run_server():
    host = socket.gethostname()# get the hostname
    port = 12345  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("\nConnection established from: " + str(address))

    data = receive(conn)
    print("\nLogged in User : ", data)
    books = get_books()
    books_dict = dict([(x.id, x) for x in books])
    data = dict([(x.id, x.__dict__) for x in books])
    send(conn, json.dumps(data))

    book_issued = receive(conn)
    try:
        data = issue_book(books_dict[book_issued])
    except:
        data = 'Error! '
    print(data+f'\nBook_id : {book_issued}')
    send(conn, data)

    conn.close()  # close the connection


if __name__ == '__main__':
    print("\nLibrary Management System!\n")
    run_server()
    print("\nServer stopped\n")
