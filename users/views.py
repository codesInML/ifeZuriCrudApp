from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'You can now log in to your account!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})