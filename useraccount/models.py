from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
 
class User(AbstractUser):
    statuses = [("CG","Care Giver"),("CT","Care Reciever")]

    email = models.EmailField(unique=True, blank=True)
    pic = models.ImageField(upload_to="useraccount/", blank=True)
    bio = models.TextField(blank=True)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    location = models.CharField(blank=True, max_length=30)
    user_type = models.CharField(max_length=2,choices=statuses, default='CG')
    fees = models.IntegerField(blank=True, null=True)
 
    def __str__(self): 
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='user', on_delete=models.CASCADE)
    friends = models.ManyToManyField(get_user_model(), blank=True, related_name='profile')

    def __str__(self):
        return '{}'.format(self.user)


    def get_friends(self):
        return self.friends.all()

    def get_friends_count(self):
        return self.friends.all().count()



class Addfriend(models.Model):
    CHOICES = [('send', 'send'), ('accepted', 'accepted')]

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reciever')
    status = models.CharField(max_length=8, choices=CHOICES, default='send')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.sender}-{self.reciever}-{self.status}"




class Review(models.Model):
    from_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="from_user", null=True, blank=True)
    to_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="to_user", null=True, blank=True)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
