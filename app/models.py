from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

select=(
        ('SSLC', 'SSLC'),
        ('PUC', 'PUC'),
        ('Engineering','Engineering'),
        ('Masters','Masters')
    )

# Create your models here.
class Sslc(models.Model):
    category=models.CharField(max_length=20,choices=select)
    book_title=models.CharField(max_length=200)
    auth_name=models.CharField(max_length=40)
    published_date=models.DateTimeField(blank=True, null=True)
    text=models.TextField(default=True)

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # auth_name=models.EmailField(max_length=100)
    # created_date = models.DateTimeField(default=timezone.now)
    # text = models.TextField()
    
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse("cbv_app:post_detail_sslc", kwargs={"pk": self.pk})


class Puc(models.Model):
    category=models.CharField(max_length=20,choices=select)
    book_title=models.CharField(max_length=200)
    auth_name=models.CharField(max_length=30)
    published_date=models.DateTimeField(blank=True, null=True)
    text=models.TextField(default=True)

    def __str__(self):
        return self.book_title

class Engineering(models.Model):
    category=models.CharField(max_length=20,choices=select)
    book_title=models.CharField(max_length=200)
    auth_name=models.CharField(max_length=30)
    published_date=models.DateTimeField(blank=True, null=True)
    text=models.TextField(default=True)

    def __str__(self):
        return self.book_title

class Masters(models.Model):
    category=models.CharField(max_length=20,choices=select)
    book_title=models.CharField(max_length=200)
    auth_name=models.CharField(max_length=30)
    published_date=models.DateTimeField(blank=True, null=True)
    text=models.TextField(default=True)

    def __str__(self):
        return self.book_title

# Create your models here.
class User_data(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    webpage=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='user',blank=True)

    def __str__(self):
        return self.user.username
    