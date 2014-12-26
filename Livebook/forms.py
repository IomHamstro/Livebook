# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from Livebook.models import UserProfile


class LoginForm(Form):
    login = forms.CharField(initial='login')
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
            'password': forms.PasswordInput(),
        }


#
# class RegistrationForm(forms.Form):
#     login = forms.CharField(label='Логин')
#     email = forms.EmailField(label='Почта')
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#     name = forms.CharField(label='Имя')
#     surname = forms.CharField(label='Фамилия')
#     # birthday = forms.DateField()
#     address = forms.CharField(label='Адрес')
#     # information = forms.CharField()
#     hobby = forms.CharField(label='Хобби')
#     # avatar = forms.ImageField()

class RegistrationProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email',  'birthday']


class RegistrationUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',  'password']