from django import forms
from .models import Answer, Question, Profile
from django.core.exceptions import ValidationError

class LinkProfileForm(forms.Form):
    unique_code = forms.UUIDField(label='Partner Unique Code')


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)

        if question.question_type == 'text':
            self.fields['answer'] = forms.CharField(
                widget=forms.Textarea,
                label='Your answer'
            )
        else:
            self.fields['answers'] = forms.ModelChoiceField(
                queryset=Answer.objects.filter(question=question),
                widget=forms.RadioSelect if question.question_type == 'single' else forms.CheckboxSelectMultiple,
                label='Choose an answer'
            )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'bio', 'mood']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'mood': forms.TextInput()
        }
        labels = {
            'picture': 'Profile Photo',
            'bio': 'About Me',
            'mood': 'Current Mood'
        }

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > 500:
            raise ValidationError("Bio cannot exceed 500 characters")
        return bio
    
    def clean_mood(self):
        mood = self.cleaned_data.get('mood')
        if len(mood) > 100:  # Пример ограничения длины
            raise ValidationError("Mood cannot exceed 100 characters")
        return mood
