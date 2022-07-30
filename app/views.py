from app.models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from app.serializers import TodoSerializers

class TodoViewSet(viewsets.ModelViewSet):
    """View reduzida criada com viewsets"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


"""class TodoListAndCreat(generics.ListCreateAPIView):
    # Viwes com funções implementadas pela generics
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
     # Viwes com funções implementadas pela generics
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers"""

"""class TodoListAndCreat(APIView):
    #View refatorada em ClassBasedViews implementado as funções
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

function based views
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""



"""class TodoDetailChangeAndDelete(APIView):
    #View refatorada em ClassBasedViews implementando as funções
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer =  TodoSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """



""" function based views
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_change_and_delete(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer =  TodoSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
