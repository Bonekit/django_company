from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignInForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def sign_in(request):
    title = 'Account | SignIn'
    template_name = 'account/login.html'

    # If the user is logged in, he should be redirected to the main page
    if request.user.is_authenticated:
        return redirect('main:index')

    # Login
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "Login was successfully")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:index')
        else:
            messages.error(request, "Login was not successfully")
            return render(request, template_name, {'login_form': form, 'page_title': title})
    else:
        form = SignInForm()
    return render(request, template_name, {'login_form': form, 'page_title': title})


def sign_up(request):
    title = 'Account | SignUp'
    template_name = 'account/registration.html'

    # If the user is logged in, he should be redirected to the main page
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in")
        return redirect('main:index')

    # Register
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('main:index')
        else:
            messages.error(request, "Registration failed")
            return render(request, template_name, {'registration_form': form, 'page_title': title})
    else:
        form = SignUpForm()
    return render(request, template_name, {'registration_form': form, 'page_title': title})


@login_required(login_url='account:login')
def sign_out(request):
    logout(request)
    return redirect('main:index')
