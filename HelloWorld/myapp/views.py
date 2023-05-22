from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm, CarForm
from .models import Car

def home(request):
    return render(request, 'myapp/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('car_list')
    return render(request, 'myapp/login.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'myapp/register.html', {'form': form})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'myapp/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'myapp/car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'myapp/add_car.html', {'form': form})

def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'myapp/edit_car.html', {'form': form})
