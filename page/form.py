from django import forms
from .models import SongFile, Comments

class SongForm(forms.ModelForm):
    class Meta:
        model = SongFile
        fields = ('title', 'audio', 'file_type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }