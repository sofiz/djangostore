from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # django module that tracks users
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  #type of the object you wanna use
    object_id = models.PositiveIntegerField() #ID of the object you wanna use
    content_object = GenericForeignKey() # the actual content of the object 
