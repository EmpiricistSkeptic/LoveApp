from django import forms
from .models import Answer, Question

class LinkProfileForm(forms.Form):
    unique_code = forms.UUIDField(label='Partner Unique Code')


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)

        if question.question_type == 'text':
            self.fields['answer'] = forms.CharField(
                widget=forms.Textarea,
                label='Ваш ответ'
            )
        else:
            self.fields['answers'] = forms.ModelChoiceField(
                queryset=Answer.objects.filter(question=question),
                widget=forms.RadioSelect if question.question_type == 'single' else forms.CheckboxSelectMultiple,
                label='Выберите ответ'
            )
