from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    # if request.user.is_authenticated:
    #     msg = f"{request.user.username} is authenticated"
    # else:
    #     msg = f"you are not authenticated"
    # return render(request, 'account/login.html', {"msg": msg})
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')




# def signup(request):
#     return render(request, 'account/signup.html')