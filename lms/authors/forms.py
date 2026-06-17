from django import forms

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Author name',
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Optional author biography',
                'rows': 6,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'author@example.com',
            }),
        }
