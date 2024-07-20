
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
```
## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/oculos-virtual.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd oculos-virtual
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Como Usar

Certifique-se de que você tem imagens suficientes para cada símbolo na pasta `symbols/`.

Treine o modelo executando o script principal:
```sh
python main.py
```
## Adicionando Novas Imagens

Para melhorar o desempenho do modelo, adicione mais imagens na pasta `symbols/`:

```bash
oculos-virtual/
├── symbols/
│   ├── A/
│   │   ├── img1.png
│   │   ├── img2.png
│   │   ├── img3.png  # Nova imagem adicionada
│   │   └── ...
│   ├── B/
│   │   ├── img1.png
│   │   ├── img2.png
│   │   ├── img3.png  # Nova imagem adicionada
│   │   └── ...
│   └── ...
´´´
## Dependências

- Python 3.x
- OpenCV
- Scikit-learn
- Joblib
- Pygame

Você pode instalar todas as dependências necessárias usando o arquivo `requirements.txt`.

## Problemas Conhecidos

- Certifique-se de que a câmera está corretamente conectada e funcional.
- O desempenho do modelo pode variar dependendo da qualidade e quantidade de dados de treinamento.
- Para melhores resultados, utilize imagens claras e bem definidas dos símbolos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
