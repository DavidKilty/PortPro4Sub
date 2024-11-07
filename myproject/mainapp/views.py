from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import TipperSignUpForm, TippeeSignUpForm
from .models import User  
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'index.html')

def logintipper(request):
    return render(request, 'logintipper.html')

def logintippee(request):
    return render(request, 'logintippee.html')

def signuptipper(request):
    form = TipperSignUpForm()
    if request.method == 'POST':
        form = TipperSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("Form errors:", form.errors)
    return render(request, 'signuptipper.html', {'form': form})

def signuptippee(request):
    form = TippeeSignUpForm()
    if request.method == 'POST':
        form = TippeeSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'signuptippee.html', {'form': form})

class TipperDeleteView(DeleteView):
    model = User  # Changed from Tipper to User
    template_name = 'tipper_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return User.objects.filter(user_type='tipper')
