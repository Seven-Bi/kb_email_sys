#############################
# Author: Chen Bi
# Date: 18 May 2020
#############################

from django import forms


#################################
# Email form
#################################
class EmailForm(forms.Form):
    # contact_email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control', 'aria-label': 'Text input with dropdown button', 'placeholder' : 'Email address'}))
    email_content = forms.CharField(min_length=5, widget=forms.Textarea(attrs={'id': 'editor1', 'class' : 'form-control', 'placeholder' : 'Example: Our best offer for xxx'}), required=True)