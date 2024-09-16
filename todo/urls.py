from django.urls import path
from .views import CreateTodo, ReadTodo, UpdateTodo, DeleteTodo

urlpatterns = [
    path('<int:pk>/', UpdateTodo.as_view()),        # For updating a task
    path('', ReadTodo.as_view()),                   # For listing tasks
    path('create', CreateTodo.as_view()),           # For creating a task
    path('delete/<int:pk>', DeleteTodo.as_view()),  # For deleting a task
]
