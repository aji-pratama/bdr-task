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
