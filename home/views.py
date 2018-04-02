# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'home/home.html')

def contact(request):
    return render(request, 'home/basic.html',{'content':['If you would like to contact me, please email me.','shamasnn@mail.uc.edu']})
