from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_developer = models.BooleanField(default=False)    

    def __str__(self):
        return f"Name : {self.user.username}, Email : {self.user.email}, First name : {self.user.first_name}, Last name : {self.user.last_name}, Is_Developer {self.is_developer}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userdetails.save()

class BugDetails(models.Model):
    bugName = models.CharField(max_length=255)
    engineerName = models.CharField(max_length=64, blank=True)
    engineerDesignation = models.CharField(max_length=16, blank=True)
    progressStatus = models.CharField(max_length=16, default='Open')
    userName = models.CharField(max_length=64)
    userEmail = models.CharField(max_length=100, blank=True)
    userPhoneNumber = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Id : {self.id} || Bug name : {self.bugName} || Engineer Name : {self.engineerName} || Engineer Designation : {self.engineerDesignation} || Progress status : {self.progressStatus} || User Name : {self.userName} || User Email : {self.userEmail} || User Phone : {self.userPhoneNumber} || Description : {self.description} "

class Engineers(models.Model):
    name = models.CharField(max_length=64)
    designation = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} - {self.designation}"