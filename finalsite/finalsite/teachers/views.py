from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, render_to_response
#from .models import teachersAddcase
# Create your views here.
def teachers(request):
	return render_to_response('case/teachers.html', locals())