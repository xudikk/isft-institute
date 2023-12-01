#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.shortcuts import render, redirect
import requests

from core.models import User


def login(request):
    return render(request, 'auth/login.html', {})
