from django.shortcuts import render


def login(request):
    if request.user.is_authenticated:
        msg = f"{request.user.username} is authenticated"
    else:
        msg = f"you are not authenticated"
    return render(request, 'account/login.html', {"msg": msg})


# def logout(request):
#     pass


# def signup(request):
#     return render(request, 'account/signup.html')