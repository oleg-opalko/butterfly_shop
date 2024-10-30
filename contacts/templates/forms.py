from django import forms

from contacts.models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'data-rule': 'email',
            'data-msg': 'Please enter a valid email address',
            'id': 'email'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message',
            'data-rule': 'minlen:10',
            'data-msg': 'Please enter at least 10 chars',
            'id': 'message',
            'rows': 5
        })
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
