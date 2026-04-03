import os
import shutil

# 1. Defina aqui os caminhos (use r antes das aspas para evitar erro de barras)
pasta_origem = r'./archive/lfw-deepfunneled/'
pasta_destino = r'./humano/'

# Extensões de imagem que você quer buscar
extensoes_validas = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

print("Iniciando a migração...")

contador = 0
for raiz, diretorios, arquivos in os.walk(pasta_origem):
    for arquivo in arquivos:
        if arquivo.lower().endswith(extensoes_validas):
            caminho_completo = os.path.join(raiz, arquivo)
            
            # Evita sobrescrever arquivos com o mesmo nome
            destino_final = os.path.join(pasta_destino, arquivo)
            if os.path.exists(destino_final):
                nome, ext = os.path.splitext(arquivo)
                destino_final = os.path.join(pasta_destino, f"{nome}_{contador}{ext}")

            shutil.move(caminho_completo, destino_final)
            contador += 1

print(f"Pronto! {contador} fotos foram movidas para: {pasta_destino}")