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
    TOKEN = '7205524595:AAHBH4ZP_-CA0x5cUAD-p3pMRLtay4_tMq8'
    CHAT_ID = '-4858896487'
    url = f"https://api.telegram.org/bot7205524595:AAHBH4ZP_-CA0x5cUAD-p3pMRLtay4_tMq8/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': mensagem}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        logging.error(f"Erro ao enviar Telegram: {e}")
