from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegistrationForm

# Create your views here.


def signup(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("accounts:login")

    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            return redirect("posts:home")
    else:
        form = AuthenticationForm()

    context = {"form": form}

    return render(request, "accounts/login.html", context)
