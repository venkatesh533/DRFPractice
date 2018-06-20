"""RestPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import serializers, routers, viewsets
from RestApp.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employees-list', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^employees/', EmployeeGenericsList.as_view()),
    url(r'^employee/(?P<pk>\d+)/', EmployeeGenericsDetail.as_view()),
    #### mixin urls ####
    url(r'^employeeslist-mixins/', EmployeeMixinListView.as_view()),
    url(r'^employeedetail-mixins/(?P<pk>\d+)/', EmployeeMixinDetailView.as_view()),
    #### urls using for auth&permission conecpts ####
    url(r'^users-list/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view()),
    #### snippet urls ####
    url(r'^snippets/', SnippetList.as_view()),
    url(r'^snippet/(?P<pk>\d+)/', SnippetDetail.as_view()),
    

]

