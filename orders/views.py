from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if request.user.is_authenticated :
        print('authenticated')
        return render(request, 'orders/index.html')
    else:
        print('not authenticated')
        return render(request, 'orders/index.html')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None :
        login(request, user)
        print('authenticated')
        # context = {
        #     'user' : user,
        #     'status' : 'Authenticated'
        # }
        messages.success(request, "Logged in Successfully")
        return redirect('orders_index')
        #return render(request, 'orders/index.html', context=context)
    else:
        messages.error(request, " Invalid credentials")
        print('not authenticated')
        return redirect('orders_index')
        #return render(request, 'orders/index.html')

def blog(request):
    return render(request, 'orders/blog.html')

def menu(request):
    return render(request, 'orders/menu.html')

def services(request):
    return render(request, 'orders/services.html')

def about(request):
    return render(request, 'orders/about.html')

def contact(request):
    return render(request, 'orders/contact.html')

def contactSubmitted(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        messages.success(request, f'Thanks {fullname} for contacting Harish Ahuja')
    return HttpResponseRedirect(reverse('orders_index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('orders_index'))

def signup(request):
    if request.POST :
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username=username,email=email)
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            # context = {
            #     'user' : user,
            #     'status' : 'Authenticated'
            # }
            messages.success(request, f'Welcome {first_name}')
        except :
            messages.error(request, f'Login Faield Username {username} already taken')

    return HttpResponseRedirect(reverse('orders_index'))
        #return render(request, 'orders/index.html', context=context)
