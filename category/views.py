from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


class LoginView(FormView): 
    form_class = LoginForm
    template_name = "login.html"
    success_url ="/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


class HomePageView(LoginRequiredMixin, FormView):
    form_class = DummyForm
    template_name = "home.html"
    success_url ="/"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        return kwargs

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_success_url())


class Signup(FormView):
    form_class = SignupForm
    template_name = "signup.html"
    success_url = "/login/"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        return kwargs

    def form_valid(self, form):
        user_obj = form.save()
        return super(Signup, self).form_valid(form)