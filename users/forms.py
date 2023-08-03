from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Model that form will work with automatically
    class Meta:
        model = User # model that will be affected
        fields = ['username', 'email', 'password1', 'password2'] # fields we want in the form and their order


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Model that form will work with automatically
    class Meta:
        model = User # model that will be affected
        fields = ['username', 'email'] # fields we want in the form and their order


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']