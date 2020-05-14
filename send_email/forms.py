from django import forms


#################################
# Email form
#################################
class EmailForm(forms.Form):
    contact_email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Email address'}))
    email_content = forms.CharField(min_length=5, widget=forms.Textarea(attrs={'id': 'editor1', 'class' : 'form-control', 'placeholder' : 'Example: Our best offer for xxx'}), required=True)
