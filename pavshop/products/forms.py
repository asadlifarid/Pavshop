from django import forms
from .models import Review

from django.contrib.auth import get_user_model


User = get_user_model()


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # fields = __all__
        fields = (
            # 'name',
            # 'email',
            'review',
            'rating'

        )
        
        widgets = {
            # 'name' : forms.TextInput(attrs={
            #     'placeholder' : 'Write your name'
            # }),
            # 'email' : forms.EmailInput(attrs={
            #     'placeholder' : 'Write your email'
            # }),
            'review': forms.Textarea(attrs={
                'placeholder' : 'Write your review here'
            })
        }
    
