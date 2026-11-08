from django import forms  

from . models import *



class ApllyForm(forms.ModelForm):

    class Meta :
        model =  Apply
        fields = ['name' , 'email' , 'phone' , 'cv' , 'websit' , 'cover_letter']




class AddForm(forms.ModelForm):
    class Meta :
        model = job
        fialds = '__all__'
        exclude = ( 'user' , 'slug',)  