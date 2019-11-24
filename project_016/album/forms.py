from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text  = forms.CharField(widget = forms.Textarea, required=False)
