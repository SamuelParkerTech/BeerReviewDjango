from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Creates choices for 1 to 5

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control dropdown-arrow'})
    )
    class Meta:
        model = Review
        fields = ('review_title','review_content','rating',)
        widgets = {
            'review_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your review title'}),
            'review_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here'}),
        }