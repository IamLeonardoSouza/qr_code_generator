# QR Code Generator

Este projeto é uma simples aplicação Python que gera um QR Code a partir de um link fornecido. O QR Code é gerado usando a biblioteca `qrcode` e a imagem resultante é salva em um arquivo PNG.

## Requisitos

- Python 3.12.4 instalado
- Biblioteca `qrcode`

## Instalação

Antes de executar o código, você precisa instalar a biblioteca `qrcode`. Você pode fazer isso usando o pip:

```bash
pip install qrcode[pil]
```

Para gerar um QR Code para um link diferente, modifique a variável link com o URL desejado:

```bash
link = "https://www.seulink.com"
```

Ao final da configuração, será criado um arquivo chamado qrcode.png no mesmo diretório onde o script é executado. O QR Code gerado pode ser escaneado para acessar o link fornecido.