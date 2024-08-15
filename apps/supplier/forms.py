# forms.py
from django import forms

class SupplierForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'supplier_name',
        })
    )
    
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'aria-describedby': 'emailHelp',
        })
    )
    
    phone = forms.CharField(
        label='Phone number',
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone',
        })
    )
    
    address = forms.CharField(
        label='Address',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'address',
        })
    )
    
    products = forms.CharField(
        label='Products',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'products',
        })
    )
