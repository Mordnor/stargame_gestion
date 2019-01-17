# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from multiselectfield import MultiSelectField


OTHERS_CHOICES = (
    ('batterie', 'Batterie'),
    ('sacoche', 'Sacoche'),
    ('souris', 'Souris'),
    ('chargeur', 'Chargeur'),
)

STATUS_SHEET = (
    ('diagnostique', 'Diagnostique'),
    ('intervention', 'Intervention'),
)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='first_name')
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=70, null=False, blank=False)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Sheet(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    statut = models.CharField(max_length=40, choices=STATUS_SHEET)
    other = MultiSelectField(max_length=40, choices=OTHERS_CHOICES, null=True, blank=True )
    reason = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    resolution = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    guarantee = models.BooleanField(default=False)

    def datepublished(self):
        return self.date.strftime('%d-%m-%Y')
        

class Request(models.Model):
    customer = models.ForeignKey(Customer)
    reason = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def datepublished(self):
        return self.date.strftime('%d/%m/%Y')




