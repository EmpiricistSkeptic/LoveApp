from django import forms
from .models import Answer

class LinkProfileForm(forms.Form):
    unique_code = forms.UUIDField(label='Partner Unique Code')


class AnswerForm(forms.Form):
    class Meta:
        model = Answer
        fields = ['text']
