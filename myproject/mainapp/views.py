from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import TipperSignUpForm, TippeeSignUpForm
from .models import User

def home(request):
    return render(request, 'index.html')

def logintipper(request):
    return render(request, 'logintipper.html')

def logintippee(request):
    return render(request, 'logintippee.html')

def signuptipper(request):
    if request.method == 'POST':
        form = TipperSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"Tipper account created: {user.username}, {user.email}")
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
