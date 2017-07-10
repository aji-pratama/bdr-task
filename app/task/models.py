from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model as user_model
User = user_model()
# from app.pengguna.models import Atasans, Staffs

class Task(models.Model):
    title = models.CharField(max_length=200)
    approval_status = models.BooleanField()
    done_status = models.BooleanField()
    keterangan = models.CharField(max_length=300, blank=True, null=True)
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    created_by = models.ForeignKey(User)
    approval_by = models.ForeignKey(User, related_name='user_approval_by', null=True, blank=True)
    doing_date = models.DateField()
    update_info = models.TextField(blank=True)

    def __unicode__(self):
        return self.title
