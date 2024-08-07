from django import forms
from new.models import Contact, Newsletter

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=255)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class Newsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'