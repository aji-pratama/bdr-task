from __future__ import unicode_literals
import os
from django.db import models
from django.conf import settings

class Pkt(models.Model):
    KODE_CHOICES = (
        ('standard', 'Standard'),
        ('mandatory', 'Mandatory'),
        ('finance', 'Finance'),
        ('mandatory_tek', 'Mandatory Teknis')
    )

    teks = models.CharField(max_length=200)
    koef = models.IntegerField()
    kode = models.CharField(max_length=100, choices=KODE_CHOICES)

    def __unicode__(self):
        return self.teks

class Datas(models.Model):
    data1 = models.IntegerField(null=True, blank=True)
    data2 = models.IntegerField(null=True, blank=True)
    data3 = models.IntegerField(null=True, blank=True)
    data4 = models.IntegerField(null=True, blank=True)
    data5 = models.IntegerField(null=True, blank=True)
    data6 = models.IntegerField(null=True, blank=True)
    data7 = models.IntegerField(null=True, blank=True)
    data8 = models.IntegerField(null=True, blank=True)
    data9 = models.IntegerField(null=True, blank=True)
    data10 = models.IntegerField(null=True, blank=True)
    data11 = models.IntegerField(null=True, blank=True)
    data12 = models.IntegerField(null=True, blank=True)
    data13 = models.IntegerField(null=True, blank=True)
    data14 = models.IntegerField(null=True, blank=True)
    data15 = models.IntegerField(null=True, blank=True)
    data16 = models.IntegerField(null=True, blank=True)
    data17 = models.IntegerField(null=True, blank=True)
    data18 = models.IntegerField(null=True, blank=True)
    data19 = models.IntegerField(null=True, blank=True)
    data20 = models.IntegerField(null=True, blank=True)
