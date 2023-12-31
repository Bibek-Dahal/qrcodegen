from django.db import models

# Create your models here.
class Person(models.Model):
    
    gender_choices = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),

    )
    first_name = models.CharField(verbose_name=("person first name"),max_length=15)
    middle_name = models.CharField('middle name',max_length=15,blank=True,null=True)
    last_name = models.CharField(verbose_name=("last name"),max_length=15)
    email = models.EmailField("E-mail",unique=True)
    gender = models.CharField("gender",max_length=1,choices=gender_choices,default='M')
    age = models.SmallIntegerField("age")
    date_of_birth = models.DateField("date of birth")
    slug = models.SlugField("slug",unique=True)
    weight = models.DecimalField("weight",max_digits=3,decimal_places=1)
    description = models.TextField("description",max_length=255)
    is_active = models.BooleanField("is active",default=False)
    created_at = models.DateTimeField("created at",auto_now_add=True)
    updated_at = models.DateTimeField("updated at",auto_now=True)


    
class Baby(models.Model):
    first_name = models.CharField(verbose_name=("first name"),max_length=15)
    middle_name = models.CharField('middle name',max_length=15,blank=True,null=True)
    last_name = models.CharField(verbose_name=("last name"),max_length=15)


    class Meta:
        db_table = "its_baby_table"
        verbose_name = "baby"
        verbose_name_plural = "babies"
        ordering = ["first_name"]
        unique_together = [["first_name", "last_name"]]



class Vehicle(models.Model):
    model_number = models.CharField(max_length=10)
    color = models.CharField(max_length=12)

    class Meta:
        abstract = True



