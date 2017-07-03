# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import getcontext

class Budgeting(models.Model):
    TYPE_PROPOSAL_CHOICES = (
        ('ADM', 'ADM'),
        ('OPR', 'OPR'),
    )

    unit = models.CharField(max_length=40, null=True, blank=True, default='')
    departement = models.CharField(max_length=40, null=True, blank=True, default='')
    divisi = models.CharField(max_length=40, null=True, blank=True, default='')
    jobid = models.CharField(max_length=30, blank=False, null=False)
    nodoc = models.CharField(max_length=40, blank=False, null=False)
    type_proposal = models.CharField(max_length=26, choices=TYPE_PROPOSAL_CHOICES)
    date = models.DateField()
    amount = models.DecimalField(max_digits=13, decimal_places=2, default=0, null=True)
    disc = models.DecimalField(max_digits=13, decimal_places=2, default=0, null=True)
    tax = models.CharField(max_length=100, default='', null=True)
    total_amount = models.DecimalField(max_digits=13, decimal_places=2, default=0, null=True)
    remark = models.CharField(max_length=100, default='', null=True)

    def __unicode__(self):
        return self.nodoc

class Item(models.Model):
    coa = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=220)
    qty = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    tot_amount = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    budgeting = models.ForeignKey(Budgeting, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ('description',)


# Create your models here.
