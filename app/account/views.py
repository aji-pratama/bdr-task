from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

def  dashboard(request):
    if request.user.is_authenticated and request.user.is_atasan:
        return render(request, 'atasan/index_atasan.html')

    if request.user.is_authenticated and not request.user.is_atasan:
        return render(request, 'staff/index_staff.html')

    return HttpResponseRedirect('/login')

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')
    template_name = 'account/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogOutView(generic.RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
