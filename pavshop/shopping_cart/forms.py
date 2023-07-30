from django import forms
from .models import Shipping_address, Billing_address


from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from phonenumber_field.phonenumber import PhoneNumber
from django_countries.fields import CountryField


from django.contrib.auth import get_user_model

User = get_user_model()


class Shipping_addressForm(forms.ModelForm):

    class Meta:
        model = Shipping_address

        fields = (
            # 'first_name',
            # 'last_name',
            
            'company',
            'address',
            'country',
            'city',
            # 'email',
            'phone',

        )


        widgets = {
            # 'first_name' : forms.TextInput(attrs={
            #     'placeholder' : 'first-name'
            # }),
            # 'last_name' : forms.TextInput(attrs={
            #     'placeholder' : 'last-name'
            # }),
            'company': forms.TextInput(attrs={
                'placeholder' : 'company'
            }),
            'address' : forms.TextInput(attrs={
                'placeholder' : 'address'
            }),
            
            'city' : forms.TextInput(attrs={
                'placeholder' : 'CITY'
            })
            # 'email' : forms.EmailInput(attrs={
            #     'placeholder' : 'EMAIL'
            # })
            

        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Email should be gmail.com')
        return email



    phone = PhoneNumberField(
        region='AZ',
        widget=PhoneNumberPrefixWidget(initial=''),
        required=False,
    )
    
    country = CountryField(blank_label="(select country)")





class Billing_addressForm(forms.ModelForm):

    class Meta:
        model = Billing_address

        fields = (
            # 'first_name',
            # 'last_name',
            
            'company',
            'address',
            'country',
            'city',
            # 'email',
            'phone',

        )


        widgets = {
            # 'first_name' : forms.TextInput(attrs={
            #     'placeholder' : 'first-name'
            # }),
            # 'last_name' : forms.TextInput(attrs={
            #     'placeholder' : 'last-name'
            # }),
            'company': forms.TextInput(attrs={
                'placeholder' : 'company'
            }),
            'address' : forms.TextInput(attrs={
                'placeholder' : 'address'
            }),
            
            'city' : forms.TextInput(attrs={
                'placeholder' : 'CITY'
            })
            # 'email' : forms.EmailInput(attrs={
            #     'placeholder' : 'EMAIL'
            # })
            

        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Email should be gmail.com')
        return email

        

    phone = PhoneNumberField(
        region='AZ',
        widget=PhoneNumberPrefixWidget(initial=''),
        required=False,
    )
    
    country = CountryField(blank_label="(select country)")
