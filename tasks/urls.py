from django.urls import path
from . import views

urlpatterns = [
    path('' , views.projects_list, name="list"),
    path('create_project/' , views.createProject, name="create_project"),
    path('update_project/<str:pk>' , views.updateProject, name="update_project"),
    path('delete_project/<str:pk>' , views.deleteProject, name="delete_project"),
    path('create_task/' , views.createTask, name="create_task"),
    path('update_task/<str:pk>' , views.updateTask, name="update_task"),
    path('delete_task/<str:pk>' , views.deleteTask, name="delete_task"),
   
]