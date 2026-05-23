import requests
import os
from tqdm import tqdm
link_github = "https://github.com/alaodiogo/minecraft.py/releases/download/Modpack/The.frog.1.12.2.mrpack"
pasta = "/home/alaodiogo/Documentos/Minecraft/"
nome_modpack = "the frog.mrpack"
pasta_modpack = "The frog"

def baixar_modpack():
    baixar_modpack = requests.get(link_github, stream=True)
    if baixar_modpack.status_code == 200:
        if not os.path.exists(os.path.join(pasta, pasta_modpack)):
            os.mkdir(os.path.join(pasta, pasta_modpack))
        with open(os.path.join(pasta, pasta_modpack,nome_modpack), "wb") as arquivo:
            tamanho_total_arq = int(baixar_modpack.headers.get("content-length"))
            with tqdm(total = tamanho_total_arq, unit = "B", unit_scale=True) as barra_de_progresso:
                for pedacos in baixar_modpack.iter_content(chunk_size=1024):
                    arquivo.write(pedacos)
                    barra_de_progresso.update(len(pedacos))
        print("Modpacks baixado com sucesso!")