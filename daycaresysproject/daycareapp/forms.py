from django import forms
from django.forms import ModelForm
from .models import *

# Create a form


class BabysiiterregForm(ModelForm):
    class Meta:
        model = Babysitter
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control "}),
            "last_name": forms.TextInput(attrs={"class": "form-control "}),
            "date_of_birth": forms.TextInput(
                attrs={"class": "form-control  datetimepicker-input", "type": "date"}
            ),
            "nin": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control "}),
            "email": forms.TextInput(attrs={"class": "form-control "}),
            "district": forms.TextInput(attrs={"class": "form-control "}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "gender":forms.Select(attrs={"class": "form-control", })
        }


class BabyregForm(ModelForm):
    class Meta:
        model = Baby
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control "}),
            "last_name": forms.TextInput(attrs={"class": "form-control "}),
            "date_of_birth": forms.TextInput(
                attrs={"class": "form-control  datetimepicker-input", "type": "date"}
            ),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "parent_name": forms.TextInput(attrs={"class": "form-control "}),
            "guardian_name": forms.TextInput(attrs={"class": "form-control "}),
            "parent_phonenummber": forms.TextInput(attrs={"class": "form-control "}),
            "guardian_phonenumber": forms.TextInput(attrs={"class": "form-control "}),
             "gender":forms.Select(attrs={"class": "form-control",})
        }


class ProcureForm(ModelForm):
    class Meta:
        model = Procure
        fields = "__all__"

        widgets ={
            "item":  forms.TextInput(attrs={"class": "form-control "}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
            "qty": forms.NumberInput(attrs={"class": "form-control"}),
           
        }

# class SchoolfeesForm(ModelForm):
#     class Meta:
#         model = Schoolfees
#         fields = ['type_of_payment','amount_paid','id']

#         widgets ={
#             "type":  forms.Select(attrs={"class": "form-control",}),
#             "amount_paid": forms.Select(attrs={"class": "form-control",}),
#             "id": forms.Select(attrs={"class": "form-control",}),
           
#         }


class DollssalesForm(ModelForm):
    class Meta:
        model = Dollsdashboard
        fields = ['customer_name','dollsbought',]

        widgets ={
            "customer_name":forms.TextInput(attrs={"class": "form-control "}),
            "dollsbought":forms.NumberInput(attrs={"class": "form-control"}),
        }

class SchoolfeesForm(forms.ModelForm):
    class Meta:
        model = Schoolfees
        fields = ['id', 'baby', 'type_of_payment', 'amount_paid']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['baby'].queryset = Baby.objects.all()
        self.fields['type_of_payment'].choices = Schoolfees.STUDY_CHOICES
        self.fields['amount_paid'].widget = forms.NumberInput()
        self.fields['amount_paid'].widget.attrs.update({'class': 'form-control'})   
        self.fields['type_of_payment'].widget.attrs.update({'class': 'form-control'})  
        self.fields['baby'].widget.attrs.update({'class': 'form-control'}) 
        # self.fields['id'].widget = forms.HiddenInput()
        # self.fields['id'].widget.attrs.update({'class': 'form-control'})   
        # self.fields['id'].widget.attrs.update({'value': '1'})
        # self.fields['id'].widget.attrs.update({'readonly': 'readonly'})
        # self.fields['id'].widget.attrs.update({'style': 'display:none'})
        # self.fields['baby'].widget.attrs.update({'style': 'display:none'}) 
        # self.fields['baby'].widget.attrs.update({'value': '1'}) 
        # self.fields['baby'].widget.attrs.update({'readonly': 'readonly'})   
        # self.fields['baby'].widget.attrs.update({'style': 'display:none'})
        # self.fields['baby'].widget.attrs.update({'value': '1'})
        # self.fields['baby'].widget.attrs.update({'readonly': 'readonly'})
        # self.fields['baby'].widget.attrs.update({'style': 'display:none'})