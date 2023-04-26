from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class userProfileForm(forms.ModelForm):
    password = None
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(label=False,widget=forms.EmailInput(attrs={'placeholder':'E-Mail'}))

    class Meta:
        model = User
        fields = ('username', 'email')