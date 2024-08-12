import qrcode

# Link que você deseja converter em QR Code
link = "https://www.seulink.com"

# Cria um objeto QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adiciona o link ao QR Code
qr.add_data(link)
qr.make(fit=True)

# Cria uma imagem do QR Code
img = qr.make_image(fill='black', back_color='white')

# Salva a imagem em um arquivo
img.save("qrcode.png")

print("QR Code gerado e salvo como 'qrcode.png'")
