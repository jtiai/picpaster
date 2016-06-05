from django import forms
from . import models


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.UploadImage
        fields = ('title', 'image', )
