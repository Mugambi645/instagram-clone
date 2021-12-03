from django import forms
#import comment model
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Class to create a form instance of the comment model
    """
    class Meta:
        """
        Meta class to define the behavior of the class
        """
        model = Comment
        fields = ['description']