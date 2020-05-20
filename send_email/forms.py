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
    email_content = forms.CharField(min_length=1, widget=forms.Textarea(attrs={'id': 'editor1', 'class' : 'form-control', 'placeholder' : 'Usage: type \'send\' here, then click the button below to fire off template emails to all our lovely clients.\n\n\nDev update: \n- For now it supports sending a template email to all clients. \n- Allow qucik-view to current template.\n\nMore features are coming soon :>'}))