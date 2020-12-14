from django import forms
from .models import*

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title','instructor','summary', 'code', 'content_type']

    