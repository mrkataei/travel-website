from django import forms
from new.models import Contact, Newsletter
from captcha.fields import CaptchaField

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=255)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        captcha = CaptchaField(label='Please enter the characters in the image')
        fields = '__all__'

class Newsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'