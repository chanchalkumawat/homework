from django import forms
from django.forms.widgets import HiddenInput
from  django.core import validators
from second_app.models import User


class FormDetails(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        #exclude=['first_name']
        #field=['first_name']

#class FormDetails(forms.Form):
  #  first_name=forms.CharField()
 #   last_name=forms.CharField()
  #  email_id=forms.EmailField()
   # verify_email=forms.EmailField()
   # botcatcher=forms.CharField(required=False,widget=HiddenInput,validators=[validators.MaxLengthValidator(0)])


#def clean(self):
  #  get_all=super().clean()
    #if get_all['email_id']!=get_all['verify_email']:
     #   raise forms.ValidationError("email is not matched")