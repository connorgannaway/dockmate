from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin as LRM

#displays register view
def register(request):
    #validates and saves form data if POST request
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}.')
            return redirect('login')
    #get request that displays empty form
    else:
        form = UserRegistrationForm()
    
    return render(request, "users/register.html", {'form':form, 'title':'Register'})

#displays profile editing view
@login_required
def profile(request):
    #validates and saves user and profile forms from a POST request
    if request.method == "POST":
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, 'Account Updated')
            return redirect('profile')
    #get request that displays pre-filled user and profile forms
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'profileform': profileform,
        'title':'Profile'
    }
    return render(request, 'users/profile.html', context)

#loops through and lists Profile objects
class ListEmployees(LRM, ListView):
    model = Profile
    context_object_name = 'employees'
