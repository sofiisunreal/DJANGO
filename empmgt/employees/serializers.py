from rest_framework import serializers

from employees.models import Department, Employee

# department serializer

class DepartmentSerializer(serializers.ModelSerializer):
    # this serializer converts department model data into JSON format and also allows JSON data to be converted back into django objects
    # basically acts like a bridge between django model and api response 
    class Meta:
        model=Department
        fields='__all__'
        # includes all fields from the department model 

class EmployeeSerializer(serializers.ModelSerializer):
    # read only shows full nested department on get request 
    department=DepartmentSerializer(read_only=True)
    
    # write only accepts a department id integer during post/put
    department_id=serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True
    )
    class Meta:
        model=Employee 
        fields='__all__'