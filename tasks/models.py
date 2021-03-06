import uuid
from django.db import models
from datetime import *


# Create your models here.


class Project(models.Model):
	title = models.CharField('Title of project', max_length=300, null=True)
	deadline = models.DateField('Deadline of the project (year, month, day)', default=date.today)
	created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.title

	def deadline_func(self):
		days = self.deadline - date.today()
		return days
		



class Task(models.Model):
	
	project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=300, null=True)
	complete = models.BooleanField(default=False)
	deadline = models.DateField('Deadline of the task (year, month, day)', default=date.today)
	created = models.DateTimeField(auto_now_add=True,null=True)
	lookup_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
	order = models.IntegerField(blank=False, default=100_000)

	def __str__(self):
		return self.title

	def deadline_func(self):
		days = self.deadline - date.today()
		return days
		
	class Meta: 		
		ordering = ['order']

# class Group(models.Model):
#     lookup_id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
#     order = models.IntegerField(blank=False, default=100_000)



# class Task(models.Model):
# 	STATUS = (
# 		('To do', 'To do'),
# 		('In process', 'In process'),
# 		('Done', 'Done'),
# 		)
# 	project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
# 	title = models.CharField(max_length=300, null=True)
# 	complete = models.BooleanField(default=False)
# 	status = models.CharField(max_length=300, null=True, choices=STATUS)
# 	created = models.DateTimeField(auto_now_add=True,null=True)

# 	def __str__(self):
# 		return self.title