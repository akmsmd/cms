from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'register/register.html', context)

def home(request):
    return render(request, 'register/home.html')
