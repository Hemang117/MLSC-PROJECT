from django.db import models
class loginpage(models.Model):
    loginpage_Username=models.CharField(max_length=50)
    loginpage_Email=models.EmailField((""), max_length=254)
    loginpage_Password=models.CharField(max_length=50)

class profile(models.Model):
    profile_Hostel=models.CharField(max_length=50)
    profile_HostelBlock=models.CharField(max_length=20)
    profile_RoomNo=models.IntegerField(max_length=10)
    profile_contact=models.IntegerField(max_length=10)
    
class notice(models.Model):
    notice_Notice=models.CharField(max_length=250)

class application(models.Model):
    application_Appl=models.CharField(max_length=800)

class events(models.Model):
    events_Eve=models.CharField(max_length=150)

class lof(models.Model):
    lof_fol=models.CharField(max_length=100)

class queries(models.Model):    
    queries_Query=models.CharField(max_length=900)


# Create your models here.

