
from django.shortcuts import render,redirect
from django.contrib.auth import login as loginuser, authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserSignUpForm
from .models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required

def signin(request):

    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login') 
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method=='GET':
        form=AuthenticationForm()
        context={
        'form':form
        }
        return render(request,"login.html",context=context)
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                utype=user.user_type
                if (utype=="D"):
                    loginuser(request,user)
                    return redirect('doctor_dashboard')
                else:
                    loginuser(request,user)
                    return redirect('patient_dashboard')

        else:
            context={
            'form':form
            }
            return render(request,"login.html",context=context)
  

def patient_dashboard(request):
    user = request.user
    return render(request, 'patient_dashboard.html', {'user': user})

def doctor_dashboard(request):
    user = request.user
    return render(request, 'doctor_dashboard.html', {'user': user})
    

def home (request):
    return render(request,'home.html')

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect("login")   