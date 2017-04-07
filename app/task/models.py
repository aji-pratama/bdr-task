from __future__ import unicode_literals
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)     # (str)
    approval_status = models.BooleanField(default=False)     # (boolean)
    done_status = models.BooleanField(default=False)     # (boolean)
    keterangan = models.TextField(blank=True)     # (string, if done_status == 0)
    created_date = models.DateField() #(_("Date"), default=datetime.date.today)     # (date)
    created_by = models.ForeignKey(Akun)     # (ForeignKey User staff)
    approval_by = models.ForeignKey('Akun', related_name='+', null=True, blank=True)     # (ForeignKey User atasan)
    doing_date = models.DateField()     # (created_date + 1, if week_array 0-4 else + 2)

    	def __unicode__(self):
    		return self.created_by
