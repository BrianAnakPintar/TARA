from django import forms
from teacherRater.models import reviews, RatingChoices

class ratingForms(forms.ModelForm):
    commentsReview = forms.CharField(widget=forms.Textarea, required=False)
    rate = forms.ChoiceField(choices=RatingChoices, widget=forms.Select(), required=True)
    makeAnonymous = forms.BooleanField(widget=forms.CheckboxInput)
    class Meta:
        model = reviews
        fields = ['commentsReview', 'rate', 'makeAnonymous']