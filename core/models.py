from django.db import models

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=200, unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubDistrict(models.Model):
    name = models.CharField(max_length=200, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
        
class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='About_us-image')
    img1 = models.ImageField(upload_to='About_us-image', blank=True, null=True)
    img2 = models.ImageField(upload_to='About_us-image', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    

class faq(models.Model):
    questions = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.questions
    
    
    
class TermsCondition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    
    
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title