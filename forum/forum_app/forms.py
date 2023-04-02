from django import forms

class User_Login(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    passwort = forms.PasswordInput()