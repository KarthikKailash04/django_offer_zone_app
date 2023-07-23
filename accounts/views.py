from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms2 import RegistrationFormS
 
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

import requests


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            pin_code=form.cleaned_data['pin_code']

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, pin_code=pin_code,username=username, password=password)
            user.phone_number = phone_number
            user.save()
          
            return redirect('login')

           
            

            
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
def registerS(request):
    if request.method == 'POST':
        form = RegistrationFormS(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            shop_address=form.cleaned_data['Shop_Address']
            pin_code=form.cleaned_data['pin_code']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_Shop_Owner(first_name=first_name, last_name=last_name, email=email, username=username, Shop_Address=shop_address,pin_code=pin_code,password=password)
            user.phone_number = phone_number
            user.save()
            #user activation mail
           
            return redirect('login')
    else:
        form = RegistrationFormS()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register2.html', context)

def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            print("Email:", email)  # Debug statement
            print("Password:", password)
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                 auth.login(request, user)
                 return redirect('home')     
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')           


        return render(request,'accounts/login.html')
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')
