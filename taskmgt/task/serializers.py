from rest_framework import serializers
from task.models import Task , Employee , Client
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    task=TaskSerializer(read_only=True)
    task_id=serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(),
        source='task',
        write_only=True
    )
    class Meta:
        model=Employee
        fields="__all__"

class ClientSerializer(serializers.ModelSerializer):
    task=TaskSerializer(read_only=True)
    task_id=serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(),
        source='task',
        write_only=True
    )
    class Meta:
        model=Client
        fields='__all__'