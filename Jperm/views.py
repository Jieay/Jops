# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from Juser.models import User, UserGroup
from Jieay.api.api import *

@require_role('user')
def perm_role_get(request):
    salt_id = request.GET.get('id', 0)
    if salt_id:
        salt = get_object(Salt, id=salt_id)
        if salt:
            role = user_have_perm(request.user, salt=salt)
            logger.debug(u'获取授权系统用户: ' + ','.join([i.name for i in role]))
            return HttpResponse(','.join([i.name for i in role]))
    else:
        roles = get_group_user_perm(request.user).get('role').keys()
        return HttpResponse(','.join(i.name for i in roles))

    return HttpResponse('error')