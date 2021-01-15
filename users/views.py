from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.http import request


class signUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return super().form_valid(form)
