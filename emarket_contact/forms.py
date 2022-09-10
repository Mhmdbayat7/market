from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی را وارد کنید', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(limit_value=150, message='تعداد کارکتر بیشتر از 150 است')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل را وارد کنید', 'class': 'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(limit_value=100, message='تعداد کارکتر بیشتر از 100 است')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان خود را وارد کنید', 'class': 'form-control'}),
        label='عنوان',
        validators=[
            validators.MaxLengthValidator(200, 'عنوان پیام بیشتر از 200 کارکتر نباشد')
        ]
    )

    text = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'متن پیام را وارد کنید', 'class': 'form-control', 'row': 8}),
        label='متن پیام'
    )