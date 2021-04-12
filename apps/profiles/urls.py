from django.urls import path
from .views import account, editAccount


app_name = 'apps.profiles'

urlpatterns = [
    path('', account, name='account'),
    path('<int:pk>/', editAccount, name='account_edit')]
