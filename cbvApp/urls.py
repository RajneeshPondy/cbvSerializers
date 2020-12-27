from django.urls import path, include
from .views import StudentList, StudentDetail, StudentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    # path('students/', StudentList.as_view()),
    # path('students/<int:pk>/', StudentDetail.as_view())
    path('', include(router.urls))
]

