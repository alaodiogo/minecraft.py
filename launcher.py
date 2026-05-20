import subprocess
from minecraft_launcher_lib import *

diretorio_mine = "/home/alaodiogo/Documentos/Minecraft/"
versao = 0
configuracoes = {
    "username": "alaodiogo",
    "uuid": "841e42a3-86b7-4f7f-ae5d-5959bd1a17c3",
    "token": "token"
    }

versao = input("Digite a versão do Minecraft que deseja instalar: ")
install.install_minecraft_version(versao, diretorio_mine)
print("Instalação concluída!")

iniciar_mine = command.get_minecraft_command(versao, diretorio_mine, configuracoes)
subprocess.run(iniciar_mine)
