from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import * 

router=DefaultRouter()
router.register('task', TaskViewSet),

urlpatterns=[
    path('client/<int:pk>',ClientDetailView.as_view()),
    path('employee/<int:pk>',EmployeeDetailView.as_view()),
    path('employees',EmployeeListView.as_view()),
    path('workers',WorkerListView.as_view()),
    path('',include(router.urls))

]

