from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import User
from problem.models import Problem
from account.permissions import is_admin_or_root

from django.db.models import Q
from django.urls import reverse

from functools import reduce
from operator import or_


def query_user(kw):
    results = list()
    if len(kw) >= 3:
        for user in User.objects.filter(username__icontains=kw).all().only('username')[:5]:
            results.append(dict(title=user.username, url=reverse('generic', kwargs=dict(name=user.username))))
    return dict(name='User', results=results)


def get_problem_q_object(kw, all=False, managing=None):
    q_list = list()
    if len(kw) >= 3:
        q_list.append(Q(title__icontains=kw))
    if kw.isdigit():
        q_list.append(Q(pk__exact=kw))
    if q_list:
        q = reduce(or_, q_list)
        if not all:
            q &= Q(visible=True)
        if managing:
            q |= Q(problemmanagement__user=managing)
        return q
    return None


def query_problem(kw, all=False):
    results = list()
    q = get_problem_q_object(kw, all)
    if q:
        for problem in Problem.objects.filter(q).distinct().all()[:5]:
            results.append(dict(title=str(problem),
                                url=reverse('problem:detail', kwargs=dict(pk=problem.pk))))
    return dict(name='Problem', results=results)


class SearchAPI(APIView):
    def get(self, request):
        kw = request.GET.get('kw')
        results = dict()
        if kw:
            results['user'] = query_user(kw)
            results['problem'] = query_problem(kw, all=is_admin_or_root(request.user))
        return Response(dict(results=results))


class SearchUserAPI(APIView):
    def get(self, request):
        kw = request.GET.get('kw')
        results = list()
        if kw:
            for user in User.objects.filter(username__icontains=kw).all().only('username', 'pk')[:5]:
                results.append(dict(name=user.username, value=user.pk))
        return Response(dict(success=True, results=results))


class SearchProblemAPI(APIView):
    def get(self, request):
        kw = request.GET.get('kw')
        managing = request.user if request.GET.get('managing') else None
        results = list()
        q = get_problem_q_object(kw, is_admin_or_root(request.user), managing)
        if q:
            for problem in Problem.objects.filter(q).distinct().all()[:5]:
                results.append(dict(name=str(problem), value=problem.pk))
        return Response(dict(success=True, results=results))