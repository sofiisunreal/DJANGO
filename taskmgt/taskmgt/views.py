from django.http import HttpResponse
from rest_framework.decorators import api_view

def home(request):
    return HttpResponse("Welcome")

@api_view(['POST'])
def subtraction(request):
    num1=request.data.get('num1')
    num2=request.data.get('num2')
    diff=num1-num2
    return HttpResponse(f"The difference of {num1} and {num2} is: {diff} ")
