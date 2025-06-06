# Organizador Automático de Arquivos

Este projeto tem como objetivo organizar automaticamente os arquivos de um diretório, separando-os em subpastas com base na extensão dos arquivos, ignora arquivos recentes (menos de 30 minutos), gera logs de movimentação e envia notificações via Telegram. 

## Funcionalidades

- Organização automática de arquivos por extensão.
- Criação de subpastas automaticamente (PDF, Word, Excel, etc.).
- Registro de logs detalhados de cada arquivo movido.
- Notificações via Telegram ao concluir a organização (opcional).
- Interface via terminal estilo menu-driven.
- Integração com Agendador de Tarefas do Windows para execução automática.

## Estrutura do Projeto

```
📁 organizador/
├── organizador.py               # Lógica principal do organizador
├── organizador_automatico.py    # Para integrar ao Agendador de tarefas Windows
├── notificacoes.py              # Envio de mensagens para o Telegram
├── logs.py                      # Configuração de log
├── Logs/                        # Arquivos de log gerados por data
└── README.md                    # Instruções e documentação do projeto
```

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/organizador-arquivos.git
    cd organizador-arquivos
    ```

2. Configure o bot do Telegram:
    - Crie um bot via [@BotFather](https://t.me/BotFather)
    - Copie o token e insira no arquivo `notificacoes.py`
    - Adicione seu chat_id (pode ser de grupo)

3. Edite o script principal (`organizador.py`) com o caminho do seu diretório

4. Execute o script:
    ```bash
    python organizador.py
    ```

5. Para automatizar:
    - Crie um `.vbs` para execução silenciosa
    - Use o Agendador de Tarefas do Windows para rodar periodicamente

## Requisitos

- Python 3.8+
- Módulos: `os`, `shutil`, `glob`, `logging`, `requests`

## 🛠️ Futuras melhorias

- Compactar arquivos antigos
- Interface gráfica com Tkinter
- Dashboard com Flask para relatórios
- Integração com e-mail

## Exemplo de Execução

```
=== Organizador de Arquivos ===
1. Organizar arquivos automaticamente
2. Organizar apenas uma extensão
3. Sair
Escolha uma opção:
```

---

Feito com 💻 por Felipe Leal
