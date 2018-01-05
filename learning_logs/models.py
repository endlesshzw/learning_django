from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
	
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=True)
	def __str__(self):
		return self.text

class Entry(models.Model):
	
	topic = models.ForeignKey(Topic, on_delete=True)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
	
	def __str__(self):
		if len(self.text)>50:
			return self.text[:50] + '...'
		else:
			return self.text
		 
class Info(models.Model):
	name = models.CharField(max_length=200)
	sex = models.CharField(max_length=200)
	age = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name