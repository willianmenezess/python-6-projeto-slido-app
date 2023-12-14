from django import forms
from slido_app.models import Visitor


class CreateVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = "__all__"
