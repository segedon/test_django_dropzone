from django import template
from ..models import ObjectFile


register = template.Library()

@register.simple_tag
def upload_url_for(_object):
    return ObjectFile.upload_url_for_object(_object)


@register.simple_tag
def get_files_for(_object):
    return ObjectFile.objects.object_files(_object)


@register.inclusion_tag('django_dropzone/simple_form.html')
def simple_form_for(_object):
    upload_url = upload_url_for(_object)
    return {'upload_url': upload_url}


@register.inclusion_tag('django_dropzone/form_with_files.html')
def form_with_files_for(_object):
    upload_url = upload_url_for(_object)
    files = ObjectFile.objects.object_files(_object)
    return {'files': files,
            'upload_url': upload_url}


@register.inclusion_tag('django_dropzone/dropzone_js.html')
def include_dropzone_js():
    return {}


@register.inclusion_tag('django_dropzone/dropzone_css.html')
def include_dropzone_css():
    return {}