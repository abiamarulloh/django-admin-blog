from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post  # Import your Post model

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  

    class Meta:
        model = Post
        fields = '__all__'