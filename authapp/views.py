from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from authapp.forms import *
from .ldapauth import main as ldaptest
import testldap.settings as set
from django_auth_ldap.backend import LDAPBackend

def login(request):
    login_form = UserForm(data=request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        #auth = LDAPBackend()

        user = auth.authenticate(request, username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))




def main(request):
    #y = ldaptest()
    #var = set.AUTH_LDAP_BIND_PASSWORD
    #print(var)
    #u = main1()
    #print(y)
    #print(u)
    return render(request, 'authapp/index.html')