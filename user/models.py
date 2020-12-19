from django.db import models

# Create your models here.

class UserDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    username = models.CharField(unique=True,max_length=300)
    enroll_no = models.IntegerField(unique=True,
        error_messages={
            'unique': ("A user with that Enroll Number already exists."),
        })
    roll_no = models.IntegerField(unique=True,
        error_messages={
            'unique': ("A user with that Roll Number already exists."),
        },)
    mobile = models.IntegerField()
    photo = models.ImageField(upload_to='myprofile')
    
    