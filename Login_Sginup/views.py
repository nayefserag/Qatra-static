from django.shortcuts import render, redirect
from django.contrib.auth import * 
from django.contrib import messages
from .forms import UserRegistrationForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView, PasswordResetView



@login_required(login_url='login')
def home(request):
    return render(request, 'Home/Home.html')

def Sginup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'Sginup/Sginup.html', context)


def logout_view(request):
    logout(request)
    if 'form_fields' in request.session:
        del request.session['form_fields']
    return redirect('login')


#Forget Password Func#
class loginView(LoginView):
    template_name='Login.html'