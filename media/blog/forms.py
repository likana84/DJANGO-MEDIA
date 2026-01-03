from django.forms import ModelForm
from django import forms

from .models import  Comment

class CommentForm(ModelForm):

   

  
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'border:none;background-color:transparent;', 'placeholder': 'Your name'}),
            'content': forms.Textarea(attrs={'style': 'border:none;background-color:pink;', 'rows': 4, 'placeholder': 'Your comment'})
        }
  #class Meta:
        #model = Comment
        #fields = ['name', 'content' ]
        #class CommentForm(ModelForm):
        