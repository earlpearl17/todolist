from django import forms
from datetime import date
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        #fields = ('title', 'due_date', 'description', 'done')
        fields = '__all__'
        labels = {
            'done': 'Is this task done?',
        }
        help_texts = {
            'due_date': 'Date when task is expected to be done.'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        words = title.split(' ')
        if len(words) > 5:
            raise forms.ValidationError('The title should be five words or less.')
        return title

    def clean(self):
        cleaned_data = self.cleaned_data # individual field's clean methods have already been called
        done = cleaned_data.get("done")
        due_date = cleaned_data.get("due_date")
        if not done and due_date < date.today():
            raise forms.ValidationError('The due date cannot be in the past.')
        return cleaned_data
