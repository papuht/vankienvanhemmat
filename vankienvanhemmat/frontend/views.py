from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ApplicationForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')
	
	
def home(request):
    
    return render(request, 'frontend/home.html')
	
def vankeus(request):

    return render(request, 'frontend/vankeus.html')
	
	
def backgrounds(request):

    return render(request, 'frontend/backgrounds.html')
	
def contact(request):

    return render(request, 'frontend/contact.html')
	
def historia(request):

    return render(request, 'frontend/historia.html')
	
def rules(request):

    return render(request, 'frontend/rules.html')
	
	


def get_application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            username = form.cleaned_data['username']
            reason = form.cleaned_data['reason']
			
            subject = "Jäsenhakemus"
            message = '''Nimi: {}, 
                       Sähköpostiosoite: {},
					   Osoite: {},
					   Puh. numero: {},
					   Käyttäjätunnus: {},
					   Syy liittyä: {}'''.format(your_name, email, address, phone, username, reason)
			
            recipients = ['admin@vankienvanhemmat.fi']
            sender = email

            send_mail(subject, message, sender, recipients)
    
            return HttpResponseRedirect('/')

    
    else:
        form = ApplicationForm()

    return render(request, 'application.html', {'form': form})