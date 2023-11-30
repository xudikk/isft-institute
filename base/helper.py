#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import datetime
from contextlib import closing

from django.conf import settings
from random import randint

from django.db import connection
from methodism import dictfetchone, dictfetchall


def lang_helper(request):
    if not request.user.is_anonymous:
        return request.user.lang
    return settings.DEFAULT_LANG


def card_mask(number):
    return number[0:4] + ' **** ****' + number[14:]


def look_at_params(params: dict, requires: list):
    """
    params required checker:
    the code
        `if 'name' not in params or 'pass' not in params or email not in params`
          is used as below
        `look_at_params(params, ['name', 'password', 'email'])`
    """
    return set(requires) - set(params.keys())

