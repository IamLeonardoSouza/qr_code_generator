from django.db import models

class QRCodeHistory(models.Model):
    url = models.URLField()
    generated_at = models.DateTimeField(auto_now_add=True)
    qr_image = models.ImageField(upload_to='qr_codes/')  # Você precisará configurar o MEDIA_URL e MEDIA_ROOT

    def __str__(self):
        return f"{self.url} - {self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"
