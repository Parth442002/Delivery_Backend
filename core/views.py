from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import House, GovernmentCorp, RenewableEnergy
from .serializers import HouseSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response


# Create your views here.
'''
class HouseView(APIView):

    def get_object(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HouseSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = HouseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
