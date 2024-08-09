from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_title','review_content','rating',)
        widgets = {
            'review_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your review title'}),
            'review_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),}