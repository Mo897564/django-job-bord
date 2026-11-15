from django.shortcuts import render

# Create your views here.
from job.models import job



def Home_index(request):

    list_job = job.objects.all().order_by('-id')[:10]


    context = {
        'list_job' : list_job

    }
    return render(request , 'home/index.html',context=context)