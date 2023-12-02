#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.urls import path
from core.dashboard.vacancy import vacancy


urlpatterns = [

    # vacancy
    path('vacancy/', vacancy, name='vacancy')



]
