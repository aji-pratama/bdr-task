from django import forms
from .models import Article
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div

class ArticleForm(forms.ModelForm):
    class Meta:

        model = Article
        fields = ('title','body')

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'project_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('title','body',
                    Div(
                        Div(Submit('save', 'Save', css_class='btn btn-primary btn-lg'), css_class='col-md-12'), css_class='row'
                    ),
                     css_class='col-md-6'),
                css_class='row'
            ),
        )
