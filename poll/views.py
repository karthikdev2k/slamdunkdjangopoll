from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #Write code implementation here
    # For Slamdunk
    html = "<html><body>Welcome to webpoll home!</body></html>"
    return HttpResponse(html)