import socket
import os
import sys
import platform

print("Nom du PC : " + socket.gethostname())
print("FQDN / Nom de domaine : " + socket.getfqdn())
print("Plate-forme du système : " + sys.platform)
print("Machine : " + platform.machine())
print("Processeur : " + platform.processor())
print("Systeme d'exploitation : " + platform.platform())
print("Système : " + platform.system())
print("Version de l'OS : " + platform.version())
