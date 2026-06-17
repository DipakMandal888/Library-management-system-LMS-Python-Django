from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'category',
            'isbn',
            'published_date',
            'description',
            'total_copies',
            'available_copies',
            'status',
            'cover_image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Book title',
            }),
            'isbn': forms.TextInput(attrs={
                'placeholder': '13-digit ISBN',
            }),
            'published_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Optional book description',
                'rows': 5,
            }),
            'total_copies': forms.NumberInput(attrs={
                'min': 1,
            }),
            'available_copies': forms.NumberInput(attrs={
                'min': 0,
            }),
        }
