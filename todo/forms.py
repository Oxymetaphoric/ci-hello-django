
# forms.py
from django import forms
from .models import Item  # Import your model

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Specify the model the form is based on
        fields = ['name', 'done']  # Specify the fields you want to include in the form
