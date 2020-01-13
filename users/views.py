from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == "POST": # if we get a post request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username  = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}!!')
            return redirect('login')

    else:
        form = UserRegisterForm()  # else just an empty form get request
    return render(request,'users/register.html',{'form':form})