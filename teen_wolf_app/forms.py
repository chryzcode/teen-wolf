from django import forms

class ContactForm(forms.Form):
    title = forms.CharField(max_length=300)
    contact_mail = forms.CharField(max_length=300)
    content = forms.Textarea()


        