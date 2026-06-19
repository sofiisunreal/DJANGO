from django.http import HttpResponse
from rest_framework.decorators import api_view

def home(request):
    return HttpResponse("Welcome to Django")

def introduction(request):
    return HttpResponse("The new url for views")

@api_view(['POST'])
def add(request):
    num1=request.data.get('num1')
    num2=request.data.get('num2')
    sum=num1+num2
    return HttpResponse(f"The sum of {num1} and {num2} is: {sum}")


