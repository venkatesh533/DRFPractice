
from django.contrib.auth.models import User
from rest_framework import serializers
from RestApp.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','snippets')

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner')

''' basic serializer for employee model '''
class EmpBaseSerialier(serializers.Serializer):
    emp_id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Employees.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

''' model serializer (like model form) for employee model'''
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

'''
serializer for department model
'''
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'



