from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user_app.forms import UserForm, SignupForm, LoginForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
                )
    else:
        form = SignupForm
    dataums = {'form': form}
    return render(request, 'signup.html', dataums)

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/admin')
                else:
                    return redirect('/secret')
    else:
        form = LoginForm
    dataum = {'form': form}
    return render(request, 'login.html', dataum)


@login_required
def special_page(request):
    data = {}
    return render(request, "special.html", data)
