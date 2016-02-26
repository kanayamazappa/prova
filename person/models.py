# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    facebookId = models.BigIntegerField(verbose_name=u'Facebook ID')
    name = models.CharField(max_length=150, verbose_name=u'Nome')
    link = models.CharField(max_length=150, verbose_name=u'Link')
    gender = models.CharField(max_length=50, verbose_name=u'Gênero', null=True, blank=True)
    
    class Meta:
        verbose_name = u'Person'
        verbose_name_plural = u'Persons'
        ordering = ['name']
        
    def __unicode__(self):
        return u'%s' % (self.name)