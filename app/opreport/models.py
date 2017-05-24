from __future__ import unicode_literals

from django.db import models

OM_CHOICES = (
    ('east', 'East'),
    ('west', 'West'),
)

class Project(models.Model):
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
    om = models.CharField(max_length=20, choices=OM_CHOICES)
    quotation_no = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    tender_name = models.CharField(max_length=200)
    rks_no = models.CharField(max_length=20)
    process_registration = models.CharField(max_length=10)
    process_aanwizing = models.CharField(max_length=10)
    process_openbid = models.CharField(max_length=10)
    addcost_bidbond = models.CharField(max_length=100)
    addcost_reffbank = models.CharField(max_length=100)
    addcost_document = models.CharField(max_length=100)
    remark = models.CharField(max_length=220)

    def __unicode__(self):
		return self.quotation_no

class Delivery(models.Model):
    om = models.CharField(max_length=20, choices=OM_CHOICES)
    job_no = models.CharField(max_length=200)
    description_material = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    value_dpp = models.CharField(max_length=200)
    value_ppn = models.CharField(max_length=200)
    progress_dono = models.CharField(max_length=200)
    progress_leadtime = models.CharField(max_length=200)
    progress_pickup = models.CharField(max_length=200)
    expedisi = models.CharField(max_length=200)
    order_status = models.CharField(max_length=200)

    def __unicode__(self):
		return self.job_no

class Ticket(models.Model):
    date_flight = models.CharField(max_length=150)
    om = models.CharField(max_length=20, choices=OM_CHOICES)
    name = models.CharField(max_length=150)
    customer = models.CharField(max_length=150)
    id_jobno = models.CharField(max_length=150)
    purpose = models.CharField(max_length=150)
    cost = models.CharField(max_length=150)
    payment = models.CharField( max_length=150)

    def __unicode__(self):
		return self.date_flight

class Cashadv(models.Model):
    date_request = models.DateField()
    om = models.CharField(max_length=20, choices=OM_CHOICES)
    name_of_payee = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    id_jobno = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    pi = models.CharField(max_length=100)
    actual_cost = models.CharField(max_length=100)
    receive_payment = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __unicode__(self):
		return self.purpose

# Budgeting terakhir cz rada ribet
class BudgetingRealisasi(models.Model):
    LOCATION_CHOICE = (
        ('kendari','Kendari'),
        ('teluk_sirih','Teluk SIrih'),
    )

    location = models.CharField(max_length=100)
    coa = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=100)
    #Budgeting Realisasi
    januari_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    januari_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    februari_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    februari_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    maret_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    maret_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    april_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    april_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    mei_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    mei_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    juni_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    juni_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    juli_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    juli_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    agustus_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    agustus_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    september_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    september_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    oktober_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    oktober_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    november_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    november_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    desember_budgeting = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    desember_realisasi = models.DecimalField(decimal_places=2, max_digits=12, default=0)

    def __unicode__(self):
		return self.deskripsi













#
