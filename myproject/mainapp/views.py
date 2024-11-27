from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import TipperSignUpForm, TippeeSignUpForm
from .models import User, Tip  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

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


@login_required
def tipper_list(request):
   
    query = request.GET.get('q', '')
    users = User.objects.filter(username__icontains=query, user_type='tippee') if query else []
    return render(request, 'tipper_list.html', {'users': users})

@login_required
def tipper_jar(request, user_id):
    receiver = get_object_or_404(User, id=user_id, user_type="tippee")
    amounts = [0.20, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00] 
    return render(request, 'tipperjar.html', {'receiver': receiver, 'amounts': amounts})


@login_required
def tippee_jar(request, user_id):
    tippee = get_object_or_404(User, id=user_id, user_type="tippee")
    tips = Tip.objects.filter(receiver=tippee)
    return render(request, 'tippeejar.html', {'receiver': tippee, 'tips': tips})


@login_required
def leave_tip(request, user_id):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        receiver = get_object_or_404(User, id=user_id, user_type="tippee")
        Tip.objects.create(sender=request.user, receiver=receiver, amount=amount)
        return redirect('tipper_jar', user_id=user_id)

@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id, sender=request.user)
    if request.method == "POST":
        tip.delete()
        return redirect('tipper_jar', user_id=request.user.id) 
    return render(request, 'tipper_update.html', {'tip': tip})

def logout_view(request):
    logout(request)
    return redirect('home')
