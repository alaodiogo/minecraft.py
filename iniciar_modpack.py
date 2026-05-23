import subprocess
import minecraft_launcher_lib
import baixar_modpack
import os

pasta_modpack = os.path.join(baixar_modpack.pasta, baixar_modpack.pasta_modpack, baixar_modpack.nome_modpack)
pasta_minecraft = baixar_modpack.pasta
configuracoes = {
    "username": "alaodiogo",
    "uuid": "841e42a3-86b7-4f7f-ae5d-5959bd1a17c3",
    "token": "token"
    }

baixar_modpack.baixar_modpack()
minecraft_launcher_lib.mrpack.install_mrpack(pasta_modpack, pasta_minecraft)
iniciar_mine = minecraft_launcher_lib.command.get_minecraft_command(
    minecraft_launcher_lib.mrpack.get_mrpack_launch_version(pasta_modpack),
    pasta_minecraft,
    configuracoes,
)
print("Iniciando o Minecraft...")
subprocess.run(iniciar_mine)