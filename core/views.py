#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.shortcuts import render


def home(request):
    return render(request, 'work/base.html', {})