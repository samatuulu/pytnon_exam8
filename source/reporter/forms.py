from django import forms

from reporter.models import Review


class ReviewProductForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['feedback']