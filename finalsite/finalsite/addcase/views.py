from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, render_to_response
from .models import Addcase
# Create your views here.
def addcase(request):
	return render_to_response('case/students.html', locals())
def addCase(request):
	if request.method == "POST":  
		Name_s=request.POST.get['name_s']
		Phone_s=request.POST.get['phone_s']
		Gender_s=request.POST.get['gender_s']
		Gender_t=request.POST.get['gender_t']
		Address_s=request.POST.get['address_s']
		Description_s=request.POST.get['description_s']
		Class_week=request.POST.get['class_week']
		Subject=request.POST.get['subject']
		Other=request.POST.get['other']
		Addcase.objects.create(name_s=Name_s,phone_s=Phone_s,gender_s=Gender_s,gender_t=Gender_t,address_s=Address_s,description_s=Description_s,class_week=Class_week,subject=Subject,other=Other)
		case_list = Addcase.objects.all()
	return render(request,'case/index.html',{'case_list':case_list})
