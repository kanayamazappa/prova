# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('facebookId', 'name', 'link', 'gender')