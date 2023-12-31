from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from core.forms import QuizForm
from core.models import Candidate, ResultTest
from core.models.vacancy import Test
from django.db.models import Q


def candedant(request, pk=None, ):
    pagination = Candidate.objects.all().order_by('-pk')
    paginator = Paginator(pagination, 30)
    page_number = request.GET.get("page", 1)
    paginated = paginator.get_page(page_number)

    ctx = {
        "roots": paginated,
        "pos": "list",
        'size': 'big'
    }
    if pk:
        us = ResultTest.objects.filter(candidate_id=pk).first()
        query = ""
        for i in us.result_tests():
            query += f'Q(id={i}) | '
        query = query.rstrip('| ')
        tests = Test.objects.filter(eval(query))
        ctx['len'] = len(tests)
        ctx['root'] = us
        ctx['test'] = tests
        ctx['corrects'] = eval(us.corrects)
        ctx['incorrects'] = eval(us.incorrects)
        ctx['size'] = 'small'

    return render(request, 'work/pages/candedant.html', ctx)


def test(request, pk=None, status=None):
    pagination = Test.objects.all().order_by('-pk')
    paginator = Paginator(pagination, 30)
    page_number = request.GET.get("page", 1)
    paginated = paginator.get_page(page_number)

    ctx = {
        'roots': Test.objects.all().order_by('-id'),
        "roots": paginated,
        "pos": "list"
    }
    if pk and not status:
        ctx['root'] = Test.objects.filter(pk=pk).first()
        ctx['big'] = True
    if status == 'form':
        root = Test.objects.filter(pk=pk).first()
        form = QuizForm(request.POST or None, instance=root or None)
        if form.is_valid():
            form.save()
            return redirect('tests')
        ctx['root'] = root
        ctx['form'] = form
        ctx['status'] = 'form'
    if status == 'del':
        root = Test.objects.filter(pk=pk).first()
        try:
            root.delete()
        except:
            pass
    return render(request, 'work/pages/tests.html', ctx)
