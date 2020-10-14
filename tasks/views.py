from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import *

# Create your views here.

def projects_list(request):

	projects = Project.objects.order_by('created')

	
	#project = Project.objects.get(pk = 2)


	#tasks = project.task_set.all()


	return render(request,'tasks/index.html', context={"projects":projects})

def createProject(request):

	form = ProjectForm()

	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}
	return render(request, 'tasks/create_project.html', context )

def updateProject(request, pk):
	project = Project.objects.get(id=pk)
	form = ProjectForm(instance=project)

	if request.method == 'POST':
		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}	
	return render(request, 'tasks/create_project.html', context )

def deleteProject(request, pk):
	project = Project.objects.get(id=pk)

	if request.method == 'POST':
		project.delete()
		return redirect('/')

	context = {'item':project}
	return render (request, 'tasks/delete_project.html', context)

def createTask(request):

	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}
	return render(request, 'tasks/create_project.html', context )

def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}	
	return render(request, 'tasks/create_task.html', context )

def deleteTask(request, pk):
	task = Task.objects.get(id=pk)

	if request.method == 'POST':
		task.delete()
		return redirect('/')

	context = {'item':task}
	return render (request, 'tasks/delete_task.html', context)






