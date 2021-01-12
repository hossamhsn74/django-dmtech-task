from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect



def signup_view(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# def login_view(request):
#     form = LoginForm(request.POST or None)
#     if request.POST and form.is_valid():
#         user = form.login(request)
#         if user:
#             login(request, user)
#             return HttpResponseRedirect('home') #Redirect to a success page.
#     return render(request, 'registration/login.html', {'login_form': form })