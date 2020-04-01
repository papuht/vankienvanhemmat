from django import forms

class ApplicationForm(forms.Form):
    your_name = forms.CharField(label='Nimi:', max_length=100)
    email = forms.EmailField(label='Sähköpostiosoite:', max_length=100)
    address = forms.CharField(label='Osoite:', max_length=100)
    phone = forms.CharField(label='Puh. numero:', max_length=100)
    username = forms.CharField(label='Haluamasi käyttäjätunnus:', max_length=100)
    reason = forms.CharField(label='Miksi haluan liittyä:', widget=forms.Textarea, max_length=30000)
	
	
	
	