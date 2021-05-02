<h1 align="center">
  <br>
  <a href="https://github.com/loseys/Oblivion/"><img src="https://i.imgur.com/tGj5RyK.png" width=160 height=150 alt="BlackMamba"></a>
  <br>
  BlackMamba
  <br>
</h1>

<h4 align="center">Command and Control</h4>

<p align="center">
  <a href="https://github.com/loseys/Oblivion/">
    <img src="https://img.shields.io/badge/platform-windows%20%7C%20linux-orange">
  </a>
  <a href="https://github.com/loseys/Oblivion/">
    <img src="https://img.shields.io/badge/version-v1.0.41-orange">
  </a>
  <a href="https://github.com/loseys/Oblivion/">
      <img src="https://img.shields.io/badge/python-3.8.6-orange.svg">
  </a>
</p>

### What's BlackMamba?

Black Mamba is a Command and Control (C2) that works with multiple connections at same time. It was developed with Python and with Qt Framework and have multiples features for a post-exploitation step.

### Some Features

- [x] Multiple clients.
- [x] Real-time communication.
- [x] Encrypted communication
- [x] Screenshot gathering.
- [x] Real-time video capture.
- [x] Locking of client mouse.
- [x] Download and upload of files.
- [x] Keylogger.
- [x] Web downloader.

### Call for Contributions⚠️

Hey, before you go to gallery you need to know that the BlackMamba is a open project, so, if you finds this tool useful and wants to add some functionality, improve the code performance or improve something in the BlackMamba, the best way to get it added is to submit a pull request <3

### Gallery

<img src="https://user-images.githubusercontent.com/61597947/107297935-23c6e800-6a53-11eb-9fa4-dcfbb516e5a7.png" width=100% />
<img src="https://user-images.githubusercontent.com/61597947/107297929-21fd2480-6a53-11eb-96d4-a45551f07954.png" width=100% />
<img src="https://user-images.githubusercontent.com/61597947/107297933-23c6e800-6a53-11eb-8b24-9d49876797e1.png" width=100% />
<img src="https://user-images.githubusercontent.com/61597947/107297931-232e5180-6a53-11eb-8070-a0081b1f4fd3.png" width=100% />
<img src="https://user-images.githubusercontent.com/61597947/107297937-245f7e80-6a53-11eb-8eb5-0c8876cb2b58.png" width=100% />
<img src="https://user-images.githubusercontent.com/61597947/107297938-245f7e80-6a53-11eb-9653-bea856c87951.png" width=100% />


### Installation

1º - Download the BlackMamba;
    
2º - Install the PIP packages;
   
     pip install -r requirements.txt  

3º - Open the port 65000 and 65005 in your Gateway or Router (the port number is optional); 

4º - Create an exception in the firewall for BlackMamba or disable it;

5ª - Go to "BlackMamba/bin/profile/socket.txt" and input the port number opened;

     SERVER_IP=0.0.0.0
     PORT=65000
     PORT_VIDEO=65005

>IMPORTANT: Do not change the 0.0.0.0.
     
6º (OPTIONAL) - Go to the BlackMamba folder and open the "keygen.py" file. Copy the resulting
key and paste in the "BlackMamba/bin/profile/crypt_key.py" ;

    The BlackMamba uses a default cryptography key. It is interesting that you change it.
    
7º - Back to BlackMamba root folder and open the "main.py" file; 

    WINDOWS
    python main.py
    
    KALI LINUX
    (sudo chmod 777 main.py)
    (sudo python3 main.py)
    
    ANOTHER LINUX
    sudo chmod 777 main.py
    sudo python3.8 main.py

8º - Click on the button that has a person icon and plus signal;

9º - Input the path where the Python file will be created, input both port numbers and 
the IP address (external or local) of your host, then click on the "Create" button.

### Client Installation

After creating the Client script, you'll need to open the script in the host target:

>WINDOWS

python script.py

>GNU/LINUX

1º Download the packages:

    scrot -y
    python3-pip -y
    python3-tk -y
    python3-dev -y

2º sudo python3.8 script.py

    KALI LINUX
    (sudo python3 script.py)
  
*IMPORTANT: The script of the client does not have persistence. If you want to do persistence, you'll need
to make it by yourself. Another important point is that the client script maybe delay some seconds or few 
minutes for connect/reconnect.*

### Author

Gustavo ([Loseys](https://github.com/loseys))

### Acknowledgments, Contributors & Involuntary Contributors

**(In no particular order)**

- [Random Davis](https://stackoverflow.com/users/6273251/random-davis)
- [Wanderson-Magalhaes](https://github.com/Wanderson-Magalhaes)
- [@byt3bl33d3r](https://github.com/byt3bl33d3r)
- **Vitor**
- [cybernobie](https://github.com/cybernobie)
- [w0rk3r](https://github.com/w0rk3r)
- [wesley587](https://github.com/wesley587)
