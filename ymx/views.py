from django.views import generic
from .models import Company
from django.shortcuts import render
# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    my_ompany = Company.objects

    # Render the HTML template index.html with the data in the context variable
    return render(
        request, 'ymx/index.html'
    )


'''
class IndexView(generic.DetailView):
    template_name = 'ymx/index.html'
    context_object_name = 'CompanyDetail'
    model = Company
'''


