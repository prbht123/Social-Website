from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Profile
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm,UserEditForm, ProfileEditForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
                
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



@login_required
def dashboard(request):
    print("hello")
    return render(request,'account/dashboard.html',{'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print("00000000000",user_form)
        if user_form.is_valid():
        # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)

        return render(request,'register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        print(user_form)
        return render(request,'register.html',{'user_form': user_form})



@login_required
def edit(request):
    if request.method == 'POST':
        print("000000000000")
        user_form = UserEditForm(instance=request.user,
        data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        print("00000000")
        user_form = UserEditForm(instance=request.user)
        print("llllllllllllllll")
        profile_form = ProfileEditForm(instance=request.user.profile)
        print("999999999999999")
        print(profile_form)
        
    return render(request,'account/edit.html',{'user_form': user_form,'profile_form': profile_form})
