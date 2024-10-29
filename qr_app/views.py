import qrcode
from PIL import Image
from django.shortcuts import render
from .forms import QRCodeForm
import base64
from io import BytesIO

def generate_qr_code(request):
    qr_img = None

    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            url = form.cleaned_data['url']
            color = form.cleaned_data['color'] or '#000000'
            logo = form.cleaned_data.get('logo')

            # Configuração do QR Code
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)

            # Gera a imagem do QR Code com a cor selecionada
            # Aqui estamos utilizando o método make_image com as cores definidas
            img = qr.make_image(fill_color=color, back_color="white").convert('RGB')

            # Adicionar logo, se houver
            if logo:
                logo = Image.open(logo)
                logo = logo.resize(img.size)

                # Criar uma máscara para aplicar opacidade
                logo = logo.convert("RGBA")
                logo_with_alpha = Image.new("RGBA", logo.size)
                for x in range(logo.width):
                    for y in range(logo.height):
                        r, g, b, a = logo.getpixel((x, y))
                        logo_with_alpha.putpixel((x, y), (r, g, b, int(a * 0.2)))  # Define a opacidade

                # Adicionar o logotipo como camada de fundo
                img.paste(logo_with_alpha, (0, 0), logo_with_alpha)

            # Converter imagem para base64
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            qr_img = base64.b64encode(buffer.getvalue()).decode('utf-8')

    else:
        form = QRCodeForm()

    return render(request, 'index.html', {'form': form, 'qr_img': qr_img})
