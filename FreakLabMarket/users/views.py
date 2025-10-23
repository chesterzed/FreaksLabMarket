from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm, ProfileForm


def login(request):
    # form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
         'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'registration',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        print("Form errors:", form.errors)
        print("Non-field errors:", form.non_field_errors())
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'profile',
        'form': form,
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:home'))


