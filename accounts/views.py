from django.shortcuts import render , redirect

from django.contrib.auth import  login , authenticate

from . form import *
from . models import *

# Create your views here.






def SignUp(request):

   if request.method =='POST':
      signform = SignupForm(request.POST)
      if signform.is_valid():
         user = signform.save()

         # username = signform.cleaned_data['username']
         # password = signform.cleaned_data['password1']
         # user = authenticate(username=username , password=password)
         login(request ,user)

         return redirect('profile')
  
   else:
      signform = SignupForm()


   
   context = {
   
     'signform' : signform

   }

   
   return render(request , 'accounts/signup.html' , context=context)






def profile(request):

   profile = Profile.objects.get(user= request.user)

   context = {

      'profile' : profile 
   
   }


   return render(request , 'accounts/profile.html' , context=context)





def profile_edit(request):

   profile = Profile.objects.get(user= request.user)

   if request.method == 'POST':

      user_edit = UserForm_Edit(request.POST , instance= request.user)
      profile_edit = ProfileForm_Edit(request.POST , request.FILES , instance= profile)

      if user_edit.is_valid() and profile_edit.is_valid():
         user_edit.save()
         myprofile = profile_edit.save(commit=False)

         myprofile.user = request.user
         myprofile.save()

         return redirect('profile')
      

   else:
      user_edit = UserForm_Edit(instance= request.user)
      profile_edit = ProfileForm_Edit(instance= profile)


   context = {

      'user_edit' : user_edit ,
      'profile_edit' : profile_edit
   }

   return render(request , 'accounts/profile_edit.html' , context=context)