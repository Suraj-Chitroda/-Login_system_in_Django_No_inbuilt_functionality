from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.base_user import make_password, check_password
from . import models
# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def logout(request):
    request.session.clear()
    return HttpResponseRedirect('login')


def home(request):
    if request.session.has_key('username'):
        if request.session['username'] is not None:
            log_user = models.Login_user.getUser(request.session['username'])
            return render(request, 'user/logged.html', context={'user': log_user})
        else:
            return redirect('login')
    else:
        return redirect('login')


def loginme(request):
    if request.method != 'POST':
        if request.session.has_key('username') and request.session['username'] is not None:

            return HttpResponseRedirect('home')
        else:
            return render(request, 'user/login.html')
    else:
        if request.session.has_key('username') and request.session['username'] is not None:

            return HttpResponseRedirect('home')
        else:
            context = {}

            username = request.POST['username']
            password = request.POST['password']
            user = models.Login_user.getUser(username)

            if user:
                if check_password(password, user.password):
                    request.session['username'] = user.username
                    return HttpResponseRedirect('home')
                else:
                    context = {
                        'status': 'Username or Password Incorrect'}

            else:
                context = {'status': 'Login unsuccessfull'}

            return render(request, 'user/login.html', context=context)


def register(request):

    if request.method != 'POST':
        if request.session.has_key('username') and request.session['username'] is not None:

            return HttpResponseRedirect('home')
        else:
            return render(request, 'user/register.html')

    else:
        if request.session.has_key('username') and request.session['username'] is not None:

            return HttpResponseRedirect('home')
        else:
            context = {}
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            username = request.POST['username']
            password = request.POST['password']

            if username.isspace():
                context = {'status': 'Username should not contain space'}
            else:

                if models.Login_user.getUser(username):
                    context = {
                        'status': 'Username already taken'}
                else:
                    reg = models.Login_user(
                        name=name,
                        password=make_password(password),
                        email=email,
                        phone=phone,
                        username=username
                    )
                    try:
                        reg.save()
                        context = {
                            'status': 'New user was successfully registered'}
                    except:
                        context = {
                            'status': 'User not registered, data not valid'}

            return render(request, 'user/register.html', context=context)
