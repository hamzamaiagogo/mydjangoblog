from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
      author=models.ForeignKey('auth.User')
      title=models.CharField(max_length=200)
      text=models.TextField()
      created_date=models.DateTimeField(default=timezone.now)
      published_date=models.DateTimeField(blank=True, null=True)
      
      def publish(self):
          self.published_date=timezone.now()
          self.save()
      def __unicode__(self):
          return self.title

class Contact(models.Model):
      name=models.CharField(max_length=50)
      mail=models.CharField(max_length=50)
      phone=models.IntegerField()
      text=models.TextField()
      
 
      def __unicode__(self):
          return self.name
class UserProfile(models.Model):
      # This line is required. Links UserProfile to a User model instance.
      user = models.OneToOneField(User)
      # The additional attributes we wish to include.
      website = models.URLField(blank=True)
      picture = models.ImageField(upload_to='profile_images', blank=True)
      # Override the __unicode__() method to return out something meaningful!
      def __unicode__(self):
          return self.user.username

