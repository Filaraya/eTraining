from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from blog.models import Module, Instructor, Content_Type, ModuleInstance 
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_modules = Module.objects.all().count()   
    num_instructors = Instructor.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_modules': num_modules,
        'num_instructors': num_instructors,
        'num_visits': num_visits,
    }


# Render the HTML template index.html
    return render(request, 'blog/index.html', context=context)

class ModuleListView(ListView):
    """Generic class-based list view for module"""
    #model= Module
    queryset = Module.objects.all()


class ModuleDetailView(DetailView):
    template_name = 'blog/module_detail.html'
    queryset = Module.objects.all()

    def get_object(self):

        id= self.kwargs.get("id")
        return get_object_or_404(Module, id=id)

class InstructorListView(ListView):
    """Generic class-based list view for a list of instructors."""
    model = Instructor
    paginate_by = 10


class InstructorDetailView(DetailView):
    """Generic class-based detail view for an instructor."""
    model = Instructor