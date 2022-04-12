from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm)
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

from .forms import CustomUserChangeForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles/index.html')
    if request.method == 'POST':
        # form = AuthenticationForm(request, data=request.POST)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        pass
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        # PasswordChangeForm의 첫번째는 user를 넣어주세요
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)