from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompanyUpdateForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View, CreateView
from .models import Company, Profile
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse

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
    paginate_by = 10

#Displays current company and form to update
class CompanyView(LRM, View):
    template_name = 'users/company.html'

    #creates empty form and passes data
    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.profile.company:
            company = user.profile.company
        else:
            company = None
        
        context = {
            'title': 'Company',
            'currentCompany': company,
            'form': CompanyUpdateForm()
        }
        return render(request, self.template_name, context)

    #logic for processing form
    def post(self, request, *args, **kwargs):
        form = CompanyUpdateForm(self.request.POST)
        if form.is_valid():
            leave = form.cleaned_data.get('leave')
            if leave:
                if self.request.user.profile.company:
                    self.request.user.profile.company = None
                    self.request.user.profile.save()
                    messages.success(self.request, 'Current Company Deleted.')
            else:
                company = form.cleaned_data.get('company')
                key = form.cleaned_data.get('key')
                if company.key == key:
                    self.request.user.profile.company = company
                    self.request.user.profile.save()
                    messages.success(self.request, 'Company Updated')
                else:
                    messages.warning(self.request, 'Incorrect Key. Try again.')
        else:
            messages.error(self.request, 'Form error')

        return redirect('company')

#View for creating companys using company model.
class CreateCompany(LRM, CreateView):
    template_name = 'users/company_form.html'
    model = Company
    fields = ['name', 'key']

    def get_success_url(self):
        messages.success(self.request, 'Company successfully created.')
        return reverse('company')
