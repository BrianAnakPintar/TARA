from django import forms
from teacherRater.models import reviews, understandabilityChoices, communicationChoices, teachingMethodChoices

class ratingForms(forms.ModelForm):
    commentsReview = forms.CharField(widget=forms.Textarea, required=False)
    understandability = forms.ChoiceField(choices=understandabilityChoices, widget=forms.Select(), required=True)
    communication = forms.ChoiceField(choices=communicationChoices, widget=forms.Select(), required=True)
    teachingMethod = forms.ChoiceField(choices=teachingMethodChoices, widget=forms.Select(), required=True)
    makeAnonymous = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    class Meta:
        model = reviews
        fields = ['commentsReview', 'understandability', 'communication', 'teachingMethod', 'makeAnonymous']