<p align="center">
  <img src="https://i.imgur.com/tGj5RyK.png" width=250 height=250 alt="ST"/>
</p>

# BLACKMAMBA

[![platforms](https://img.shields.io/badge/platform-windows%20%7C%20linux-orange)](https://github.com/loseys/Oblivion/)
[![version](https://img.shields.io/badge/version-v1.0.14-orange)](https://github.com/loseys/Oblivion/)
[![Python 3.8.6](https://img.shields.io/badge/python-3.8-orange.svg)](https://www.python.org/downloads/release/python-386/)
[![Release](https://img.shields.io/badge/Release-beta-orange)](https://github.com/loseys/Oblivion/)
[![license](https://img.shields.io/badge/license-MIT-orange)](https://github.com/loseys/Oblivion/)

BlackMamba is a multi client C2/post exploitation framework with some spyware features. Powered by Python 3.8.6 and QT Framework.

Some of BlackMamba features are:
- **Multi Client** - Supports multiple client connections at the same time.
- **Real Time Communication Updates** - Real time communication and updates between the client and server.
- **Encrypted Communication** - Almost all communications are encrypt, with exception of screen video streaming.
- **Screenshot Gattering** - Get a realtime screenshot from the client.
- **Video Streaming** - Watch in real time the client screen.
- **Client Lock** - Lock and unlock the machine of the client.
- **Encrypted File Transfer (upload/download)** - Download files from the client or uploads files for the client.
- **Keylogger** - Register all the keys pressed by client.
- **Web Downloader** - Download files from URLs or content by RAW pages.

<p align="center">
  <img src="https://user-images.githubusercontent.com/61597947/107297935-23c6e800-6a53-11eb-9fa4-dcfbb516e5a7.png" width=1127 height=618 alt="ST"/> 
</p> </p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61597947/107297933-23c6e800-6a53-11eb-8b24-9d49876797e1.png" width=1366 height=626 alt="ST"/> 
</p> </p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61597947/107297929-21fd2480-6a53-11eb-96d4-a45551f07954.png" width=1149 height=655 alt="ST"/> 
</p> </p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61597947/107297931-232e5180-6a53-11eb-8070-a0081b1f4fd3.png" width=978 height=699 alt="ST"/> 
</p> </p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61597947/107297937-245f7e80-6a53-11eb-8eb5-0c8876cb2b58.png" width=976 height=697 alt="ST"/> 
</p> </p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61597947/107297938-245f7e80-6a53-11eb-9653-bea856c87951.png" width=976 height=699 alt="ST"/> 
</p> </p>

# Install Guide

> SERVER INSTALL

1º - Download the BlackMamba;
    
2º - Install the PIP packages;

     PyQt5
     Pillow
     PyAutoGUI
     pytest-shutil
     cryptography
     pynput
     pygame

3º - Open the port 65000 and 65005 in your Gateway or Router (the port number is optional); 

4º - Create an exception in firewall for BlackMamba or disable it;

5ª - Go to "BlackMamba/bin/profile/socket.txt" and input the port number opened;

     SERVER_IP=0.0.0.0
     PORT=65000
     PORT_VIDEO=65005

     IMPORTANT: Do not change the 0.0.0.0.
     
6º (OPTIONAL) - Go to BlackMamba folder and open the "keygen.py" file. Copy the result
key and paste in the "BlackMamba/bin/profile/crypt_key.py" ;

    The BlackMamba use a default cryptography key, is interesting that you change it.
    
7º - Back to BlackMamba root folder and open the "main.py" file;

    WINDOWS
    python main.py
    
    GNU/LINUX
    sudo chmod 777 main.py
    sudo python3.8 main.py
   
        KALI LINUX
        (sudo chmod 777 main.py)
        (sudo python3 main.py)

8º - Click on the button that have a person icon and plus signal;

9º - Input the path where the Python file will be created, input the both port numbers and 
the IP address (external or local) of your host, then click on the "Create" button.

> CLIENT INSTALL

After create the Client script you'll need to open the script in the host target:

**WINDOWS**

python script.py

**GNU/LINUX**

1º Download the packages:

    scrot -y
    python3-pip -y
    python3-tk -y
    python3-dev -y

2º sudo python3.8 script.py

    KALI LINUX
    (sudo python3 script.py)
  
**IMPORTANT**: The script of client not have persistence, if you want to do a persistence you'll need 
to made by yourself. Another important point is that the client script maybe delay some seconds or few 
minutes for connect/reconnect.

# Release status

Currently the BlackMamba is on beta stage, this means that the features are all completed but likely to contain a number of known and unknown bugs. Is important reinforce that the majority of critical bugs like crashes or buffer overflow alredy have been solved.

# More information

For more information please take a look in the Wiki.

# Call for Contributions

I'm just one person developing the BlackMamba, if anyone finds this tool useful and would like to add some functionality, improve the code performace or improve something in the BlackMamba the best way to get it added is to submit a pull request.

If you want to collaborate but you don't know Python you can help me so much with bug reports, you can do it with Issues :)

# Author

Gustavo ([Loseys](https://github.com/loseys))

# Acknowledgments, Contributors & Involuntary Contributors

**(In no particular order)**

- [Random Davis](https://stackoverflow.com/users/6273251/random-davis) for help me with video streaming script.
- [Wanderson-Magalhaes](https://github.com/Wanderson-Magalhaes) for GUI inspiration. Tamo junto Wanderson.
- [@byt3bl33d3r](https://github.com/byt3bl33d3r) for README inspiration.
- **Vitor** for help me with some English translations.
