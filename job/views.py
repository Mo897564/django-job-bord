from django.shortcuts import render , get_object_or_404 , redirect

from . models import *

# Create your views here.

def job_list(request):

    job_list = job.objects.all()

    context = {
            'job_list' : job_list
        
        }

    return render(request , 'jobs/jobs.html' , context=context)





def job_details(request , id):
        
    job_details = job.objects.get(id=id)

    context = {
            'job' : job_details
        
        }

    return render(request , 'jobs/job_details.html' , context=context)
