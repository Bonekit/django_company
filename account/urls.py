from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('registration/', views.sign_up, name='account-sign_up'),
    path('login/', views.sign_in, name='account-sign_in'),
    path('logout/', views.sign_out, name='account-sign_out'),
]
