from django import forms
from blog.models import Comment,Contact

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['post','name','email','subject','message']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','subject','message']
