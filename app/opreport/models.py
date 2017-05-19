from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    OM_CHOICES = (
        ('east', 'East'),
        ('west', 'West'),
    )

    om = models.CharField(max_length=20, choices=OM_CHOICES)
    location = models.CharField(max_length=100)
    job_no = models.CharField(max_length=30)
    project_name = models.TextField()
    spk_no = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    statuspr_material = models.IntegerField(default=0)
    statuspr_fabrication = models.IntegerField(default=0)
    statuspr_installation = models.IntegerField(default=0)
    invoice_tahap1 = models.CharField(max_length=100, blank=True, null=True)
    invoice_tahap2 = models.CharField(max_length=100, blank=True, null=True)
    invoice_tahap3 = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=220, blank=True, null=True)

    def __unicode__(self):
		return self.project_name


class Quotation(models.Model):
    tanggal = models.DateField()
    inquiry_no = models.CharField(max_length=50)
    quotation_no = models.CharField(max_length=20)
    costumer = models.CharField(max_length=100)
    desc_material = models.TextField()
    qty = models.IntegerField(default=0)
    unit = models.CharField(max_length=10)
    bid_price = models.CharField(max_length=50)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
		return self.costumer

class Tender(models.Model):
    OM_CHOICES = (
        ('east', 'East'),
        ('west', 'West'),
    )

    om = models.CharField(max_length=20, choices=OM_CHOICES)
    quotation_no = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    tender_name = models.CharField(max_length=200)
    rks_no = models.CharField(max_length=20)
    process_registration = models.CharField(max_length=10)
    process_aanwizing = models.CharField(max_length=10)
    process_openbid = models.CharField(max_length=10)
    # process_registration = models.DateField()
    # process_aanwizing = models.DateField()
    # process_openbid = models.DateField()
    addcost_bidbond = models.CharField(max_length=100)
    addcost_reffbank = models.CharField(max_length=100)
    addcost_document = models.CharField(max_length=100)
    remark = models.CharField(max_length=220)

    def __unicode__(self):
		return self.quotation_no

class Delivery(models.Model):
    om = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_no = models.CharField(max_length=200)
    description_material = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    value_dpp = models.CharField(max_length=200)
    value_ppn = models.CharField(max_length=200)
	progress_dono = models.CharField(max_length=200)
    progress_leadtime = models.CharField(max_length=200)
    progress_pickup = models.CharField(max_length=200)
    expedisi = models.CharField(max_length=200)
    order_status = models.CharField(max_length=200)

    def __unicode__(self):
		return self.job_no
















#
