from django import forms
from Administrator.models import Administrator
class AdministratorForm(forms.ModelForm):
class Meta:
    model = Administrator
    fields = "__all__"