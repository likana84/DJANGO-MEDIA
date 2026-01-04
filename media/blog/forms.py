from django.forms import ModelForm
from django import forms

from .models import  Comment

class CommentForm(ModelForm):

   

  
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'border:none;background-color:pink;width:255px;'}),
            'content': forms.Textarea(attrs={'style': 'border:none;background-color:pink;rows:4;cols:8;display:block;margin-bottom:10px;'}),
        }
  #class Meta:
        #model = Comment
        #fields = ['name', 'content' ]
        #class CommentForm(ModelForm):
        