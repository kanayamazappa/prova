# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(models.Model):
    facebookId = models.BigIntegerField(verbose_name=u'Facebook ID')
    name = models.CharField(max_length=150, verbose_name=u'Nome')
    link = models.CharField(max_length=150, verbose_name=u'Link')
    gender = models.CharField(max_length=50, verbose_name=u'Gênero', null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name=u'Ativo')
    
    class Meta:
        verbose_name = u'Person'
        verbose_name_plural = u'Persons'
        ordering = ['name']
        
    def __unicode__(self):
        return u'%s' % (self.name)

class Log(models.Model):
    owner = models.ForeignKey(User, verbose_name=u'Usuário')
    person = models.ForeignKey(Person, null=True, blank=True)
    action = models.CharField(max_length=50, verbose_name=u'Ação')
    register = models.DateTimeField(auto_now_add=True, verbose_name=u'Data de Cadastro')
    
    class Meta:
        verbose_name = u'log'
        verbose_name_plural = u'Logs'
        ordering = ['-register']
        
    def __unicode__(self):
        if self.person:
            return u'%s - %s - %s' % (self.owner, self.person, self.action)
        else:
            return u'%s - %s' % (self.owner, self.action)