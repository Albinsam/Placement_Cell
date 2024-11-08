from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_name', 'resume', 'cover_letter_text', 'cover_letter_file']
        widgets = {
            'job_name': forms.TextInput(attrs={'placeholder': 'Enter Job Name'}),
            'cover_letter_text': forms.Textarea(attrs={'placeholder': 'Write your cover letter here...'}),
        }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)