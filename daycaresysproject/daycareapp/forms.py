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

class SchoolfeesForm(ModelForm):
    class Meta:
        model = Schoolfees
        fields = ['type_of_payment','amount_paid','id']

        widgets ={
            "type":  forms.Select(attrs={"class": "form-control",}),
            "amount_paid": forms.Select(attrs={"class": "form-control",}),
            "id": forms.Select(attrs={"class": "form-control",}),
           
        }


class DollssalesForm(ModelForm):
    class Meta:
        model = Dollsdashboard
        fields = ['customer_name','dollsbought',]

        widgets ={
        "customer_name":forms.TextInput(attrs={"class": "form-control "}),
        "dollsbought":forms.NumberInput(attrs={"class": "form-control"}),



        }








      


        
  