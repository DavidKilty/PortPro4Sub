from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import TipperSignUpForm, TippeeSignUpForm
from .models import User
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'index.html')

def logintipper(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting login: {username}, {password}")  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Login failed")
            return render(request, 'logintipper.html', {'error': 'Invalid username or password'})
    return render(request, 'logintipper.html')

def logintippee(request):
    return render(request, 'logintippee.html') 

def signuptipper(request):
    if request.method == 'POST':
        form = TipperSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User saved: {user.username}, {user.email}, {user.password}")
            return redirect('home')
        else:
            print("Form errors:", form.errors)
    else:
        form = TipperSignUpForm()
    return render(request, 'signuptipper.html', {'form': form})

def signuptippee(request):
    if request.method == 'POST':
        form = TippeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"Tippee account created: {user.username}, {user.email}")
            return redirect('home')
        else:
            print("Form errors:", form.errors)
    else:
        form = TippeeSignUpForm()
    return render(request, 'signuptippee.html', {'form': form})

class TipperDeleteView(DeleteView):
    model = User
    template_name = 'tipper_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return User.objects.filter(user_type='tipper')
