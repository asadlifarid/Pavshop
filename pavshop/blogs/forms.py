from django import forms
from .models import Comment, Story
from ckeditor.widgets import CKEditorWidget

from django.contrib.auth import get_user_model


User = get_user_model()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = __all__
        fields = (
            # 'name',
            # 'email',
            # 'subject',
            'message',

        )
        
        widgets = {
            # 'name' : forms.TextInput(attrs={
            #     'class' : 'form-control',
            #     'placeholder' : ''
            # }),
            # 'email' : forms.EmailInput(attrs={
            #     'class' : 'form-control',
            #     'placeholder' : ''
            # }),
            # 'subject' : forms.TextInput(attrs={
            #     'class' : 'form-control',
            #     'placeholder' : ''
            # }),
            'message': forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : ''
            })
        }
    






class CreateStoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        fields = ('title', 
                  'description', 
                  'category', 
                #   'author', 
                  'image', 
                  'is_archive', 
                  'content',
                  'tag'
                #   'slug',
        )
        # exclude = ('slug', 'is_archive', )

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : ''
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : ''
            }),
            'image' : forms.FileInput,

            'content' : forms.Textarea(attrs={
                'class' : 'form-control w-100',
                'placeholder' : ''
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control'
            }),
            'tag' : forms.SelectMultiple(attrs={
                'class' : 'form-control'
            })
        }




# class UpdateStoryForm(forms.ModelForm):
#     edit_story = forms.BooleanField(widget=forms.HiddenInput, initial=True)


#     class Meta:
#         model = Story
#         fields = ('title', 
#                   'content'
#         )




# class DeleteStoryForm(forms.Form):
#     delete_story = forms.BooleanField(widget=forms.HiddenInput, initial=True)
