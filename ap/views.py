from django.shortcuts import render
from .models import Jobs
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request, 'home.html')

class JobListView(ListView):
    model = Jobs
    jobs = Jobs.objects.all()

    template_name = 'job_list.html'
    context_object_name = 'jobs'
