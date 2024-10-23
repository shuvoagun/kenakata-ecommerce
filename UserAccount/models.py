from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Division, District, SubDistrict

class CustomUserManager(BaseUserManager): # don't integrate on dashboard
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.pop('email', None)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, password=password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin): # don't integrate on dashboard
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=60, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return  self.email or self.phone or "Unnamed User"



    

class Profile(models.Model): # don't integrate on dashboard
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="sellerpicture", default='avatar.png')
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='profiles', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='profiles', blank=True, null=True)
    sub_district = models.ForeignKey(SubDistrict, on_delete=models.CASCADE, related_name='profiles', blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.email or self.user.phone 

    class Meta:
        verbose_name_plural = "Profiles"
        



@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
