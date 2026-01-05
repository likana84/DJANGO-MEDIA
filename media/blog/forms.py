from django.forms import ModelForm


from .models import  Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # remove labels and add common styling attrs
        if 'name' in self.fields:
            self.fields['name'].label = 'Name'
            self.fields['name'].widget.attrs.update({'style': 'width:200px;background-color:pink;display:block;' })
        if 'content' in self.fields:
            self.fields['content'].label = 'Content'
            self.fields['content'].widget.attrs.update({'style': 'width:200px;background-color:pink;margin-top:10px;display:block;' })
    class Meta:
        model = Comment
        fields = ['name',  'content']
       
        
        