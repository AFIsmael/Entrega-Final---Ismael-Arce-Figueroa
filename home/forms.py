from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from home.models import Avatar

class UserRegisterForm(UserCreationForm):

     email = forms.EmailField(
         label= 'Email',
         required=True,
     )
     username = forms.CharField(
         label = 'Username',
         required=True,
     )
     password1 = forms.CharField(
         label = "Password",
         required=True,
         widget=forms.PasswordInput,
     )
     password2 = forms.CharField(
         label = "Confirm password",
         required=True,
         widget=forms.PasswordInput,
    )
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        widgets = {
            "email": forms.TextInput(attrs={"readonly": "readonly"}),
        }


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("image", )
        