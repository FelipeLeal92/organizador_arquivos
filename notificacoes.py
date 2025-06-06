# ========================================
# Script: notificacoes.py
# Autor: Felipe Leal
# Descrição: Envia logs para canais externos
# ========================================

import requests
import logging

# Importa requests para enviar dados via API do Telegram
# Importa o caminho do log definido no módulo 'logs'
def enviar_telegram(mensagem):
    TOKEN = 'COLE AQUI O TOKEN DO SEU BOT'
    CHAT_ID = 'COLE QUI O ID DO GRUPO QUE RECEBERÁ AS NOTIFICAÇÕES'
    url = f"https://api.telegram.org/botSEUTOKENAQUI/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': mensagem}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        logging.error(f"Erro ao enviar Telegram: {e}")
