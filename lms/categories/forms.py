from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Category name',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Optional category description',
                'rows': 5,
            }),
        }
