from django import forms
from django.contrib.auth.models import User

class register_form(forms.ModelForm):

    password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Passwort'}))
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(label=False,widget=forms.EmailInput(attrs={'placeholder':'E-Mail'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']