from django import forms
from . models import ATM

class AtmForm(forms.ModelForm):
     class Meta:
          model=ATM
          fields=['name','account_no','phone','email','aadhar','dob','photo','gender']