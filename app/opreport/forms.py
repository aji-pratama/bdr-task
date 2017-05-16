from django import forms
from .models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div


class ProjectForm(forms.ModelForm):
    class Meta:

        model = Project
        fields = ('om', 'location', 'job_no', 'project_name',
                'spk_no', 'value', 'statuspr_material',
                'statuspr_fabrication', 'statuspr_installation',
                'invoice_tahap1', 'invoice_tahap2', 'invoice_tahap3')

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
                    'invoice_tahap1', 'invoice_tahap2', 'invoice_tahap3',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )
