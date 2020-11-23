from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Module, Instructor, Content_Type, ModuleInstance 
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_modules = Module.objects.all().count()   
    num_instructors = Instructor.objects.count()
    
    context = {
        'num_modules': num_modules,
        'num_instructors': num_instructors,
    }


# Render the HTML template index.html
    return render(request, 'blog/index.html', context=context)