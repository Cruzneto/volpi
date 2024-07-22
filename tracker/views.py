from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User, WaterIntake
from django import forms
from datetime import date
from django.db.models import Sum
from django.views.decorators.http import require_POST


class RegisterForm(UserCreationForm):
    weight = forms.FloatField()

    class Meta:
        model = User
        fields = ['username', 'weight', 'password1', 'password2']

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'tracker/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    user = request.user
    recommended_water = user.weight * 35  # Recommended water intake in ml based on weight
    today_intake = WaterIntake.objects.filter(user=user, date=date.today()).aggregate(Sum('amount'))['amount__sum'] or 0
    remaining_water = recommended_water - today_intake
    return render(request, 'tracker/index.html', {
        'recommended_water': recommended_water,
        'today_intake': today_intake,
        'remaining_water': remaining_water,
    })

@login_required
def add_intake(request, amount):
    WaterIntake.objects.create(user=request.user, amount=amount)
    return redirect('index')


@login_required
def history(request):
    user = request.user
    history = WaterIntake.objects.filter(user=user).order_by('-date')
    return render(request, 'tracker/history.html', {'history': history})


