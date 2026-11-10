from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User

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

    user = models.ForeignKey(User , on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    # location = models.
    job_type = models.CharField(max_length=20 , choices=JOB_TYPES)
    description = models.TextField(max_length=1000 , null=True, blank=True)
    img = models.ImageField(upload_to= 'photos/job/%y/%m/%d' , default= 'photo_default/default.png')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2 ,default=0.0 , null=True, blank=True)
    Category = models.ForeignKey(Categry , on_delete=models.SET_NULL , null=True , blank=True)
    experience = models.IntegerField(default=1)


    slug = models.SlugField( null=True , blank=True , unique=True)
    def save(self , *args , **kwarges):
        self.slug = slugify(self.title)
        super(job,self).save(*args , **kwarges)




    def __str__(self):
        return self.title




class Apply(models.Model):

    job = models.ForeignKey(job , related_name='apply_job'  ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    websit = models.URLField()
    cv = models.FileField(upload_to='applay/cvs/%m/%d')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
