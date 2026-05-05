from django import forms
from hello.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message',]