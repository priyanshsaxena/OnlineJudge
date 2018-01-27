from django import forms

class SubmissionForm(forms.Form):
    #title = forms.CharField(max_length=50)
    filename = forms.FileField(label='Upload your code')