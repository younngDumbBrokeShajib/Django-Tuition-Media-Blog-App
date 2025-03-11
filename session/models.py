from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from PIL import Image



# Create your models here.


class CustomModelManager(models.Manager):
    def get_vip_cus(self):
        return self.annotate(post_count=Count('user__post')).filter(post_count__gt=3)
class UserModel(models.Model):
    gender=(
        ('Male','Male'),
        ('Female','Female'),
    )
    pro_category=(
        ('Studen','Student'),
        ('Tutor','Tutor'),
    )
    blood_group_choice=(
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
    )
    religion_choice=(
        ('Islam','Islam'),
        ('Hindu','Hindu'),
        ('Christian','Christian'),
    )

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bdate=models.DateField()
    gender=models.CharField(max_length=100,choices=gender)
    blood_group=models.CharField(max_length=100,choices=blood_group_choice)
    profession=models.CharField(max_length=50,choices=pro_category)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=13)
    bio=models.TextField()
    nationality=models.CharField(max_length=30)
    religion=models.CharField(max_length=50,choices=religion_choice)
    profile_pic=models.ImageField(default='default.jpg',upload_to='media/images')

    vip_author=CustomModelManager()
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()
        img=Image.open(self.profile_pic.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
