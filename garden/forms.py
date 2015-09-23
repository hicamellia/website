# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django import forms
from models import *


class PasswordForm(forms.Form):
    email = forms.CharField(required=False)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm = forms.CharField(required=True, widget=forms.PasswordInput)
    origin = forms.CharField(required=False, widget=forms.PasswordInput)

    def clean_confirm(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm:
            if password != confirm:
                raise forms.ValidationError("验证密码不一致")
        return confirm

    def clean_origin(self):
        email = self.cleaned_data.get("email")
        origin = self.cleaned_data.get("origin")

        if origin and email:
            user = authenticate(username=email, password=origin)
            if user is None:
                raise forms.ValidationError("原密码不正确")
        return origin

class EmailForm(forms.Form):
    origin = forms.EmailField(required=False)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    first_name = forms.CharField(required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        origin = self.cleaned_data.get('origin')
        if origin and email == origin:
            return email
        user = User.objects.filter(username=email, email=email)
        if len(user) != 0:
            raise forms.ValidationError("该邮箱已被注册")
        return email