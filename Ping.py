import os
ip = input("Donne l'adresse IP ou le nom de dommaine (ex : google.fr) :")
retourduping = os.system("ping -c 1 " + ip)

if retourduping == 0:
  print(ip, 'OK - Le ping fonction !')
else:
  print(ip, 'NO OK - Le ping ne fonctionne pas !')
