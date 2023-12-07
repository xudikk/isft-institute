#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.urls import path
from core.dashboard.vacancy import vacancy, check_test, final_result
from core.dashboard.new import new_html


urlpatterns = [

    # vacancy
    path('vacancy/', vacancy, name='vacancy'),
    path('test/check/', check_test, name='test-checker'),
    path('final/result/', final_result, name='final-result'),


    path('new_html/', new_html, name='new_html'),
    path('new_html/view/<int:view>/', new_html, name='test_html'),
    path('new_html/<status>/', new_html, name='new_status'),
]
