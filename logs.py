# ========================================
# Script: logs.py
# Autor: Felipe Leal
# Descrição: Gera logs de movimentção de arquivos
# ========================================

import os
import logging
from datetime import datetime
from organizador import origem

# Configurações iniciais do sistema de log
# Gera um arquivo de log diário na subpasta "Logs" da origem
log_pasta = os.path.join(origem, 'Logs')
os.makedirs(log_pasta, exist_ok=True)
log_caminho = os.path.join(log_pasta, f"movimentacoes_{datetime.now().date()}.log")

# Define o formato e o destino do arquivo de log
logging.basicConfig(filename=log_caminho, level=logging.INFO, format='%(asctime)s - %(message)s')