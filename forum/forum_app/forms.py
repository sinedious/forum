from django import forms
from forum_app.models import beitrag

class PostBeitrag(forms.ModelForm):
    class Meta:
        model = beitrag
        fields = ['titel', 'beitrag']
        widgets = {'beitrag': forms.Textarea(attrs={'placeholder': 'Beitrag'}), 
                   'titel':forms.TextInput(attrs={'placeholder': 'Titel'})}

from forum_app.models import beitrag, comment

class CommentForm(forms.ModelForm):
        Kommentar = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
    }))
        class Meta:
             model = comment
             fields = ['Kommentar']
        

        
        