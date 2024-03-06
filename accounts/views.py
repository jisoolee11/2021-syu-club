from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home1'))
            else:
                messages.error(request, "ID 또는 Password가 잘못되었습니다.")
                return redirect(reverse('home1'))
        else:
            messages.error(request, "ID 또는 Password가 잘못되었습니다.")
            return redirect(reverse('home1'))
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})
        

def user_logout(request):
    logout(request)
    return redirect(reverse('home1'))