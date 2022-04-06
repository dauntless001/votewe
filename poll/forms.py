from django import forms
from poll.models import PollingUnit


class PollingUnitForm(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PollingUnitForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'