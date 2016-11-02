# -*- coding: utf-8 -*-

from __future__ import division
import uuid
import urllib
import json
from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.http import HttpResponse
import paramiko
from Jieay.api.api import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Jperm.perm_api import get_group_user_perm, gen_resource


try:
    from django.http import JsonResponse
except ImportError:
    from Jieay.api.api import JsonResponse

def getDaysByNum(num):
    """
    输出格式:([datetime.date(2015, 11, 6),  datetime.date(2015, 11, 8)], ['11-06', '11-08'])
    """

    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    date_li, date_str = [], []
    for i in range(0, num):
        today = today-oneday
        date_li.append(today)
        date_str.append(str(today)[5:10])
    date_li.reverse()
    date_str.reverse()
    return date_li, date_str


def get_data(x, y, z):
    pass

@require_role(role='user')
def index_cu(request):
    username = request.user.username
    return HttpResponseRedirect(reverse('user_detail'))


@require_role(role='user')
def index(request):
    li_date, li_str = getDaysByNum(7)
    today = datetime.datetime.now().day
    from_week = datetime.datetime.now() - datetime.timedelta(days=7)

    if is_role_request(request, 'user'):
        return index_cu(request)

    elif is_role_request(request, 'super'):
        # dashboard 显示汇总
        users = User.objects.all()
        # hosts = Asset.objects.all()

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def skin_config(request):
    return render_to_response('skin_config.html')


def is_latest():
    node = uuid.getnode()
    jsn = uuid.UUID(int=node).hex[-12:]
    with open(os.path.join(BASE_DIR, 'version')) as f:
        current_version = f.read()
    lastest_version = urllib.urlopen('http://www.jumpserver.org/lastest_version.html?jsn=%s' % jsn).read().strip()

    if current_version != lastest_version:
        pass

@defend_attack
def Login(request):
    """登录界面"""
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'GET':
        return render_to_response('login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.role == 'SU':
                        request.session['role_id'] = 2
                    elif user.role == 'GA':
                        request.session['role_id'] = 1
                    else:
                        request.session['role_id'] = 0
                    return HttpResponseRedirect(request.session.get('pre_url', '/'))
                else:
                    error = '用户未激活'
            else:
                error = '用户名或密码错误'
        else:
            error = '用户名或密码错误'
    return render_to_response('login.html', {'error': error})

@require_role('user')
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))