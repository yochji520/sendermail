#!/usr/bin/python3
#-*- coding: UTF-8 -*-

from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from urllib.parse import unquote
from mailrest.test import *
from mailrest.sendmail import *


@csrf_exempt
@api_view(http_method_names=['post', 'get'])
@permission_classes((permissions.AllowAny,))
def revdata(request):
    if request.method == 'GET':
        return Response('''welcome to sendermail!!!''')
    elif request.method == 'POST':
        str_bytes = request.body
        par_str = unquote(str_bytes.decode(encoding='UTF-8'))
        strlist = par_str.split('&')
        tomail = strlist[0]
        subject = strlist[1]
        content = strlist[2]
        sendmail(tomail, subject, content)
        a(par_str)
        return Response(par_str)
    else:
        pass