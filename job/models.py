from django.db import models

# Create your models here.


class Categry(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name




class job(models.Model):

    JOP_TYPE =(
            ("Full Time" , "Full Time"),
            ("Part Time" , "Part Time"),
        
    )


    titel = models.CharField(max_length=100)
    # location = models.
    job_type = models.CharField(max_length=20 , choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(default=0)
    categry = models.ForeignKey(Categry , on_delete=models.CASCADE , null=True , blank=True)
    experince = models.IntegerField(default=1)

    def __str__(self):
        return self.titel



