#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.contrib import admin

# Register your models here.
from core.models import Candidate, Test, ResultTest

admin.site.register(Candidate)
admin.site.register(Test)
admin.site.register(ResultTest)