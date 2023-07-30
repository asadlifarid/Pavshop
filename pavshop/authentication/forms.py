from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect

from base.validators import ValidationError

from django.contrib.auth import get_user_model

# Generic Login View
from django.contrib.auth.forms import AuthenticationForm, UsernameField

User = get_user_model()


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',

    }))


    class Meta:
        model = User

        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'image',

        )
        
        widgets = {
            'password' : forms.PasswordInput(attrs={
                'placeholder' : 'Password'
            })

        }
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")
        # elif password == confirm_password:
        #     print('Successssss')
        #     return redirect('success_page')
        return super().clean()


    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Email must be gmail.com')
        return email


    def save(self, commit):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])  # hash'ledikden sonra save etsin formu
        user.is_active = False
        # return user.save()
        user.save()
        return user





# login formun save olunma xususiyyeti olamli deyil, ona gore modelform'dan inherit almiriq
class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder':'Username',
    }))

    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
    }))

    
   
   




# function-based Login view
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
#         'placeholder':'Username',
#     }))

#     password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={
#         'placeholder':'Password',
#     }))
