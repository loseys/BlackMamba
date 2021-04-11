####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
#################################################################################### 

"""
Generates a Fernet key.
"""

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
print(key.decode('utf-8'))
input('')
