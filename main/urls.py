from django.urls import path
from .views import TestObjectListView, TestObjectDetailView

urlpatterns = [
    path('list/', TestObjectListView.as_view()),
    path('object/<int:pk>', TestObjectDetailView.as_view(), name='object_detail'),
]