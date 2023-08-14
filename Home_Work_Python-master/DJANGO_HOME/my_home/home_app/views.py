from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .forms import MyForm, UserLoginForm
from .models import HtmlCard


def get_basic(request):
    html_card = HtmlCard.objects.all()
    context = {'html_card': html_card}
    return render(request, 'basic.html', context)


def after_register(request):
    template_name = 'register.html'
    return render(request, template_name)


def register(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'rrgister_after.html', {'form': form})

    else:
        form = MyForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.user = request.user
            new_user.save()
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect('home_app:base')
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('home_app:base')





def page_one(request):
    template_name = 'page_one.html'
    return render(request, template_name)


def page_second(request):
    template_name = 'page_second.html'
    return render(request, template_name)
