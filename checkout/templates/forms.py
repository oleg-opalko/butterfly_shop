from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'First Name',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'first_name'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Last Name',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'last_name'
        })
    )
    country = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Country',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'country'
        })
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Address',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'address'
        })
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'City',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'city'
        })
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'State',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'state'
        })
    )
    zip_code = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Zip Code',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'zip_code'
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Phone',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'phone'
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Email',
            'data-rule': 'email',
            'data-msg': 'Please enter your email',
            'id': 'email'
        })
    )

    create_account = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'id': 'acc'})
    )

    order_notes = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'checkout__input',
            'placeholder': 'Notes about your order...',
            'data-rule': 'minlen:4',
            'type': 'text',
            'data-msg': 'Please enter at least 4 chars',
            'id': 'order_notes'
        }),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'checkout__input form-control',
            'placeholder': 'Account Password',
            'data-rule': 'password',
            'data-msg': 'Please enter your password',
            'id': 'account_password'
        }),
        required=False
    )


    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'country', 'address', 'city', 'state', 'zip_code', 'phone', 'email', 'order_notes', 'password', ]

    def clean(self):
        cleaned_data = super().clean()
        create_account = self.cleaned_data.get('create_account')

        if create_account:
            if not cleaned_data.get('password'):
                self.add_error('password', 'Password is required when creating an account.')

        return cleaned_data

