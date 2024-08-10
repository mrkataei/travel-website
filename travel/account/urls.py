from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    # path('', logout, name='logout'),
    # path('', signup, name='signup'),
]