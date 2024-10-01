# QR Code Generator

This project is a simple Python application that generates a QR Code from a provided link. The QR Code is generated using the `qrcode` library, and the resulting image is saved in a PNG file.

## Requirements

- Python `3.12.4` installed
- `qrcode` library

## Installation

Before running the code, you need to install the `qrcode` library. You can do this using pip:

```bash
pip install qrcode[pil]
```

To generate a QR Code for a different link, modify the link variable with the desired URL:

```bash
link = "https://www.seulink.com"
```

At the end of the configuration, a file called qrcode.png will be created in the same directory where the script is executed. The generated QR Code can be scanned to access the link provided.

Example of a functional QR Code:

![Logotipo do Projeto](images/qrcode.png)
