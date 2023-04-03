from django import forms

class User_Login(forms.Form):
    email = forms.EmailField(label=False ,widget= forms.TextInput(attrs={'placeholder': 'E-Mail'}))
    passwort = forms.CharField(label=False ,widget=forms.PasswordInput(attrs={'placeholder': 'passwort'}))