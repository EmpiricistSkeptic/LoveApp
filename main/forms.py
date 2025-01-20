from django import forms

class LinkProfileForm(forms.Form):
    unique_code = forms.UUIDField(label='Partner Unique Code')