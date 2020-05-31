from django.shortcuts import render

# Create your views here.
## 新しく追加
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from windletterapi.models import User
from windletterapi.serializers import MessageSerializer, ChangeDataSerializer

## @api_view()デコレータをつける
# @csrf_exempt
@api_view(['GET', 'POST'])
def message(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = MessageSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## @api_view()デコレータをつける
# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def change_data(request, pk):

    """
    Retrieve, update or delete a code snippet.
    """

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ChangeDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
