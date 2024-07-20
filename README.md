
# Óculos Virtual com Tradução de Símbolos

Este projeto implementa um sistema de tradução de símbolos utilizando a câmera de um notebook e um modelo de Machine Learning. Ele captura imagens da câmera, detecta e traduz símbolos impressos em um papel.

## Tabela de Conteúdos
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Adicionando Novas Imagens](#adicionando-novas-imagens)
- [Dependências](#dependências)
- [Problemas Conhecidos](#problemas-conhecidos)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Estrutura do Projeto

```bash
oculos-virtual/
│
├── symbols/  # Diretório contendo as imagens de símbolos para treinamento
│   ├── A/
│   │   ├── img1.png
│   │   ├── img2.png
│   │   └── ...
│   ├── B/
│   │   ├── img1.png
│   │   ├── img2.png
│   │   └── ...
│   └── ...
│
├── utils/  # Diretório com funções utilitárias
│   ├── camera.py
│   ├── display.py
│   └── symbol_recognition.py
│
├── model.pkl  # Modelo treinado para reconhecimento de símbolos
│
├── main.py  # Script principal para rodar o sistema
│
└── README.md  # Documentação do projeto
