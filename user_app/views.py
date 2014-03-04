from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user_app.forms import UserForm, SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.save():
                user = User.objects.create_user(
                    form.cleaned_data["username"],
                    form.cleaned_data["email"],
                    form.cleaned_data["password"],
                )
    else:
        form = SignupForm
    dataums = {'form': form}
    return render(request, 'signup.html', dataums)