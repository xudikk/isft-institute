from django.urls import path
from core.dashboard.auth import login
from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login')
]
