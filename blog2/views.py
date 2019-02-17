# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('blog2')

def index_page(request):
    return render(request, 'blog2/index.html', {'name': 'imooc'})
