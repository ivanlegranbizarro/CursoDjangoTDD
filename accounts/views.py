from django.shortcuts import render

from .forms import UserRegistrationForm

# Create your views here.


def signup(request):
    form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
