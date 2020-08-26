from django import forms


class InputDataForm(forms.Form):
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    user_name   = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"this is a word"}))
    password    = forms.CharField(widget=forms.PasswordInput)
    email       = forms.EmailField()