from django import forms
# from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ValidationError
from Profile.models import User_Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        

        if not user.first_name:
            raise ValidationError('Please enter firstname')

        if commit:
            user.save()
        return user

class EditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'email',
                # 'password'
        ]
class EditUserDetail(forms.ModelForm):
    class Meta:
        model=User_Profile
        fields = [
            'language',
            'picture',
        ]

