from django import forms
from myform.forms import forms

class InputForm(forms.Form):

    first_name=forms.CharField(max_length=255)
    last_name=forms.CharField(max_length=255)
    roll_no=forms.IntegerField(help_text="Enter only numbers")
    password=forms.CharField(widget=forms.PasswordInput())
    