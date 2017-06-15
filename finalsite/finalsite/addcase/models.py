from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Addcase(models.Model):
	name_s = models.CharField(max_length=20)
	phone_s = models.CharField(max_length=20)
	gender_s = models.CharField(max_length=2)
	gender_t = models.CharField(max_length=2)
	address_s = models.CharField(max_length=30)
	description_s = models.TextField(default='無')
	class_week = models.CharField(max_length=30)
	subject = models.CharField(max_length=30)
	other = models.TextField(default='無')

	def __str__(self):
		return self.name_s

class AddTeachers(models.Model):
	name_teacher = models.CharField(max_length=20)
	phone_teacher = models.CharField(max_length = 20)
	major = models.CharField(max_length=20)
	experience = models.TextField(default='無')
	TSubject = models.CharField(max_length=20)
	Other = models.TextField(default = '無')

	def __str__(self):
		return self.name_teacher