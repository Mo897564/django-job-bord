from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
from .filters import Filter_Job
from .models import *
from .form import *




# Create your views here.

def job_list(request):

    job_list = job.objects.all()


    filter  = Filter_Job(request.GET , queryset= job_list)
    job_list = filter.qs

    paginator = Paginator(job_list , 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)


    context = {
            'job_list' : page_obj ,
            'filter' : filter
        
        }

    return render(request , 'jobs/jobs.html' , context=context)





def job_details(request , slug):
        
    job_details = get_object_or_404(job , slug=slug)

    if request.method == 'POST':
        form_aplay = ApllyForm(request.POST , request.FILES)
        if form_aplay.is_valid():
            myform = form_aplay.save(commit=False)
            myform.job = job_details
            myform.save()
            return redirect('job_list')
    else:    

        form_aplay = ApllyForm()


    context = {
            'job' : job_details,
            'formapply' : form_aplay       
        }

    return render(request , 'jobs/job_details.html' , context=context)



@login_required
def add_job(request):

    if request.method == 'POST':
        form_add = AddForm(request.POST , request.FILES) 
        if form_add.is_valid():
            myform  = form_add.save(commit=False)
            myform.user = request.user
            myform.save() 

            return redirect('job_list')


    else:
        form_add =AddForm()        


    context = {

       'formadd' : form_add ,
        
        }
    
    
    return render(request , 'jobs/add_job.html' , context=context)