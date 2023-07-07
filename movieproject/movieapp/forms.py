from django import forms
from . models import movielist

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model=movielist
        fields=['name','desc','year','img']