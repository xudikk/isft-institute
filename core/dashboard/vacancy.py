#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import binascii
import datetime
import os
from contextlib import closing

from django.db import connection
from django.shortcuts import render, redirect, HttpResponse

from base.custom import answered_dictfetchall
from core.models import ResultTest, Candidate


def vacancy(request):
    with closing(connection.cursor()) as cursor:
        sql = """
               SELECT id, quest AS question, "true" AS answer, a, b, c, d FROM core_test
               order by random() limit 20;
           """
        cursor.execute(sql)
        result = answered_dictfetchall(cursor)

    if request.POST:
        data = request.POST
        condidate = Candidate.objects.create(**{'FIO': data.get('fio', ), 'pasport_seria': data.get('seria', ),
                                                'pasport_number': data.get('seria_num', ), 'phone': data.get('phone', ),
                                                })
        test = ResultTest.objects.create(candidate=condidate, status='Boshlandi',
                                         test_ids=str(repr([x['id'] for x in result])),)
        request.session['test_id'] = test.id
        return HttpResponse("success")

    ctx = {
        "quests": result,
    }
    return render(request, 'pages/quiz.html', ctx)


def check_test(request):
    data = request.GET
    result = ResultTest.objects.filter(id=request.session.get('test_id', 0)).first()
    if result:
        corrects = eval(result.corrects)
        incorrects = eval(result.incorrects)
        if int(data.get('result', 0)):
            corrects.append(int(data.get('test_id')))
        else:
            incorrects.append(int(data.get('test_id')))

        result.corrects = str(corrects)
        result.incorrects = str(incorrects)
        result.save()
        print(corrects, incorrects)
    return HttpResponse("Continue")


def final_result(request):
    data = request.GET
    result = ResultTest.objects.filter(id=request.session.get('test_id', 0)).first()
    print(data)
    if result:
        result.corrects_cnt = int(data.get('correct', 0))
        result.incorrects_cnt = int(data.get('inc', 0))
        result.end = datetime.datetime.now()
        result.save()
    return HttpResponse("Continue")



