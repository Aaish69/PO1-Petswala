from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView
from .models import User, Vendor
from .form import UserSignUpForm, VendorSignUpForm
from django.contrib import messages

# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')


class user_register(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'accounts/user_register.html'

    def validation(self, form, request):
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created successfully for {username}!')
        login(self.request, user)
        return redirect('login')

class vendor_register(CreateView):
    model = Vendor
    form_class = VendorSignUpForm
    template_name = 'accounts/vendor_register.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')