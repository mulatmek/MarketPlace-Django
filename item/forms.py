from django import forms

from .models import Item

CLASS_INPUT = 'w-full px-6 py-4 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:border-indigo-500'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'price', 'image')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': CLASS_INPUT
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': CLASS_INPUT
    }))

    price = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': 'Price',
        'class': CLASS_INPUT
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': CLASS_INPUT    
    }))

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'price', 'image', 'is_sold')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': CLASS_INPUT
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': CLASS_INPUT
    }))

    price = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': 'Price',
        'class': CLASS_INPUT
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': CLASS_INPUT    
    }))