from django import forms
from .models import Project, Quotation, Tender, Delivery, Ticket, Cashadv, BudgetingRealisasi
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div
from parsley.decorators import parsleyfy

@parsleyfy
class ProjectForm(forms.ModelForm):
    job_no = forms.IntegerField()
    value = forms.DecimalField()
    statuspr_material = forms
    statuspr_fabrication = forms.IntegerField()
    statuspr_installation = forms.IntegerField()
    invoice_tahap1 = forms.DecimalField()
    invoice_tahap2 = forms.DecimalField()
    invoice_tahap3 = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = Project
        fields = ('om', 'location', 'job_no', 'project_name',
                'spk_no', 'value', 'statuspr_material',
                'statuspr_fabrication', 'statuspr_installation',
                'invoice_tahap1', 'invoice_tahap2', 'invoice_tahap3', 'remark')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_project_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('om', 'location', 'job_no', 'project_name',
                    'spk_no',
                     css_class='col-md-6'),

                Div('value', 'statuspr_material','statuspr_fabrication', 'statuspr_installation',
                    'invoice_tahap1', 'invoice_tahap2', 'invoice_tahap3', 'remark',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )


class QuotationForm(forms.ModelForm):
    quotation_no = forms.IntegerField()
    qty = forms.DecimalField()
    bid_price = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = Quotation
        fields = ('tanggal', 'inquiry_no', 'quotation_no', 'costumer',
                'desc_material', 'qty', 'unit', 'bid_price', 'status', )

    def __init__(self, *args, **kwargs):
        super(QuotationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_quotation_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('tanggal', 'inquiry_no', 'quotation_no', 'costumer','desc_material',
                     css_class='col-md-6'),

                Div( 'qty', 'unit', 'bid_price', 'status',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )

# TENDER FORMS
class TenderForm(forms.ModelForm):
    quotation_no = forms.IntegerField()
    addcost_bidbond = forms.DecimalField()
    addcost_reffbank = forms.DecimalField()
    addcost_document = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = Tender
        fields = ('om','quotation_no','location','tender_name','rks_no',
                'process_registration','process_aanwizing','process_openbid',
                'addcost_bidbond','addcost_reffbank','addcost_document','remark', )

    def __init__(self, *args, **kwargs):
        super(TenderForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_tender_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('om','quotation_no','location','tender_name',
                    'rks_no','process_registration','process_aanwizing',
                     css_class='col-md-6'),

                Div('process_openbid', 'addcost_bidbond','addcost_reffbank',
                    'addcost_document','remark',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )

# DELIVERY FORMS
class DeliveryForm(forms.ModelForm):
    value_dpp = forms.DecimalField()
    value_ppn = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = Delivery
        fields = ('om','location','job_no','description_material','vendor','value_dpp',
                'value_ppn','progress_dono','progress_leadtime',
                'progress_pickup','expedisi','order_status',)

    def __init__(self, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_delivery_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('om','location','job_no','description_material','vendor','value_dpp',
                     css_class='col-md-6'),

                Div('value_ppn','progress_dono','progress_leadtime','progress_pickup','expedisi','order_status',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )

# TICKET PROJECT
class TicketForm(forms.ModelForm):
    cost = forms.DecimalField()
    payment = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = Ticket
        fields = ('date_flight','om','name','customer','id_jobno','purpose','cost','payment')

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_ticket_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('date_flight','om','name','customer',
                     css_class='col-md-6'),

                Div('id_jobno','purpose','cost','payment',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )

# Cashadv
class CashadvForm(forms.ModelForm):
    id_jobno = forms.IntegerField()
    car = forms.DecimalField()
    pi = forms.DecimalField()
    actual_cost = forms.DecimalField()
    receive_payment = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = Cashadv
        fields = ('date_request','om','name_of_payee','customer','id_jobno','purpose','car','pi','actual_cost','receive_payment','status')

    def __init__(self, *args, **kwargs):
        super(CashadvForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_cashadv_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('date_request','om','name_of_payee','customer','id_jobno',
                     css_class='col-md-6'),

                Div('purpose','car','pi','actual_cost','receive_payment','status',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )


# BudgetingRealisasi
class BudgetingRealisasiForm(forms.ModelForm):
    januari_budgeting = forms.DecimalField()
    januari_realisasi = forms.DecimalField()
    februari_budgeting = forms.DecimalField()
    februari_realisasi = forms.DecimalField()
    maret_budgeting = forms.DecimalField()
    maret_realisasi = forms.DecimalField()
    april_budgeting = forms.DecimalField()
    april_realisasi = forms.DecimalField()
    mei_budgeting = forms.DecimalField()
    mei_realisasi = forms.DecimalField()
    juni_budgeting = forms.DecimalField()
    juni_realisasi = forms.DecimalField()
    juli_budgeting = forms.DecimalField()
    juli_realisasi = forms.DecimalField()
    agustus_budgeting = forms.DecimalField()
    agustus_realisasi = forms.DecimalField()
    september_budgeting = forms.DecimalField()
    september_realisasi = forms.DecimalField()
    oktober_budgeting = forms.DecimalField()
    oktober_realisasi = forms.DecimalField()
    november_budgeting = forms.DecimalField()
    november_realisasi = forms.DecimalField()
    desember_budgeting = forms.DecimalField()
    desember_realisasi = forms.DecimalField()

    class Meta:
        parsley_namespace = 'parsley'
        model = BudgetingRealisasi
        fields = ('location','coa','deskripsi')

    def __init__(self, *args, **kwargs):
        super(BudgetingRealisasiForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_budgeting_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('location','coa','deskripsi',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-12'),
                css_class='row'
            ),
        )










#
