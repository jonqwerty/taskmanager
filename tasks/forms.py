from django import forms
from django.forms import ModelForm

from .models import *

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = '__all__'



class TaskForm(forms.ModelForm):
	
	class Meta:
		model = Task
		fields = '__all__'

class OrderingForm(forms.Form):
    ordering = forms.CharField()

    
#class TaskForm(forms.ModelForm):
	###title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
	#class Meta:
		#model = Task
		#fields = '__all__'