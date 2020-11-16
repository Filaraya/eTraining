from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

context={}
def index(request):

# Render the HTML template index.html
    return render(request, 'blog/index.html', context=context)