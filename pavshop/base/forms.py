from django import forms
from .models import Newsletter, Contact

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from phonenumber_field.phonenumber import PhoneNumber


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        # fields = '__all__'
        fields = (
            'email',
            # 'is_active',
        )

        widgets = {
            'email' : forms.EmailInput(attrs={
                'placeholder' : "Enter your email address"
            })
        }

     
    def clean_email(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError("Email must be gmail.com :)")
        return value



 


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = '__all__'
        fields = (
            'full_name',
            'email',
            'phone',
            'subject',
            'message',
            
        )

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : ''
                # 'name' : 'full_name'
            }),

            'email': forms.EmailInput(attrs={
                'class' : 'form-control',
                'type' : 'email',
                'placeholder' : ''
                # 'name' : 'email'
            }),

            # 'phone': PhoneNumberField(attrs={
            #     'class' : 'form-control',
            #     'placeholder' : '123-45-678',
            #     'name' : 'phone',
            #     'pattern': "[0-9]{3}-[0-9]{2}-[0-9]{3}"
            # }),


            'subject': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : ''
                # 'name' : 'subject'

            }),

            'message': forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : ''
                # 'name' : 'message'

            })


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


