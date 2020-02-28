from django.shortcuts import render

def home(request):
    
    return render(request, 'home.html')
	
def vankeus(request):

    return render(request, 'vankeus.html')
	
	
def backgrounds(request):

    return render(request, 'backgrounds.html')
	
def contact(request):

    return render(request, 'contact.html')
	
def historia(request):

    return render(request, 'historia.html')
	
def rules(request):

    return render(request, 'rules.html')
	



# Create your views here.
