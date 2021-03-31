from django.shortcuts import get_object_or_404
from django.apps import apps
from django.http.response import JsonResponse
from django.contrib.contenttypes.models import ContentType
from .models import ObjectFile


def upload_file(request, app_label, model_name, object_id):
    """
    Загрузка файла
    """
    model = apps.get_model(app_label=app_label,
                           model_name=model_name)
    obj = get_object_or_404(model, pk=object_id)
    content_type = ContentType.objects.get(app_label=app_label, model=model_name)
    file = request.FILES.get('file')
    file = ObjectFile.objects.create(file=file, object_id=obj.pk, content_type=content_type)
    return JsonResponse({'download_url': file.file.url,
                         'delete_url': file.delete_url})


def delete_file(request, file_id):
    """
    Удаление файла
    """
    file = get_object_or_404(ObjectFile, pk=file_id)
    file.delete()
    return JsonResponse({'status': 'success'})
