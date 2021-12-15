from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserForm



def log_out(request):
    logout(request)
    return redirect('listings:index')

def register(request):
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)