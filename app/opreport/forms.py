from django import forms
from .models import Project, Quotation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div


class ProjectForm(forms.ModelForm):
    class Meta:

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
    class Meta:

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
