from django.db import models

# Create your models here.


class Project(models.Model):
	title = models.CharField(max_length=300, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.title



class Task(models.Model):
	
	project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=300, null=True)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.title




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