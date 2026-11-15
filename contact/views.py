from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail 
from django.contrib import messages
from django.conf import settings

def send_message(request):

    myinfo = Info.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and subject and email and message:
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],      
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, 'Sorry, an error occurred while sending the message. Please try again.')
        else:
            messages.error(request, 'Please fill in all required fields.')

        return redirect('contact')


    context = {
        'myinfo': myinfo
    }
    return render(request, 'contact/contact.html', context=context)