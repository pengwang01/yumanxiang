from django.views import generic
from .models import company
# Create your views here.


class IndexView(generic.DetailView):
    template_name = 'ymx/index.html'
    context_object_name = 'CompanyDetail'
    model = company