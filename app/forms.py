from django import forms
from .models import Article, BlogComment, Suggest


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name', 'body']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your User name',
                'aria-describedby': 'sizing-addon1',
            }),
            'body': forms.Textarea(attrs={'placeholder': 'Comments',
                                          'class': 'form-control',
                                          'rows': 4,
                                          }),
        }


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        fields = ['suggest']
        widgets = {
            'suggest': forms.Textarea(attrs={
                'placeholder': 'suggestions',
                'class': 'form-control',
                'rows': 4,
                'cols': 80,
                })
        }



