from django import forms

class QRCodeForm(forms.Form):
    url = forms.URLField(label='URL', required=True, widget=forms.URLInput(attrs={
        'class': 'form-input',
        'placeholder': 'Digite a URL aqui...'
    }))
    color = forms.CharField(label='Cor (HEX)', initial='#000000', required=False)
    logo = forms.ImageField(label='Logo (opcional)', required=False)
