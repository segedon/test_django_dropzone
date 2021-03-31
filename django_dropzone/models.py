from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .settings import STORAGE, UPLOAD_TO


class ObjectFileManager(models.Manager):
    def object_files(self, _object: models.Model):
        content_type = ContentType.objects.get_for_model(_object)
        return self.filter(object_id=_object.id, content_type__id=content_type.id)


class ObjectFile(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(db_index=True, max_length=64)
    content_object = GenericForeignKey('content_type', 'object_id')
    file = models.FileField(storage=STORAGE, upload_to=UPLOAD_TO)

    objects = ObjectFileManager()

    @staticmethod
    def upload_url_for_object(_object: models.Model):
        return reverse('dropzone_upload_file',
                       kwargs={
                           'app_label': _object._meta.app_label,
                           'model_name': _object._meta.model_name,
                           'object_id': _object.pk
                       })

    @property
    def delete_url(self):
        return reverse('dropzone_delete_file', kwargs={'file_id': self.pk})
