from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import UserRegisterForm


def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'authentication/profile.html', {'title':'Profile'})


def register(request):
    form = "Dummy String"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, f'Account with username {user} successfully created')
            return HttpResponseRedirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'title':'register','form':form})

def edit_profile(request):
    form = UserChangeForm()
    return render(request, 'authentication/edit_profile.html',{'form':form})