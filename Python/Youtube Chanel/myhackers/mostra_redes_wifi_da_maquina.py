from asyncio import subprocess
from os import chdir, getcwd, system
import re

print("-"*60)
print("Redes Wifi encontradas neste computador:")
print("-"*60)
showLocalNetWorks = "/etc/NetworkManager/system-connections/"
#troca o diretório
chdir(showLocalNetWorks)
pwd = getcwd()
#exibe o diretório corrente
print("Current working directory: {0}".format(pwd))
command_output = subprocess.run([showLocalNetWorks], capture_output = True).stdout.decode
profile_names = (re.findall("All User Profile    : (.*)\r", command_output))
#guarda o comando para listar 
ls_a = "ls -lha"
print(system(ls_a))
print("-"*60)
armazenaRede = "ls -lha | head -4 | tail -1"
system(armazenaRede)






