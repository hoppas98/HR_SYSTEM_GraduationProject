from django.db import models


# Create your models here.

class ContactUs(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, unique=False)
    Message = models.CharField(max_length=150)
    Created_date = models.DateTimeField(auto_now_add=True)


class PostsJobs(models.Model):
    Company_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Job_Title = models.CharField(max_length=150)
    Description = models.CharField(max_length=350)
    Created_date = models.DateTimeField(auto_now_add=True)


class ApplicantCV(models.Model):
    # Personal Info
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, unique=True)
    Street = models.CharField(max_length=150)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Phone = models.CharField('Volume Number', max_length=11)

    # Work Experience
    Job_Title = models.CharField(max_length=100)
    Company = models.CharField(max_length=150)
    City_Town_Work = models.CharField(max_length=50)
    Country_Work = models.CharField(max_length=50)
    Start_Date_Work = models.CharField(max_length=16)
    End_Date_Work = models.CharField(max_length=16)

    # Eduction
    School_Name = models.CharField(max_length=150)
    City_Town_School = models.CharField(max_length=50)
    Country_School = models.CharField(max_length=50)
    Degree = models.CharField(max_length=150)
    Graduation_Date = models.CharField(max_length=16)
    University_Name = models.CharField(max_length=255)

    # Skills
    Skills_1 = models.CharField(max_length=50)
    Skills_2 = models.CharField(max_length=50)
    Skills_3 = models.CharField(max_length=50)
    Skills_4 = models.CharField(max_length=50)
    Skills_5 = models.CharField(max_length=50)
    Skills_6 = models.CharField(max_length=50)
    Skills_7 = models.CharField(max_length=50)
    Skills_8 = models.CharField(max_length=50)
    Skills_9 = models.CharField(max_length=50)
    pdf_cv = models.CharField(max_length=50)

    Created_date = models.DateTimeField(auto_now_add=True)
