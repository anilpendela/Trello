from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
import re
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
               widget= forms.TextInput
               (attrs=
               	{'class':'form-control',
				'id':'username',
				'placeholder': 'User Name',
				}))
    password = forms.CharField(max_length=100,
               widget=forms.PasswordInput
               (attrs=
               	{'class':'form-control',
				'id':'password',
				'placeholder': 'Password',
				}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Please enter valid Username & Password")
        return self.cleaned_data

class DummyForm(forms.Form):
  pass

class SignupForm(forms.Form):
    username = forms.CharField(max_length=20,
               widget= forms.TextInput
               (attrs=
                {'class':'form-control',
                'id':'username',
                'placeholder': 'User Name',
                }))
    email_id = forms.EmailField(max_length=64,
               widget= forms.EmailInput
               (attrs=
                {'class':'form-control',
                'id':'email_id',
                'placeholder': 'Email ID',
                }))
    password = forms.CharField(max_length=20,
               widget=forms.PasswordInput
               (attrs=
                {'class':'form-control',
                'id':'password',
                'placeholder': 'Password',
                }))
    reenter_password = forms.CharField(max_length=20,
               widget=forms.PasswordInput
               (attrs=
                {'class':'form-control',
                'id':'reenter_password',
                'placeholder': 'Re-Enter Password',
                }))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except Exception:
            user = None
        if user is not None:
            raise ValidationError("Username Already Exists.")
        return username

    def clean_reenter_password(self):
        password = self.cleaned_data['password']
        reenter_password = self.cleaned_data['reenter_password']
        if password != reenter_password:
            raise ValidationError("Password and Re-Enter didn't match")

        return reenter_password

    def save(self):
        user = User()
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email_id']
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user