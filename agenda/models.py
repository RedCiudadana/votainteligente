# coding=utf-8
from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Activity(models.Model):
    date = models.DateTimeField()
    url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=1024)
    description = models.CharField(blank=True,max_length=1024)
    long_description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="agenda/activities/",
                                        null=True,
                                        blank=True,
                                        verbose_name=_(u'Una imagen para el evento'),
                                        help_text=_(u'será la imagen que utilicemos en la lista de eventos'))
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True)
    object_id = models.CharField(max_length=1024,blank=True,
                                            null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.description

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-date']
