from django.db import models
from django.urls import reverse


class TestObject(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('object_detail', kwargs={'pk': self.id})


