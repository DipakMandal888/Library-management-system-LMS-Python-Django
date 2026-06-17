from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'user',
            'membership_type',
            'phone',
            'address',
            'is_active',
        ]
        widgets = {
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone number',
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Optional member address',
                'rows': 5,
            }),
        }
