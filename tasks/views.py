from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect

from django.urls import reverse

from django.views.decorators.http import *
from django.db import transaction

from .models import *
from .forms import *

# Create your views here.

def projects_list(request):

	# projects = Project.objects.order_by('created')

	projects = Project.objects.all()

	
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

def deadlineProject(request, pk):
	project = Project.objects.get(id=pk)
	d = project.deadline_func()

	d = d.days
	


	context = {"dd":d}

	print (type(d))

	return render ( request, 'tasks/show_deadline_project.html', context )


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

# def createTask(request):

# 	form = TaskForm()

# 	if request.method == 'POST':
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'tasks/create_project.html', context )

def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('/')

	print(type(task.id))

	context = {'form':form}	
	return render(request, 'tasks/create_task.html', context )

def deleteTask(request, pk):
	task = Task.objects.get(id=pk)

	if request.method == 'POST':
		task.delete()
		return redirect('/')

	context = {'item':task}
	return render (request, 'tasks/delete_task.html', context)


def createTask(request, pk):
	a = Project.objects.get(id = pk)
	if request.method == 'POST':
		d = request.POST['title']
		a.task_set.create(title = d )
		return redirect('/')

	context = {"project.id":a}

	return render ( request, 'tasks/index.html', context )

def deadlineTask(request, pk):
	task = Task.objects.get(id=pk)
	d = task.deadline_func()

	d = d.days
	
	context = {"dd":d}

	return render ( request, 'tasks/show_deadline_task.html', context )

	

# 	if request.method == 'POST':
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'tasks/create_project.html', context )


@require_POST
def save_new_ordering(request):
	form = OrderingForm(request.POST)

	if form.is_valid():
	    ordered_ids = form.cleaned_data["ordering"].split(',')

	    with transaction.atomic():
	        current_order = 1
	        for id in ordered_ids:
	            group = Task.objects.get(id__exact=id)
	            group.order = current_order
	            group.save()
	            current_order += 1


	print (type(id))
	print ((Task.objects.get(id=1)).order)
	
	a = Task.objects.all().order_by('order')

	context = {'aa':a}

	return render(request, 'tasks/reorder.html', context)
	

	