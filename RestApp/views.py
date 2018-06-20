# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
### for permissions ###
from rest_framework import permissions
from RestApp.serializers import *
from RestApp.models import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

### viewset for departments model ###
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListView(APIView):
    '''
    General api view for employees listing objects
    '''
    def get(self,request):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer(queryset,many=True)
        return Response(serializer_class.data)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    '''
    General api view to Retrieve,delete and update instances of employee 
    '''
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self,request,pk):
        emp_obj = self.get_object(pk)
        serializer = EmployeeSerializer(emp_obj)
        return Response(serializer.data)
        
    def put(self,request,pk):
        emp_obj = self.get_object(pk)
        serializer = EmployeeSerializer(emp_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        emp_obj = self.get_object(pk)
        emp_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeMixinListView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    '''
    Employee list view using mixins and generics
    '''
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeMixinDetailView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    '''
    Employee detail view using mixins and generics
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class EmployeeGenericsList(generics.ListCreateAPIView):
    '''
    Employees list using generics listcreateapiview
    '''
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer

class EmployeeGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Employees objects detail view (retrieve,update,delete) using generics RetrieveUpdateDestroyAPIView
    '''
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer

class UserList(generics.ListAPIView):
    '''
    user list api view 
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    '''
    user object detail api view 
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
    '''
    Snippet list api view
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Snippet detail api view
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



