import django.forms
from models import Photo 

class SillyForm(django.forms.ModelForm):
    class Meta:
        model = Photo 
        fields = ['name',]
