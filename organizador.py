# ========================================
# Script: organizador.py
# Autor: Felipe Leal
# Descrição: Organização automática de arquivos por extensão
# ========================================


# Bibliotecas padrão para manipulação de arquivos e logs
import logging
import os
import shutil
import glob
import time
from time import sleep
from notificacoes import enviar_telegram

# *_____é representa qualquer sequência de caracteres em um nome de arquivo, incluindo nenhuma sequência
# ?_____representa qualquer caractere único em um nome de arquivo
# []____são usados para criar um conjunto de caracteres e consiste em qualquer caractere dentro desse conjunto
# [!]___o conjunto de caracteres será negado. Ele irá responder a qualquer característica que não esteja dentro desse conjunto

# Caminho principal onde os arquivos serão monitorados e organizados
origem = 'C:/Users/felip/Downloads/'

# Dicionário que define as extensões de arquivos e suas respectivas pastas de destino
extensoes_por_pasta = {
    'PDF': ['pdf', 'PSF'],
    'Word': ['docx'],
    'Excel': ['xls', 'xlsx', 'xlsm', 'csv'],
    'Videos': ['mp4', 'MP4'],
    'Imagens': ['jpg', 'jpeg', 'png'],
    'Executaveis': ['exe'],
    'Audios': ['mp3']
}

# Move arquivos de uma extensão específica para uma subpasta designada
# Também registra a movimentação no log
def mover_arquivos(origem, extensao, subpasta):
    destino = os.path.join(origem, subpasta)
    os.makedirs(destino, exist_ok=True)
    arquivos = glob.iglob(os.path.join(origem, f'*.{extensao}'))

    agora = time.time()
    movidos = 0
    for arq in arquivos:
        # Ignorar arquivos com menos de 30 minutos de modificação
        if agora - os.path.getmtime(arq) < 1800:
            continue

        nome = os.path.basename(arq)
        shutil.move(arq, destino)
        logging.info(f'Movido: {nome} -> {destino}')
        movidos += 1

    return movidos

# Itera sobre o dicionário de extensões para mover os arquivos automaticamente
def organizar_arquivos():
    total = 0
    for pasta, extensoes in extensoes_por_pasta.items():
        for ext in extensoes:
            total += mover_arquivos(origem, ext, pasta)

        return total

# Menu interativo exibido no terminal para o usuário escolher ações manuais
def menu():
    while True:
        print("\n=== Organizador de Arquivos ===")
        print("1. Organizar arquivos automaticamente")
        print("2. Organizar apenas uma extensão")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        # Organiza os arquivos automaticamente
        if escolha == '1':
            total = organizar_arquivos()
            msg = f"✅ Organização concluída.\nArquivos movidos: {total}"
            print(msg)
            enviar_telegram("✅ Organização automática concluída com sucesso.")
            sleep(2)

        # Permite que você escolha qual extensão você quer organizar
        elif escolha == '2':
            ext = input("Digite a extensão (ex: pdf): ").lower()
            pasta = input("Nome da pasta de destino: ")
            mover_arquivos(origem, ext, pasta)
            print(f"Arquivos .{ext} movidos para {pasta}.")
            sleep(2)

        # Finaliza a execução do programa
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu interativo se o script for executado diretamente
if __name__ == '__main__':
    menu()

