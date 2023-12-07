#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.urls import path
from core.dashboard.vacancy import vacancy, check_test, final_result
from core.dashboard.view import candedant, test
from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('candedant/', candedant, name='condedant'),
    path('candedant/info/<pk>/', candedant, name='view_condedant'),
    path('test/', test, name='tests'),
    path('test/info/<pk>/', test, name='view_test'),
    path('test/add/<status>/', test, name='add_test'),
    path('test/edit/<status>/<pk>/', test, name='edit_test'),
    path('test/delete/<status>/<pk>/', test, name='del_test'),

    # vacancy
    path('vacancy/', vacancy, name='vacancy'),
    path('test/check/', check_test, name='test-checker'),
    path('final/result/', final_result, name='final-result'),


]
