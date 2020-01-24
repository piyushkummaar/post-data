from django.db import models

PUBLISH_CHOICES = [
    ('draft','Draft'
    ),
    ('publish','Publish'
    ),
    ('unpublish', 'Unpublish'),
]
class Post(models.Model):
    active = models.BooleanField(default=True)
    post_title = models.CharField(max_length=20,unique=True)
    slug = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    publish = models.CharField(
        max_length=124, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(null=True,blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    author_email = models.EmailField()
    
    def __str__(self):
        return self.post_title


