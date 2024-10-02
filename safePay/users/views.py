from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            phone_no = form.cleaned_data['phone_no']
            password = form.cleaned_data['password']
            
            user = authenticate(request, phone_no=phone_no, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('landing_page')
            else:
                form.add_error(None, "Invalid phone number or password")
        else:
            form = UserLoginForm()
        
        return render(request, 'user/login.html', {'form', form})

@login_required
def logout(request):
    return render(request, 'users/logout.html')



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            print("User saved successfully")
            
            user.authenticate(username=form.cleaned_data['phone_no'], password= form.cleaned_data['password1'])
            
            if user is not None:
                login(request, user)
                print("User logged in: ", request.user.is_authenticated)
                return redirect('landing_page')
            else:
                print("Failed to login")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})          