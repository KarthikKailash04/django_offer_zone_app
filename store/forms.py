from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from datetime import timedelta,datetime

class offerform(forms.ModelForm):
    starting_date = forms.DateTimeField(
        label="Starting Date",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=datetime.now().replace(second=0, microsecond=0)
    )
    ending_date = forms.DateTimeField(
        label="Starting Date",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=datetime.now().replace(second=0, microsecond=0)
    )
    def clean(self):
        cleaned_data = super().clean()
        starting_date = cleaned_data.get("starting_date")
        ending_date = cleaned_data.get("ending_date")

        if starting_date and ending_date:
            if starting_date > ending_date:
                raise ValidationError("The ending date must be after the starting date.")
            if ending_date - starting_date < timedelta(days=1):
                raise ValidationError("The ending date must be at least one day after the starting date.")

        return cleaned_data

    class Meta:
        model = Product
        fields = ['offer','images','discription','category','offer_shop_pincode','starting_date','ending_date','offer_percent','offer_shop_name','offer_shop_address','number','alt_number']
    def __init__(self, *args, **kwargs):
        super(offerform, self).__init__(*args, **kwargs)
        """self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'"""
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
