from django import forms
from .models import Budgeting, Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div
from parsley.decorators import parsleyfy

@parsleyfy
class BudgetingForm(forms.ModelForm):
    class Meta:
        parsley_namespace = 'parsley'
        model = Budgeting
        fields = ('jobid',
                    'nodoc', 'type_proposal', 'date', 'amount',
                    'disc', 'tax', 'total_amount', 'remark', )

    def __init__(self, *args, **kwargs):
        super(BudgetingForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_budgeting_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('jobid', 'nodoc', 'type_proposal',
                    'date', 'amount',
                     css_class='col-md-6'),

                Div('disc', 'tax', 'total_amount', 'remark',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )
