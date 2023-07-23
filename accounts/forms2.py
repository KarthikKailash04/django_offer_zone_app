from django import forms
from .models import Account


class RegistrationFormS(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password','Shop_Address','pin_code']


    def __init__(self, *args, **kwargs):
        super(RegistrationFormS, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['Shop_Address'].widget.attrs['placeholder'] = 'Enter Shop Address'
        self.fields['pin_code'].widget.attrs['placeholder'] = 'Pin Code'


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'