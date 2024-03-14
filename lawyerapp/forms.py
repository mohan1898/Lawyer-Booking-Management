from django import forms
from lawyerapp.models import Lawyer


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = "__all__"
