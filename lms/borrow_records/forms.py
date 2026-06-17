from django import forms

from .models import BorrowRecord


class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = [
            'member',
            'book',
            'due_date',
            'return_date',
            'fine_amount',
            'notes',
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'return_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'fine_amount': forms.NumberInput(attrs={
                'min': 0,
                'step': '0.01',
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Optional notes',
                'rows': 5,
            }),
        }
