from django.db import models

# Create your models here.


class Categry(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name




class job(models.Model):

    JOB_TYPES =(
            ("Full Time" , "Full Time"),
            ("Part Time" , "Part Time"),
        
    )


    title = models.CharField(max_length=100)
    # location = models.
    job_type = models.CharField(max_length=20 , choices=JOB_TYPES)
    description = models.TextField(max_length=1000 , null=True, blank=True)
    img = models.ImageField(upload_to= 'photos/%y/%m/%d' , default= 'photo_default/default.png')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0 , null=True, blank=True)
    Category = models.ForeignKey(Categry , on_delete=models.SET_NULL , null=True , blank=True)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.titel



