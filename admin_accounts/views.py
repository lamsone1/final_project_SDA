from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from utils.models import Box


class AdminLoginView(LoginView):
    template_name = 'form.html'


class AdminPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('utils')


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('utils')


