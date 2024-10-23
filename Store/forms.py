from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'massage', 'phone']

class BlogCommentForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'message']