from django import forms

from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from . models import *



class SignupForm(UserCreationForm):

    class Meta:
       model = User
       fields = ['first_name', 'last_name' , 'username', 'email' , 'password1' , 'password2']




class UserForm_Edit(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name' , 'email' ]


class ProfileForm_Edit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone' , 'city' , 'img' , 'bio']
