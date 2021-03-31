from django.views.generic import ListView, DetailView
from .models import TestObject


class TestObjectListView(ListView):
    template_name = 'main/list.html'
    model = TestObject
    context_object_name = 'objects'


class TestObjectDetailView(DetailView):
    template_name = 'main/detail.html'
    model = TestObject
    context_object_name = 'object'



