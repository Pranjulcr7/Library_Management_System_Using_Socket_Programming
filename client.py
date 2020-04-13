import socket
import pickle
import json


def receive(conn):
    return conn.recv(2048).decode()


def send(conn, data):
    conn.send(data.encode())


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 12345  # socket server port number
    conn = socket.socket()  # instantiate
    conn.connect((host, port))  # connect to the server

    message = input("Enter username : ")
    send(conn, message) # send message
    data = receive(conn)  # receive response
    books = json.loads(data)

    book_issued = library(books)
    send(conn, book_issued)
    data = receive(conn)
    print(data)

    conn.close()  # close the connection


def library(books):
    for key,book in books.items():
        print("\nBook_id :", book['id'])
        print("Name :", book['name'])
        print("Author :", book['author'])
        print("Publisher :", book['publisher'])

    book_issued = input("\nEnter Book_id to issue book : ")
    return book_issued


if __name__ == '__main__':
    print("\nWelcome to Library Management System!\n")
    client_program()
    print("\n\tConnection closed!\n")
