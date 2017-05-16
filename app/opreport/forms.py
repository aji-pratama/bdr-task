from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('om', 'location', 'job_no', 'project_name',
                'spk_no', 'value', 'statuspr_material',
                'statuspr_fabrication', 'statuspr_installation',
                'invoice_tahap1', 'invoice_tahap2', 'invoice_tahap3')
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
