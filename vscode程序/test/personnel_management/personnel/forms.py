from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

from .models import Position, Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'})
    )
    password1 = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )
    password2 = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请确认密码'})
    )
class UserAppendForm(forms.Form):
    ps = Position.objects.all()
    posit = []
    for p in ps:
        posit.append((p.position, p.position))
    username = forms.CharField(
        label='姓名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入姓名'})
    )
    type = forms.CharField(
        label='职位',
        widget=forms.Select(choices=posit),
    )
    gender = forms.ChoiceField(
        label='性别',
        initial='male',
        widget=widgets.RadioSelect,
        choices=(('male','男'),('female','女'))
    )
    age = forms.CharField(
        label='年龄',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入年龄'})
    )
    home = forms.CharField(
        label='籍贯',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入籍贯'})
    )
    nationality = forms.CharField(
        label='民族',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入民族'})
    )
    phone = forms.CharField(
        label='电话',
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入11位电话'}),
    )
    id_card = forms.CharField(
        label='身份证号',
        max_length=18,
        min_length=18,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入18位身份证号'})
    )
    salary_pre_hour = forms.CharField(
        label='时薪',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入时薪'})
    )
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))