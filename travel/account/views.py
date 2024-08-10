from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# def login_view(request):
#     # if request.user.is_authenticated:
#     #     msg = f"{request.user.username} is authenticated"
#     # else:
#     #     msg = f"you are not authenticated"
#     # return render(request, 'account/login.html', {"msg": msg})
#     if request.user.is_authenticated:
#         return redirect('/')
#     # if request.method == 'POST':
#     if "register" in request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('account:login')
#         form = UserCreationForm()
#         context = {"form": form}
#         return render(request, 'account/login.html', context=context)
#     if "login" in request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('/')

#     return render(request, 'account/login.html')
def login_view(request):
    # Initialize the forms to ensure they're always available
    login_form = AuthenticationForm()
    registration_form = UserCreationForm()

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        if 'login' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password')
        
        elif 'register' in request.POST:
            registration_form = UserCreationForm(request.POST)
            if registration_form.is_valid():
                user = registration_form.save()
                login(request, user)
                return redirect('/')
            else:
                for field, errors in registration_form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")

    return render(request, 'account/login.html', {
        'login_form': login_form,
        'registration_form': registration_form,
    })
@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login')




# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('account:login')
#     form = UserCreationForm()
#     context = {"form": form}

#     return render(request, 'account/login.html', context=context)