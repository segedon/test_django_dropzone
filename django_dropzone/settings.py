from django.conf import settings
from django.core.files.storage import default_storage


STORAGE = getattr(settings, 'DROPZONE_STORAGE_OBJECT', default_storage)
UPLOAD_TO = getattr(settings, 'UPLOAD_TO', '')