from django.forms import ModelForm
from . import models


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['city'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['street'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['account_number'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['image_logo'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = models.Company
        fields = ['brand', 'city', 'street', 'account_number', 'image_logo']
