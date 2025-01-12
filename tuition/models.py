from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

# Create your models here.
#here the return statement is used to show the actual name of the entry in the admin panel
#self.name=name shows the name of the post in the admin panel
#self.id shows the id of the post in the admin panel

#here a new model named Post is created with its coresponding fields
#also to show the table field in the admin panel register the post model in the admin.py file 

#part 15----------------------------
#adding an image field. First in settings.py create MEIDA_ROOT and MEDIA_URL
#then in the selected model(POST) add imagefield() as param default has been used. 
#to use Default image we have to define where the uploaded image will be saved. Use upload_to param
#Dont forget to makemigrations and migrate
#then to show the uploaded picture go to main urls.py file for more documentation

#-------------------part 16 Multiselect Field----------------
#install djang-multiselectfield
#add the pakkage to the installed apps from settings.py
#also import the in the models.py file

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    content=models.TextField()
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class_in(models.Model):
    name=models.CharField(max_length=100)
    section=models.CharField(max_length=5,default="A")

    def __str__(self):
        return self.name


class Post(models.Model):
    categories=(
        ('Teacher','Teacher'),
        ('Student','Student')
    )

    Medium=(('Bangla','Bangla'),
            ('English','English'),
            ('Urdu','Urdu'),
            ('Arabic','Arabic')
            )
    #use models.ForeignKey for one to many relationship
    #user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    email=models.EmailField()
    #2nd 
    salery=models.IntegerField() 
    details=models.TextField()
    available=models.BooleanField()
    category=models.CharField(max_length=100,choices=categories)
    image=models.ImageField(default='default.jpg',upload_to='media/images')
    #subjects=MultiSelectField(choices=medium,max_length=100,default='Bangla')
    medium=MultiSelectField(max_length=100,max_choices=3,choices=Medium,default="Bangla")

    #show=id.concat(title)

    #usage of ManyToMany field

    subject=models.ManyToManyField(Subject, related_name='Subjects_added')
    class_in=models.ManyToManyField(Class_in,related_name='Class_in')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output=(300,300)
            img.thumbnail(output)
            img.save(self.image.path)

    def __str__(self):
        return self.title




