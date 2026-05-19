from minecraft_launcher_lib import *
diretorio_mine = "/home/alaodiogo/Documentos/Minecraft/"
conta = microsoft_account.get_auth_code_from_url(url: str)

#def minecraft_launcher():
versao = input("Digite a versão do Minecraft que deseja instalar: ")
install.install_minecraft_version(versao, diretorio_mine)
command.get_minecraft_command(versao, diretorio_mine, conta)