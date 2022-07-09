from django import forms
from django.core.validators import RegexValidator

from taxi.models import Driver

LICENSE_VALIDATION_REG_EXP = "^[A-Z]{3}\d{5}"
LICENSE_VALIDATION_HELP_TEXT = "License number format: AAA00000"


class DriverCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    license_number = forms.CharField(required=True,
                                     min_length=8,
                                     max_length=8,
                                     validators=[RegexValidator(
                                         LICENSE_VALIDATION_REG_EXP)],
                                     help_text=LICENSE_VALIDATION_HELP_TEXT)

    class Meta:
        model = Driver
        fields = ["username", "password", "first_name", "last_name", "email",
                  "license_number"]


class DriverUpdateForm(forms.ModelForm):
    license_number = forms.CharField(required=True,
                                     min_length=8,
                                     max_length=8,
                                     validators=[RegexValidator(
                                         LICENSE_VALIDATION_REG_EXP)],
                                     help_text=LICENSE_VALIDATION_HELP_TEXT)

    class Meta:
        model = Driver
        fields = ["first_name", "last_name", "email", "license_number"]


class CarSearchForm(forms.Form):
    model = forms.CharField(max_length=70, required=False, label="",
                            widget=forms.TextInput(attrs={
                                "placeholder": "Search by model"}))