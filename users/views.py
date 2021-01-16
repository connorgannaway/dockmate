from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}.')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    
    return render(request, "users/register.html", {'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, 'Account Updated')
            return redirect('profile')
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'profileform': profileform
    }
    return render(request, 'users/profile.html', context)