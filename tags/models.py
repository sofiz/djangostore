from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255) #tagname

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) # an item can have multiple tags
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #type of the object you wanna use
    object_id = models.PositiveIntegerField() #ID of the object you wanna use
    content_object = GenericForeignKey() # the actual content of the object 
