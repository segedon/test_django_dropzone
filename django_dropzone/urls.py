from django.urls import path
from .views import upload_file, delete_file


urlpatterns = [
    path('upload_file/<str:app_label>/<str:model_name>/<str:object_id>/',
         upload_file, name='dropzone_upload_file'),
    path('delete_file/<int:file_id>/', delete_file, name='dropzone_delete_file'),
]