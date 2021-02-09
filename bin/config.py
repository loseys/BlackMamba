####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
####################################################################################

"""
Reads the /bin/profile/socket.txt to get the values of main port, the video port and the
ip address from the server and creates the SERVER_IP, PORT and PORT_VIDEO variables.
"""
with open('bin/profile/socket.txt','r') as f:
    content = f.read()
    f.close()

content = content.lstrip().rstrip()
content = content.split('\n')

SERVER_IP, PORT, PORT_VIDEO = content

SERVER_IP = SERVER_IP.replace('SERVER_IP', '').replace('=', '').replace(' ', '').lstrip().rstrip()
PORT = PORT.replace('PORT', '').replace('=', '').replace(' ', '').lstrip().rstrip()
PORT_VIDEO = PORT_VIDEO.replace('PORT_VIDEO', '').replace('=', '').replace(' ', '').lstrip().rstrip()

# print(f'{SERVER_IP}/{PORT}/{PORT_VIDEO}')
