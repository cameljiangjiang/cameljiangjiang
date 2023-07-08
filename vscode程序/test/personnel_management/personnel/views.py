from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegistrationForm, UserAppendForm
from .models import Profile

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
#            user = form.cleaned_data['user']
            auth.login(request, user) 
            return redirect('user_list')  # 登录成功后重定向到个人资料页面
    else:
        form = LoginForm()
    return render(request, 'personnel/login.html', {'form': form})
# def login(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             user = login_form.cleaned_data['user']
#             auth.login(request, user)
#             return redirect(request.GET.get('from', reverse('user_list')))
#     else:
#         login_form = LoginForm()

#     context = {}
#     context['login_form'] = login_form
#     return render(request, 'personnel/login.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 注册成功后重定向到登录页面
    else:
        form = RegistrationForm()
    return render(request, 'personnel/register.html', {'form': form})
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             messages.success(request, f'Account created for {username}. You can now login.')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'personnel/register.html', {'form': form})

# @login_required
# def view_profile(request):
#     user = request.user
#     profile = user.profile  # 假设Profile模型有一个与User模型的OneToOneField关联的字段
#     return render(request, 'personnel/view_profile.html', {'user': user, 'profile': profile})

def user_list(request):
    users = User.objects.all()
    context = {}
    context['users'] = users
    return render(request, 'personnel/user_list.html', context)
@login_required
def edit_profile(request):
    user = request.user
def append_user(request):
    usr = request.user
    if usr.is_authenticated:
        if request.method == 'POST':
            usermodify_form = UserAppendForm(request.POST)
            if usermodify_form.is_valid():
                username = usermodify_form.cleaned_data['username']
                password = usermodify_form.cleaned_data['password']

                print(usermodify_form.cleaned_data['type'])
                if usermodify_form.cleaned_data['type'] == '经理':
                    add = User.objects.create_superuser(username,'', password)
                else:
                    add = User.objects.create_user(username, '',password)
                add.save()
                add.email = str(add.pk) + '@163.com'
                add.save()
                staff_type = usermodify_form.cleaned_data['type']
                staff_gender = usermodify_form.cleaned_data['gender']
                staff_age = usermodify_form.cleaned_data['age']
                home = usermodify_form.cleaned_data['home']
                staff_nationality = usermodify_form.cleaned_data['nationality']
                staff_tel = usermodify_form.cleaned_data['phone']
                id_card = usermodify_form.cleaned_data['id_card']
                salary_pre_hour = usermodify_form.cleaned_data['salary_pre_hour']
                add1 = Profile(user=add, staff_type=staff_type, staff_gender=staff_gender, staff_age=staff_age, staff_home=home,
                               staff_nationality=staff_nationality, staff_tel=staff_tel, id_card=id_card,
                               salary_pre_hour=salary_pre_hour)
                add1.save()
                return redirect(reverse('regiser'))
        usermodify_form = UserAppendForm()
        context = {}
        context['usermodify_form'] = usermodify_form
        return render(request, 'personnel/append_user.html', context)
    else:
        return redirect(reverse('login'))
