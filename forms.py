from django import forms
from django.forms import ModelForm
from feedb.models import Customer
# Create your views here.

class FeedbackForm(ModelForm):

    class Meta:
        model=Customer
        exclude=['company']
