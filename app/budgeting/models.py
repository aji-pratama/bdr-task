# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    disc = models.DecimalField(max_digits=3, decimal_places=2)
    tax = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=13, decimal_places=2)
    remark = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nodoc

class Item(models.Model):
    coa = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=220)
    qty = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    tot_amount = models.DecimalField(max_digits=13, decimal_places=2)
    budgeting = models.ForeignKey(Budgeting, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ('description',)


# Create your models here.
