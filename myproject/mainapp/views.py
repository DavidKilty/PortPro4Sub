from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import TipperSignUpForm, TippeeSignUpForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
            if user.user_type == 'tipper':
                return redirect('tipper_homepage')
            elif user.user_type == 'tippee':
                return redirect('tippee_homepage')
        else:
            return render(request, 'logintipper.html', {'error': 'Invalid email or password'})
    return render(request, 'logintipper.html')


@login_required
def tipper_homepage(request):
    return render(request, 'tipperhomepage.html', {'tipper': request.user})


def logintippee(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting login: {username}, {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'tippee':
            login(request, user)
            return redirect('tippee_homepage')
        else:
            return render(request, 'logintippee.html', {'error': 'Invalid email or password'})
    return render(request, 'logintippee.html')


@login_required
def tippee_homepage(request):
    return render(request, 'tippeehomepage.html', {'tippee': request.user})


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

@login_required
def tippee_jar(request):
    
    tips = []  
    return render(request, 'tippeejar.html', {'tips': tips})


@login_required
def tipper_jar(request):
    
    tips = []  
    return render(request, 'tipperjar.html', {'tips': tips})


@login_required
def tipper_list(request):
    return render(request, 'tipper_list.html')


@login_required
def tipper_update(request, pk):
    return render(request, 'tipper_update.html')


@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'tipper_confirm_delete.html')

def logout_view(request):
    logout(request)
    return redirect('home')

