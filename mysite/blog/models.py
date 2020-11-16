from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

class Topic (models.Model):
    title = models.CharField (max_length=255)
    slug= models.SlugField(max_length=255,unique=True)

    class Meta:
        ordering =['title']

    def __str__(self):
        return self.title

class Subtopic(models.Model):
    owner = models.ForeignKey (User,
                                related_name='subtopics_created', 
                                on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic,
                                related_name='subtopic', 
                                on_delete=models.CASCADE)
    title =models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique =True)
    detail =models.TextField()
    created = models.DateTimeField(auto_now_add=True)
        
    class Meta: 
        ordering = ['-created']

    def __str__(self):
        return self.title

class Content (models.Model):
    subtopic = (models.ForeignKey(Subtopic,
                                  related_name= 'contents',
                                  on_delete = models.CASCADE))
    content_type = models.ForeignKey (ContentType,
                                    on_delete = models.CASCADE,
                                    limit_choices_to = {'model__in':(
                                    'text',
                                    'video',
                                    'image',
                                    'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey ('content_type', 'object_id')

#Creating the content models

class ItemBase(models.Model):
    owner = models.ForeignKey (User,
                                related_name = '%(class)s_related',
                                on_delete = models.CASCADE)
    title = models. CharField(max_length = 255)
    created = models.DateTimeField (auto_now_add = True)
    updated = models. DateTimeField (auto_now = True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Text (ItemBase):
    content = models.TextField()

class File (ItemBase):
    file =models.FileField (upload_to ='files')

class Image (ItemBase):
    file = models.FileField(upload_to ='images')

class Video (ItemBase):
    url = models.URLField() 
