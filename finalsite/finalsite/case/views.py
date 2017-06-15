from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, render_to_response
from addcase.models import Addcase , AddTeachers
from django.template import RequestContext
# Create your views here.
def index(request):
	case_list = Addcase.objects.order_by('-id')[:3]
	teacher_list = AddTeachers.objects.order_by('-id')[:3]
	return render(request,'case/index.html',locals())

def contact(request):
	return render(request,'case/contact.html',locals())

def search_student(request):
	return render(request,'case/search_student.html',locals())

def search_teacher(request):
	return render(request,'case/search_teacher.html',locals())

def addCase(request):
	if request.method == "POST":  
		Name_s=request.POST['name_s']
		Phone_s=request.POST['phone_s']
		Gender_s=request.POST['gender_s']
		Gender_t=request.POST['gender_t']
		Address_s=request.POST['address_s']
		Description_s=request.POST['description_s']
		Class_week=request.POST['class_week']
		Subject=request.POST['subject']
		Other=request.POST['other']
		a=Addcase(name_s=Name_s,phone_s=Phone_s,gender_s=Gender_s,gender_t=Gender_t,address_s=Address_s,description_s=Description_s,class_week=Class_week,subject=Subject,other=Other)
		a.save()
		teacher_list = AddTeachers.objects.order_by('-id')[:3]
		case_list = Addcase.objects.order_by('-id')[:3]
	return render(request,'case/index.html',locals())

def addCaseT(request):
	if request.method == "POST":  
		Name_teacher=request.POST['name_teacher']
		Phone_teacher=request.POST['phone_teacher']
		Major=request.POST['major']
		Experience=request.POST['experience']
		tSubject=request.POST['TSubject']
		other=request.POST['Other']
		print('name'+Name_teacher)
		a=AddTeachers(name_teacher=Name_teacher,phone_teacher=Phone_teacher,major=Major,experience=Experience,TSubject=tSubject,Other=other)
		a.save()
		case_list = Addcase.objects.order_by('-id')[:3]
		teacher_list = AddTeachers.objects.order_by('-id')[:3]
	return render(request,'case/index.html',locals())
def searchT(request):
	if request.method == "POST": 
		Subject=request.POST['subject']
		tea_list=AddTeachers.objects.filter(TSubject=Subject).order_by("-id")
		return render(request,'case/search_teacher.html',locals())

def searchS(request):
	if request.method == "POST": 
		Subject=request.POST['subject']
		stu_list=Addcase.objects.filter(subject=Subject).order_by("-id")
		return render(request,'case/search_student.html',locals())