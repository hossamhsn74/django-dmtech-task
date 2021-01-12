from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate, login



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'user_type')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'user_type')



# class LoginForm(forms.Form):
#     email = forms.EmailField(max_length=255, required=True)

#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#         user = authenticate(email=email, password=password)
#         if not user or not user.is_active:
#             raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
#         return self.cleaned_data

#     def login(self, request):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#         user = authenticate(email=email, password=password)
#         return user