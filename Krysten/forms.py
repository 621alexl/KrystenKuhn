
# forms.py 
from django import forms 
from .models import *
  
class DescriptionForm(forms.ModelForm): 
  
    class Meta: 
        model = Description 
        fields = ['description', 'image'] 