from django.db import models

# Create your models here.

class Catagory (models.Model):

  Title = models.CharField (max_length=30)

  def __str__(self) -> str:
    return self.Title
  

class Login_Data (models.Model):

  first_name = models.CharField (max_length=30)
  last_name = models.CharField (max_length=30)

  def __str__(self) -> str:
    return self.first_name + self.last_name
  

class Post_Music (models.Model):

  artist = models.CharField (max_length=30)
  Music_Title = models.CharField (max_length=20)
  cover_picture = models.ImageField (upload_to='Music_Background/',null=True, blank=True)
  music = models.FileField (null=True, blank=True)
  release_date = models.DateField (null=False, blank=False, auto_created=True, auto_now_add=True)

  def __str__(self) -> str:
    return self.artist