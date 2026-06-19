from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import * 
# creating router object from the default router class
router=DefaultRouter()
router.register('departments', DepartmentViewSet)

urlpatterns=[
    path('employees',EmployeeListCreateView.as_view()),
    path('employees/<int:pk>',EmployeeDetailView.as_view()),
    path('',include(router.urls))

]

