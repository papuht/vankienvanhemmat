from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ApplicationForm

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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('frontend/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationForm()

    return render(request, 'application.html', {'form': form})