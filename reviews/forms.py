from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {
            "title",
            "location",
            "grade",
            "companion",
            "content",            
            "image",
        }