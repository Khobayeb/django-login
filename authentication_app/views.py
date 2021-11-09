from django.shortcuts import render,  HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

# Create your views here.


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)

            return HttpResponseRedirect(reverse('login'))

    dict = {'form': form}
    return render(request, 'signup.html', context=dict)



def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
