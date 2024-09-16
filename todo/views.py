from rest_framework import generics
from .serializers import TaskSerializer
from .models import ToDo
 
class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TaskSerializer

class ReadTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TaskSerializer
    
class UpdateTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TaskSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TaskSerializer

