from django import forms
from .models import TrackedProduct

class TrackProductForm(forms.ModelForm):
    class Meta:
        model = TrackedProduct
        fields = ['product_url']